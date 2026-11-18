#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 23:07
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   repositories.py
# @Desc     :

from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import AsyncEngine


async def async_table_ready(
        engine: AsyncEngine,
        table: str,
        *,
        display: bool = False,
) -> bool:
    async with engine.connect() as connection:
        tables = await connection.run_sync(lambda sync_conn: inspect(sync_conn).get_table_names())

    if display:
        print(tables)

    return table in tables
