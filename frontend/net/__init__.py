#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/17 23:22
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :

"""
****************************************************************
Network Tools for Streamlit Application
----------------------------------------------------------------
A collection of HTTP client functions designed for communication
with the FastAPI backend and retrieval of API response data.
****************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .account import request_to_post_signin, request_to_post_signup
from .crud import (
    request_to_delete_tables,
    request_to_initialise_tables,
    request_to_list_tables,
)
from .goods import request_to_get_goods
from .types import URL, AcceptTypes, RequestMethods

__all__ = [
    "request_to_post_signin",
    "request_to_post_signup",

    "request_to_delete_tables",
    "request_to_list_tables",
    "request_to_initialise_tables",

    "request_to_get_goods",

    "URL",
    "AcceptTypes",
    "RequestMethods",
]
