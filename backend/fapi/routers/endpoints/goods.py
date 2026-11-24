#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 11:16
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   goods.py
# @Desc     :

from datetime import date
from decimal import Decimal
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ....dbkit import Goods
from ...dependencies import yield_async_session
from ...schemas import (
    CRUDResponse,
    GoodCreation,
    GoodResponse,
    GoodsResponse,
)
from ...types import ResponseStatus

router = APIRouter()


@router.get("", response_model=GoodsResponse)
async def to_get_goods(session: Annotated[AsyncSession, Depends(yield_async_session)]) -> GoodsResponse:
    """
    Get all goods

    :param session: The database session
    :type session: AsyncSession
    """
    _result = await session.execute(select(Goods))
    _goods = _result.scalars().all()
    _status = ResponseStatus
    return GoodsResponse(
        code=_status.SUCCESS.code,
        message=_status.SUCCESS.message,
        goods=[GoodResponse.model_validate(good) for good in _goods],
    )


@router.post("/create", response_model=GoodResponse)
async def to_create_good(
        good: GoodCreation,
        session: Annotated[AsyncSession, Depends(yield_async_session)],
) -> GoodResponse:
    """
    Create a new good

    :param good: The good to create
    :param session: The database session
    :return: The created good
    """
    _good = Goods(**good.model_dump())

    session.add(_good)
    await session.commit()
    await session.refresh(_good)
    return GoodResponse.model_validate(_good)


@router.delete("/delete", response_model=CRUDResponse)
async def to_delete_good(
        db_id: int,
        session: Annotated[AsyncSession, Depends(yield_async_session)],
) -> CRUDResponse:
    """
    Delete a good
    :param db_id: The ID of the good to delete
    :param session: The database session
    :return: The deletion response
    """
    _status = ResponseStatus
    _good = await session.get(Goods, db_id)

    if _good is None:
        raise HTTPException(status_code=_status.NOT_FOUND.code, detail=_status.NOT_FOUND.message)

    await session.delete(_good)
    await session.commit()

    return CRUDResponse(
        code=_status.SUCCESS.code,
        message=_status.SUCCESS.message,
    )


@router.patch("/update", response_model=GoodResponse)
async def to_update_good(
        db_id: int,
        good: GoodCreation,
        session: Annotated[AsyncSession, Depends(yield_async_session)],
) -> GoodResponse:
    """
   Update a good

   :param db_id: The ID of the good to update
   :param good: The good to update
   :param session: The database session
   :return: The updated good
   """
    _status = ResponseStatus
    _good = await session.get(Goods, db_id)

    if _good is None:
        raise HTTPException(status_code=_status.NOT_FOUND.code, detail=_status.NOT_FOUND.message)

    for key, value in good.model_dump().items():
        setattr(_good, key, value)

    await session.commit()
    await session.refresh(_good)

    return GoodResponse.model_validate(_good)


@router.patch("/sell", response_model=GoodResponse)
async def to_sell_good(
        db_id: int,
        sale_price: Decimal,
        session: Annotated[AsyncSession, Depends(yield_async_session)],
) -> GoodResponse:
    _status = ResponseStatus
    _good = await session.get(Goods, db_id)

    if _good is None:
        raise HTTPException(status_code=_status.NOT_FOUND.code, detail=_status.NOT_FOUND.message)

    if _good.sale_date is not None:
        raise HTTPException(status_code=_status.CONFLICT.code, detail="The good has already been sold.")

    if _good.expected_profit is None:
        raise HTTPException(
            status_code=_status.VALIDATION_ERROR.code,
            detail="Expected profit must be specified before selling."
        )

    if sale_price <= 0:
        raise HTTPException(status_code=_status.VALIDATION_ERROR.code, detail="Sale price must be greater than zero.")

    _good.sale_date = date.today()
    _good.sale_price = sale_price

    await session.commit()
    await session.refresh(_good)

    return GoodResponse.model_validate(_good)
