#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 20:48
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   goods.py
# @Desc     :


from requests import request
from streamlit import cache_data

from .base import HEADERS
from .types import URL, RequestMethods


@cache_data(ttl=60)
def request_to_get_goods(url: str | URL) -> list[dict]:
    _url: URL = URL(url)
    _response = request(
        RequestMethods.GET.value,
        _url.value,
        headers=HEADERS,
        timeout=30
    )
    _response.raise_for_status()
    return _response.json()["data"]
