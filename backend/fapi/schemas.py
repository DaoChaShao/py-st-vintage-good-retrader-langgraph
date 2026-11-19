#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 23:21
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   schemas.py
# @Desc     :

from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from .types import ResponseStatus


class GoodResponse(BaseModel):
    """ Response for a single good """
    model_config = ConfigDict(from_attributes=True)

    # Main Key
    id: int
    # Attributes
    purchase_date: date | None
    sale_date: date | None
    product: str | None
    category: str | None
    price: Decimal | None
    quantity: int | None
    description: str | None

    created_at: datetime | None
    updated_at: datetime | None


class GoodsResponse(BaseModel):
    """ Response for goods endpoint """
    code: int | ResponseStatus
    message: str | ResponseStatus
    data: list[GoodResponse]
