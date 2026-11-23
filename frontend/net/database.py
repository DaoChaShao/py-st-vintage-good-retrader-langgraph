#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/21 21:45
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   database.py
# @Desc     :

from requests import request

from .base import HEADERS
from .types import URL, RequestMethods


def request_to_delete_tables(url: str | URL) -> None:
    """
    Delete all tables in the database

    :param url: The URL to delete the tables from
    :return: None
    """
    _url: URL = URL(url)
    _response = request(
        RequestMethods.DELETE.value,
        _url.DELETE_TABLES.value,
        headers=HEADERS,
        timeout=30,
    )
    _response.raise_for_status()


def request_to_list_tables(url: str | URL) -> list[str]:
    """
    List all tables in the database

    :param url: The URL to list the tables from
    :return: A list of table names
    """
    _url: URL = URL(url)
    _response = request(
        RequestMethods.GET.value,
        _url.LIST_TABLES.value,
        headers=HEADERS,
        timeout=30,
    )
    return _response.json()["data"]


def request_to_initialise_tables(url: str | URL) -> None:
    """
    Initialise all tables in the database

    :param url: The URL to initialise the tables at
    :return: None
    """
    _url: URL = URL(url)
    _response = request(
        RequestMethods.POST.value,
        _url.INITIALISE_TABLES.value,
        headers=HEADERS,
        timeout=30,
    )
    _response.raise_for_status()
