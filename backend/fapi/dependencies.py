#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 19:33
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   dependencies.py
# @Desc     :

from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from ..config import SQLiteConfig
from ..constants import SQLITE, YAML
from ..engines import InitEngine
from ..services import load_yaml
from ..types import DBType, ExecutionMode
from .session import InitAsyncSession

yaml = load_yaml(YAML, DBType.SQLITE)

sqlite_config = SQLiteConfig(
    path=SQLITE,
    mode=ExecutionMode.ASYNC,
    echo=True,
    database=yaml.database,
)
sqlite = InitEngine(sqlite_config)
factory = InitAsyncSession(sqlite.engine)


async def yield_async_session() -> AsyncIterator[AsyncSession]:
    """ Dependency for getting a session """
    async with factory.initialise() as session:
        yield session
