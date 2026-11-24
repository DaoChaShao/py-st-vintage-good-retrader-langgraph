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

from ..dbkit import UserRoles
from .types import (
    AccessTokenTypes,
    ProductTypes,
    ResponseStatus,
)


class CRUDResponse(BaseModel):
    """ Response for CRUD operations """

    code: int | ResponseStatus
    message: str | ResponseStatus


class UserBase(BaseModel):
    """ User base schema """

    model_config = ConfigDict(from_attributes=True)

    username: str


class UserSignIn(UserBase):
    """ User base schema """

    password: str


class UserManagement(UserBase):
    """ User management schema """

    # Main Key
    id: int
    # Attributes
    is_active: bool
    role: UserRoles


class UsersManagement(BaseModel):
    """ Users management schema """

    users: list[UserManagement]


class UserUpdate(UserBase):
    """ User schema """

    # Main Keys
    id: int
    # Attributes
    old_password: str | None
    new_password: str | None
    is_active: bool
    role: UserRoles
    # Timestamps
    updated_at: datetime


class UserInit(UserSignIn):
    """ User init schema """

    role: UserRoles = UserRoles.ADMIN.value


class UsersDeletion(BaseModel):
    """ User deletion schema """

    ids: list[int]


class UserResponse(UserBase):
    """ Response for a single user """

    # Main Key
    id: int
    # Attributes
    is_active: bool
    role: UserRoles
    # Timestamps
    created_at: datetime | None
    updated_at: datetime | None


class UsersResponse(CRUDResponse):
    """ Response for users endpoint """

    users: list[UserResponse]


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


class GoodCreation(BaseModel):
    """ Schema for creating a good """

    model_config = ConfigDict(from_attributes=True)

    # Dates
    purchase_date: date | None = None
    sale_date: date | None = None
    # Product Information
    sku: str | None = None
    city: str | None = None
    store: str | None = None
    product: str | None = None
    production_year_start: int | None = None
    production_year_end: int | None = None
    brand: str | None = None
    series: str | None = None
    generation: int | None = None
    category: ProductTypes | None = None
    # Quantity
    set: int | None = None
    piece: int | None = None
    # Financial Information
    purchase_price: Decimal | None = None
    exchange_rate: Decimal | None = None
    shipping_fee: Decimal | None = None
    expected_profit: Decimal | None = None
    sale_price: Decimal | None = None
    # Description
    description: str | None = None


class GoodResponse(GoodCreation):
    """ Response for a single good """

    id: int
    created_at: datetime
    updated_at: datetime


class GoodsResponse(CRUDResponse):
    """ Response for goods endpoint """

    goods: list[GoodResponse]


class TablesResponse(CRUDResponse):
    """ Response for table endpoint """

    tables: list[str]
