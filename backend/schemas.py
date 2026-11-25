#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 23:21
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   schemas.py
# @Desc     :

from datetime import date, datetime
from decimal import Decimal

from pydantic import Field

from .base import ABSSchema
from .domains import ProductTypes
from .types import AccessTokenType, ResponseStatus, UserRole


class DBGeneral(ABSSchema):
    """ General database configuration schema """

    echo: bool = False
    timeout: int = Field(default=30, gt=0)
    pool_size: int = Field(default=5, ge=0)
    max_overflow: int = Field(default=10, ge=0)


class SQLite(DBGeneral):
    """ SQLite database configuration schema """

    database: str


class PostgresSQL(DBGeneral):
    """ PostgresSQL database configuration schema """

    user: str
    password: str
    host: str
    port: int
    database: str
    ssl: str = "require"


class CRUDResponse(ABSSchema):
    """ Response for CRUD operations """

    code: int | ResponseStatus
    message: str | ResponseStatus


class UserBase(ABSSchema):
    """ User base schema """

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
    role: UserRole


class UsersManagement(ABSSchema):
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
    role: UserRole
    # Timestamps
    updated_at: datetime


class UserInit(UserSignIn):
    """ User init schema """

    role: UserRole = UserRole.ADMIN.value


class UsersDeletion(ABSSchema):
    """ User deletion schema """

    ids: list[int]


class UserResponse(UserBase):
    """ Response for a single user """

    # Main Key
    id: int
    # Attributes
    is_active: bool
    role: UserRole
    # Timestamps
    created_at: datetime | None
    updated_at: datetime | None


class UsersResponse(CRUDResponse):
    """ Response for users endpoint """

    users: list[UserResponse]


class AccessTokenResponse(ABSSchema):
    """ Response for user authentication """

    token: str
    type: str | AccessTokenType = AccessTokenType.BEARER
    expires_at: int


class VerificationResponse(ABSSchema):
    """ Response for successful login """

    code: int | ResponseStatus
    message: str | ResponseStatus
    user: UserResponse
    token: AccessTokenResponse


class GoodCreation(ABSSchema):
    """ Schema for creating a good """

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
    # Financial Information for store
    purchase_price: Decimal | None = None
    extra_fee: Decimal | None = None
    exchange_rate: Decimal | None = None
    expected_profit: Decimal | None = None
    # Financial Information for customer
    customer: str | None = None
    gender: str | None = None
    location: str | None = None
    shipping_fee: Decimal | None = None
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


class Customer(ABSSchema):
    """ Customer schema """

    customer: str
    gender: str | None
    location: str
    shipping_fee: Decimal
    sale_price: Decimal
