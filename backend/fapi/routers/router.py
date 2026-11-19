#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 00:07
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   router.py
# @Desc     :

from fastapi import APIRouter

from .endpoints import (
    goods,
)

router = APIRouter()

# Register the routers
router.include_router(goods.router, prefix="/goods", tags=["goods"])
