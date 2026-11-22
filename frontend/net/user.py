#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/21 19:59
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   user.py
# @Desc     :

from datetime import datetime
from typing import Any

from requests import Response, request

from backend.fapi import UserSignIn, UserUpdate

from .base import HEADERS
from .types import URL, RequestMethods


def request_to_sign_in(url: str, *, username: str, password: str) -> Any:
    """
    Post username and password to sign in via the given URL

    :param url: The URL to post the user to
    :param username: The username of the user
    :param password: The password of the user
    :return: The response from the server
    """
    _user = UserSignIn(username=username, password=password)
    _url: URL = URL(url)
    return request(
        RequestMethods.POST.value,
        _url.value,
        headers=HEADERS,
        timeout=30,
        json=_user.model_dump(),
    )


def request_to_sign_up(url: str, *, username: str, password: str) -> Any:
    """
    Post username and password to register a new user via the given URL

    :param url: The URL to post the user to
    :param username: The username of the user
    :param password: The password of the user
    :return: The response from the server
    """
    _user = UserSignIn(username=username, password=password)
    _url: URL = URL(url)
    return request(
        RequestMethods.POST.value,
        _url.value,
        headers=HEADERS,
        timeout=30,
        json=_user.model_dump(),
    )


def request_to_update(
        url: str | URL,
        *,
        user_id: int,
        username: str,
        old_password: str | None,
        new_password: str | None,
        role: str,
        status: bool,
        updated_at: datetime,
) -> Response:
    """
    Update info

    :param url: The URL to post the user to
    :param user_id: The id of the user
    :param username: The username of the user
    :param old_password: The original password of the user
    :param new_password: The new password of the user
    :param role: The role of the user
    :param status: The status of the user
    :param updated_at: The last updated time of the user
    :return: The response from the server
    """
    _user: UserUpdate = UserUpdate(
        id=user_id,
        username=username,
        old_password=old_password,
        new_password=new_password,
        role=role,
        is_active=status,
        updated_at=updated_at,
    )
    _url: URL = URL(url)
    return request(
        RequestMethods.POST.value,
        _url.UPDATE.value,
        headers=HEADERS,
        timeout=30,
        json=_user.model_dump(mode="json"),
    )
