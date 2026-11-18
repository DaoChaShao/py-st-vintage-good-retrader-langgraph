#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 23:21
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   schemas.py
# @Desc     :

from datetime import date
from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field


class GoodsBase(BaseModel):
    purchase_date: Annotated[date, Field(description="The date the goods were purchased")]
    sale_date: Annotated[date | None, Field(description="The date the goods were sold")]
    product: Annotated[str | None, Field(description="The name of the product")]
    category: Annotated[str | None, Field(description="The category of the product")]
    price: Annotated[Decimal | None, Field(description="The price of the product")]
    quantity: Annotated[int | None, Field(description="The quantity of the product")]
    description: Annotated[str | None, Field(description="A description of the product")]


class GoodsCreate(GoodsBase):
    """ Data required to create goods """
    pass


class GoodsUpdate(GoodsBase):
    """ Data allowed when updating goods """
    pass


class GoodsResponse(GoodsBase):
    """ Data returned by the API """
    id: int

    model_config = ConfigDict(from_attributes=True)
