#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 20:32
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :

"""
****************************************************************
Async Tools for Streamlit Application
----------------------------------------------------------------
A collection of utility tools designed for Streamlit page initialisation and core function execution.
****************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .dialogs import (
    dialog_delete_tables,
    dialog_delete_users,
    dialog_init_tables,
    dialog_manage_users,
    dialog_sign_up,
    dialog_update,
)
from .layout import async_configue_page, async_navigate_pages
from .services import (
    async_db_ready,
)

__all__ = [
    # Layout from Main utilisation
    "async_configue_page",
    "async_navigate_pages",

    # functions for streamlit subpages
    "dialog_delete_tables",
    "dialog_delete_users",
    "dialog_init_tables",
    "dialog_sign_up",
    "dialog_update",
    "dialog_manage_users",

    "async_db_ready",
]
