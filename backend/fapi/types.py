#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 20:19
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   types.py
# @Desc     :

from enum import Enum, StrEnum, unique


@unique
class ResponseStatus(Enum):
    SUCCESS = (200, "Success")
    CREATED = (201, "Created")
    BAD_REQUEST = (400, "Bad Request")
    UNAUTHORISED = (401, "Unauthorised")
    FORBIDDEN = (403, "Forbidden")
    NOT_FOUND = (404, "Not Found")
    CONFLICT = (409, "Conflict")
    VALIDATION_ERROR = (422, "Validation Error")
    INTERNAL_SERVER_ERROR = (500, "Internal Server Error")

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


@unique
class AccessTokenTypes(StrEnum):
    BEARER = "bearer"
