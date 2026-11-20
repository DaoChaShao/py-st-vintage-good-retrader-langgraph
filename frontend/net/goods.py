#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 20:48
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   goods.py
# @Desc     :

from typing import Any

from fake_useragent import UserAgent
from requests import get
from streamlit import cache_data

from .types import URL, HttpHeader

UA = UserAgent()

HEADERS: dict[str, Any] = {
    "User-Agent": UA.random,
    "Accept": HttpHeader.APPLICATION_JSON.value
}


@cache_data(ttl=60)
def get_goods(url: str | URL) -> list[dict]:
    _url: URL = URL(url)
    _response = get(
        _url.value,
        headers=HEADERS,
        timeout=30
    )
    _response.raise_for_status()
    return _response.json()["data"]
