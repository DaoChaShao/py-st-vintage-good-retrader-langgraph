#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/17 23:13
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :


"""
***************************************************************
FastAPI Core - Backend API Management Toolkit
---------------------------------------------------------------
This package provides a collection of reusable utilities, classes,
and components for API routing, request validation, response handling,
business logic and dependency management.

Designed to provide a modular, extensible, and consistent interface
for building and managing asynchronous RESTful APIs with FastAPI.
***************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .dependencies import yield_async_session
from .schemas import (
    GoodCreation,
    UserInit,
    UserManagement,
    UsersDeletion,
    UserSignIn,
    UsersManagement,
    UserUpdate,
)
from .services import JWTAccessTokenEncoder
from .session import InitAsyncSession
from .types import (
    AccessTokenTypes,
    ProductTypes,
    ResponseStatus,
)

__all__ = [
    "yield_async_session",

    "GoodCreation",
    "UsersDeletion",
    "UserInit",
    "UserUpdate",
    "UsersManagement",
    "UserSignIn",
    "UserManagement",

    "JWTAccessTokenEncoder",

    "InitAsyncSession",

    "ResponseStatus",
    "ProductTypes",
    "AccessTokenTypes",
]
