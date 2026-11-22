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

from .types import AccessTokenTypes, ResponseStatus


class CRUDResponse(BaseModel):
    """ Response for CRUD operations """

    code: int | ResponseStatus
    message: str | ResponseStatus


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
    # Timestamps
    created_at: datetime | None
    updated_at: datetime | None


class GoodsResponse(CRUDResponse):
    """ Response for goods endpoint """

    data: list[GoodResponse]


class TablesResponse(CRUDResponse):
    """ Response for table endpoint """

    data: list[str]


class UserBase(BaseModel):
    """ User base schema """

    model_config = ConfigDict(from_attributes=True)

    username: str


class UserSignIn(UserBase):
    """ User base schema """

    password: str


class UserUpdate(UserBase):
    """ User schema """

    # Main Keys
    id: int
    # Attributes
    old_password: str | None
    new_password: str | None
    is_active: bool
    role: str
    # Timestamps
    updated_at: datetime


class UserResponse(UserBase):
    """ Response for a single user """

    # Main Key
    id: int
    # Attributes
    is_active: bool
    role: str
    # Timestamps
    created_at: datetime | None
    updated_at: datetime | None


class AccessTokenResponse(BaseModel):
    """ Response for user authentication """

    model_config = ConfigDict(from_attributes=True)

    token: str
    type: str | AccessTokenTypes = AccessTokenTypes.BEARER
    expires_at: int


class VerificationResponse(BaseModel):
    """ Response for successful login """

    model_config = ConfigDict(from_attributes=True)

    code: int | ResponseStatus
    message: str | ResponseStatus
    user: UserResponse
    token: AccessTokenResponse
