#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 19:33
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   dependencies.py
# @Desc     :

from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from ..dbkit import (
    DBCONFIG,
    SQLITE,
    InitEngine,
)
from ..dbkit.types import ExecutionModes
from .session import InitAsyncSession

config = DBCONFIG(SQLITE, True, ExecutionModes.ASYNC)
sqlite = InitEngine(config)
factory = InitAsyncSession(sqlite.engine)


async def yield_async_session() -> AsyncIterator[AsyncSession]:
    """ Dependency for getting a session """
    async with factory.initialise() as session:
        yield session
