#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/23 17:19
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   test.py
# @Desc     :

from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def test_goods():
    return {"message": "Goods endpoint works"}
