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

from backend.fapi import (
    UserManagement,
    UserSignIn,
    UsersManagement,
    UserUpdate,
)

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


def request_to_get_users(url: str | URL) -> Any:
    _url: URL = URL(url)
    _response = request(
        RequestMethods.GET.value,
        _url.value,
        headers=HEADERS,
        timeout=30
    )
    _response.raise_for_status()
    return _response.json()["users"]


def request_to_manage_users(url: str, *, changed_users: list[dict]) -> Any:
    """ Update multiple users """
    _url = URL(url)
    _users = [
        UserManagement.model_validate(user)
        for user in changed_users
    ]
    _data = UsersManagement(users=_users)
    return request(
        RequestMethods.PATCH.value,
        _url.value,
        headers=HEADERS,
        timeout=30,
        json=_data.model_dump(mode="json"),
    )


def request_to_init_admin(url: str) -> Any:
    """
    Post username and password to register a new user via the given URL

    :param url: The URL to post the user to
    :return: The response from the server
    """
    _url: URL = URL(url)
    return request(
        RequestMethods.POST.value,
        _url.value,
        headers=HEADERS,
        timeout=30,
    )
