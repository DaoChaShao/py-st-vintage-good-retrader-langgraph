#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 23:12
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   session.py
# @Desc     :

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from utils.helper import Access


class InitAsyncSession(Access):
    """ Initialise Session """

    def __init__(self, engine: AsyncEngine) -> None:
        """ Initialise Session """
        super().__init__()
        self._session = async_sessionmaker(
            bind=engine,
            class_=AsyncSession,
            autoflush=False,
            expire_on_commit=False,
        )

    def initialise(self) -> AsyncSession:
        """ Initialise Session """
        return self._session()
