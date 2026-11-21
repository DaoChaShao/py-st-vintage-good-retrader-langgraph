#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/21 19:59
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   account.py
# @Desc     :

from typing import Any

from requests import request

from backend.fapi import User

from .base import HEADERS
from .types import URL, RequestMethods


def request_to_post_signin(url: str, *, username: str, password: str) -> Any:
    """
    Post username and password to sign in via the given URL

    :param url: The URL to post the user to
    :param username: The username of the user
    :param password: The password of the user
    :return: The response from the server
    """
    _user = User(username=username, password=password)
    _url: URL = URL(url)
    return request(
        RequestMethods.POST.value,
        _url.value,
        headers=HEADERS,
        timeout=30,
        json=_user.model_dump(),
    )


def request_to_post_signup(url: str, *, username: str, password: str) -> Any:
    """
    Post username and password to register a new user via the given URL

    :param url: The URL to post the user to
    :param username: The username of the user
    :param password: The password of the user
    :return: The response from the server
    """
    _user = User(username=username, password=password)
    _url: URL = URL(url)
    return request(
        RequestMethods.POST.value,
        _url.value,
        headers=HEADERS,
        timeout=30,
        json=_user.model_dump(),
    )
