#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/17 23:11
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   __init__.py.py
# @Desc     :

"""
***************************************************************
Backend Package
---------------------------------------------------------------
This package provides:

+ dbkit: Database configuration, connection management,
  session handling, and data access utilities.
+ fastapi: RESTful API endpoints, request validation,
  business logic and backend service management.

It serves as the backend layer for database operations,
business logic processing, and communication with frontend
applications through HTTP APIs.
***************************************************************
"""

__author__ = "Shawn Yu"
__version__ = "0.1.0"

from .dbkit import (
    DBCONFIG,
    DECLARATION,
    GENERAL,
    SQLITE,
    Goods,
    InitEngine,
    InitSession,
    count_records,
    create_db,
    delete_table_data,
    drop_tables,
    eliminate_db,
    read_data,
    table_ready,
)

__all__ = [
    "DBCONFIG",
    "DECLARATION",
    "GENERAL",
    "Goods",
    "SQLITE",
    "InitEngine",
    "InitSession",
    "count_records",
    "create_db",
    "delete_table_data",
    "drop_tables",
    "eliminate_db",
    "read_data",
    "table_ready",
]
