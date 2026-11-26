#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/3 23:56
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :

"""
****************************************************************
Database Core - Database Management Toolkit
----------------------------------------------------------------
This package provides a collection of reusable utilities, classes,
and components for database configuration, connection management,
session handling, transaction control, and data access.

Designed to provide a modular, extensible, and consistent interface
for database operations across different database systems.
****************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .repository import (
    count_records,
    create_db,
    delete_table_records,
    drop_tables,
    eliminate_db,
    hash_password,
    read_records,
    table_ready,
)
from .session import InitSession

__all__ = [
    "count_records",
    "create_db",
    "delete_table_records",
    "drop_tables",
    "eliminate_db",
    "hash_password",
    "read_records",
    "table_ready",

    "InitSession",
]
