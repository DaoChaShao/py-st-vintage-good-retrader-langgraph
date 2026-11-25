#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/23 17:19
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   test.py
# @Desc     :

from fastapi import APIRouter

from ...schemas import CRUDResponse
from ...types import ResponseStatus

router = APIRouter()


@router.get("", response_model=CRUDResponse)
async def test_goods() -> CRUDResponse:
    """ Test the goods endpoint """
    _status = ResponseStatus
    return CRUDResponse(
        code=_status.SUCCESS.code,
        message=_status.SUCCESS.message
    )
