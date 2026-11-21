#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 21:02
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   types.py
# @Desc     :

from enum import StrEnum, unique


@unique
class AcceptTypes(StrEnum):
    """ HTTP Header """
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"


@unique
class RequestMethods(StrEnum):
    """ HTTP Method """
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


BASE: str = "http://127.0.0.1:8000/api"


@unique
class URL(StrEnum):
    """ URL """
    TEST = BASE + "/test"
    GOODS = BASE + "/goods"
    USER = BASE + "/user"

    DELETE_TABLES = BASE + "/crud/delete/tables"
    INITIALISE_TABLES = BASE + "/crud/initialise/tables"
    LIST_TABLES = BASE + "/crud/list/tables"

    REGISTRATION = BASE + "/account/registration"
    VERIFICATION = BASE + "/account/verification"
