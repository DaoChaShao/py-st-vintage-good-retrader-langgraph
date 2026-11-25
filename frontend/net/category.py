#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/25 22:36
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   category.py
# @Desc     :

from requests import request

from .base import HEADERS
from .types import URL, RequestMethod


def request_to_get_category(url: str) -> dict[str, list]:
    """
    Get all user types

    :param url: The URL to get the user types from
    :return: The response from the server
    """
    _url: URL = URL(url)
    _response = request(
        RequestMethod.GET.value,
        _url.value,
        headers=HEADERS,
        timeout=30
    )
    _response.raise_for_status()
    return _response.json()["category"]
