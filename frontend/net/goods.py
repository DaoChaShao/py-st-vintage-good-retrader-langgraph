#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 20:48
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   goods.py
# @Desc     :

from typing import Any

from requests import Response, request
from streamlit import cache_data

from backend.fapi import (
    Customer,
    GoodCreation,
)

from .base import HEADERS
from .types import URL, RequestMethod


@cache_data(ttl=60)
def request_to_get_goods(url: str | URL) -> list[dict]:
    """
    Get goods from the given URL

    :param url: The URL to get the goods from
    :return: The goods
    """
    _url: URL = URL(url)
    _response = request(
        RequestMethod.GET.value,
        _url.value,
        headers=HEADERS,
        timeout=30
    )
    _response.raise_for_status()
    return _response.json()["goods"]


def request_to_post_good(url: str | URL, good: dict[str, Any]) -> Response:
    """
    Post a good to the given URL

    :param url: The URL to post the good to
    :param good: The good to post
    :return: The response
    """
    _url: URL = URL(url)
    _good: GoodCreation = GoodCreation(**good)
    return request(
        RequestMethod.POST.value,
        _url.value,
        headers=HEADERS,
        timeout=30,
        json=_good.model_dump(mode="json"),
    )


def request_to_delete_good(url: str | URL, db_id: int) -> Response:
    """
    Delete a good from the given URL

    :param url: The URL to delete the good from
    :param db_id: The db_id of the good to delete
    :return: The response
    """
    _url: URL = URL(url)
    return request(
        RequestMethod.DELETE.value,
        _url.value,
        headers=HEADERS,
        timeout=30,
        params={"db_id": db_id},
    )


def request_to_update_good(url: str | URL, *, db_id: int, good: dict[str, Any]) -> Response:
    """
    Put a good to the given URL

    :param url: The URL to put the good to
    :param db_id: The db_id of the good to put
    :param good: The good to put
    :return: The response
    """
    _url: URL = URL(url)
    _good: GoodCreation = GoodCreation(**good)
    return request(
        RequestMethod.PATCH.value,
        _url.value,
        headers=HEADERS,
        timeout=30,
        params={"db_id": db_id},
        json=_good.model_dump(mode="json"),
    )


def request_to_sell_good(url: str | URL, *, db_id: int, customer: dict[str, Any]) -> Response:
    """
    Sell a good from the given URL

    :param url: The URL to sell the good from
    :param db_id: The db_id of the good to sell
    :param customer: The customer to sell the good to
    :return: The response
    """
    _url: URL = URL(url)
    _customer: Customer = Customer(**customer)
    return request(
        RequestMethod.PATCH.value,
        _url.value,
        headers=HEADERS,
        timeout=30,
        params={"db_id": db_id},
        json=_customer.model_dump(mode="json"),
    )


def request_to_restock_good(url: str | URL, *, db_id: int) -> Response:
    """
    Restock a good from the given URL

    :param url: The URL to restock the good from
    :param db_id: The db_id of the good to restock
    :return: The response
    """
    _url: URL = URL(url)
    return request(
        RequestMethod.PATCH.value,
        _url.value,
        headers=HEADERS,
        timeout=30,
        params={"db_id": db_id},
    )
