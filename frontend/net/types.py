#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 21:02
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   category.py
# @Desc     :

from enum import StrEnum, unique


@unique
class AcceptType(StrEnum):
    """ HTTP Header """
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"


@unique
class DBReadyStatus(StrEnum):
    INIT = "init"
    STOP = "stop"


@unique
class RequestMethod(StrEnum):
    """ HTTP Method """
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


BASE: str = "http://127.0.0.1:8000/api"


@unique
class URL(StrEnum):
    """ URL """
    TEST = BASE + "/test"
    USER = BASE + "/user"

    DELETE_TABLES = BASE + "/crud/delete/tables"
    INITIALISE_TABLES = BASE + "/crud/initialise/tables"
    LIST_TABLES = BASE + "/crud/list/tables"

    SIGN_UP = BASE + "/user/sign/up"
    SIGN_IN = BASE + "/user/sign/in"
    UPDATE = BASE + "/user/update"

    GET_USERS = BASE + "/user/get/users"
    MANAGE_USERS = BASE + "/user/manage/users"

    INIT_ADMIN = BASE + "/user/init/admin"
    DELETE_USERS = BASE + "/user/delete"
    # -----
    GET_GOODS = BASE + "/goods"
    CREATE_GOOD = BASE + "/goods/create"
    DELETE_GOOD = BASE + "/goods/delete"
    UPDATE_GOOD = BASE + "/goods/update"
    SELL_GOOD = BASE + "/goods/sell"
    RESTOCK_GOOD = BASE + "/goods/restock"

    GET_CATEGORY = BASE + "/category"
