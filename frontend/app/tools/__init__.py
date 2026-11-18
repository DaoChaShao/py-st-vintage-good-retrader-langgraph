#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 12:37
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :

"""
****************************************************************
Tools for Streamlit Application
----------------------------------------------------------------
A collection of utility tools designed for Streamlit page initialisation and core function execution.
****************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .dialogs import (
    create_record,
    delete_db,
    delete_records,
    delete_selected_record,
    delete_tables,
    update_record,
)
from .layout import configue_page, navigate_pages
from .services import db_ready
from .types import DBReadyStatus

__all__ = [
    # Layout from Main utilisation
    "configue_page",
    "navigate_pages",

    # functions for streamlit subpages
    "create_record",
    "delete_db",
    "delete_records",
    "delete_selected_record",
    "delete_tables",
    "update_record",

    "db_ready",

    "DBReadyStatus"
]
