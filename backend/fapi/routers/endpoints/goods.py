#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 11:16
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   goods.py
# @Desc     :

from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...dependencies import yield_async_session
from ...schemas import GoodResponse, GoodsResponse
from ...services import async_read_records
from ...types import ResponseStatus

router = APIRouter()


@router.get("/test")
async def test_goods():
    return {"message": "Goods endpoint works"}


@router.get(
    "",
    response_model=GoodsResponse
)
async def get_goods(session: Annotated[AsyncSession, Depends(yield_async_session)]) -> GoodsResponse:
    _records = await async_read_records(session)
    _status = ResponseStatus.SUCCESS
    return GoodsResponse(
        code=_status.code,
        message=_status.message,
        data=[GoodResponse.model_validate(record) for record in _records],
    )
