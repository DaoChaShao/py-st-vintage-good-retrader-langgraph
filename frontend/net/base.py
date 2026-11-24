#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/21 19:54
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   base.py
# @Desc     :

from typing import Any

from fake_useragent import UserAgent

from .types import AcceptType

UA = UserAgent()

HEADERS: dict[str, Any] = {
    "User-Agent": UA.random,
    "Accept": AcceptType.APPLICATION_JSON.value
}
