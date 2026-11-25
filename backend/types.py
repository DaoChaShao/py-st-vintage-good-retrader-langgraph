#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 22:12
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   types.py
# @Desc     :

from enum import Enum, StrEnum, unique


@unique
class AccessTokenType(StrEnum):
    """ Access Token Type """
    BEARER = "bearer"


@unique
class DBType(StrEnum):
    """ Database Type """

    SQLITE = "sqlite"
    POSTGRES = "postgres"


@unique
class ExecutionMode(StrEnum):
    """ Execution Mode """

    SYNC = "sync"
    ASYNC = "async"


@unique
class HashAlgorithm(StrEnum):
    """ Hash Algorithm For Password Hashing """

    BCRYPT = "bcrypt"
    PBKDF2 = "pbkdf2"
    SCRYPT = "scrypt"
    ARGON2 = "argon2"


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
class UserRole(StrEnum):
    """ Role """

    ADMIN = "admin"
    USER = "user"
