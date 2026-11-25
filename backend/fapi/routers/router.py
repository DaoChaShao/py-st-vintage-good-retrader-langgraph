#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 00:07
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   router.py
# @Desc     :

from fastapi import APIRouter

from .endpoints import (
    category,
    database,
    goods,
    test,
    user,
)

router = APIRouter()

# Register the routers
router.include_router(category.router, prefix="/category", tags=["category"])
router.include_router(database.router, prefix="/crud", tags=["crud"])
router.include_router(goods.router, prefix="/goods", tags=["goods"])
router.include_router(test.router, prefix="/test", tags=["test"])
router.include_router(user.router, prefix="/user", tags=["user"])
