#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/17 23:15
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :

"""
***************************************************************
Frontend Package
---------------------------------------------------------------
This package provides:

+ app: Streamlit application, pages, and UI utilities.
+ net: HTTP request handling and backend API communication.

It serves as the frontend layer for user interaction,
application navigation, and communication with backend services.
***************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .api import async_configue_page, async_navigate_pages

__all__ = [
    # Async Functions
    "async_configue_page",
    "async_navigate_pages",
]
