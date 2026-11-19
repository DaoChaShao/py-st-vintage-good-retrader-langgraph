#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 23:07
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   services.py
# @Desc     :

from sqlalchemy import inspect, select
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from ..dbkit import Goods


async def async_read_records(session: AsyncSession) -> list[Goods]:
    """
    Read records from the database

    :param session: The database session
    :return: A list of goods objects
    """
    result = await session.execute(select(Goods))
    return list(result.scalars().all())


async def async_table_ready(
        engine: AsyncEngine,
        table: str,
        *,
        display: bool = False,
) -> bool:
    """
    Check if the table is ready

    :param engine: The database engine
    :param table: The table name
    :param display: Display the table names
    :return: True if the table is ready, False otherwise
    """
    async with engine.connect() as connection:
        tables = await connection.run_sync(lambda sync_conn: inspect(sync_conn).get_table_names())

    if display:
        print(tables)

    return table in tables
