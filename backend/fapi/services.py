#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 23:07
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   services.py
# @Desc     :

from datetime import UTC, datetime, timedelta
from typing import Literal, Self

from access_modifiers import protectedmethod
from jwt import encode
from sqlalchemy import inspect, select
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from utils import Access

from ..dbkit import Goods


class JWTAccessTokenEncoder(Access):
    """ JWT Access Token Encoder """

    def __init__(
            self,
            secret_key: str = "9e4f1a7c8b2d6e0f3a5c9d1b7e8f2046c3a9d5e1f8b2c7a0d4e6f9b3c5a81270",
            algorithm: str | Literal["HS256"] = "HS256",
    ) -> None:
        """
        Initialize the JWT Access Token Encoder

        :param secret_key: The secret key for the token
        :param algorithm: The algorithm for the token
        :return: None
        """
        super().__init__()
        self._secret_key: str = secret_key
        self._algorithm: str = algorithm

    @protectedmethod
    def _init_expiration(self, expires_in: int = 3600) -> datetime:
        """
        Initialize the expiration time for the token

        :param expires_in: The expiration time in seconds
        :return: The expiration time
        """
        return datetime.now(UTC) + timedelta(seconds=expires_in)

    def create(self, user_id: int, *, expires_in: int = 3600) -> tuple[str, int]:
        """
        Create a JWT access token

        :param user_id: The user ID
        :param expires_in: The expiration time in seconds
        :return: The JWT access token
        """
        _expire: datetime = self._init_expiration(expires_in)
        _payload: dict[str, str | datetime] = {
            "sub": str(user_id),
            "exp": _expire,
        }
        return encode(_payload, self._secret_key, algorithm=self._algorithm), int(_expire.timestamp())

    def __enter__(self) -> Self:
        """ Enter the context manager """
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
        Exit the context manager

        :param exc_type: The type of exception that occurred
        :param exc_value: The value of the exception that occurred
        :param traceback: The traceback of the exception that occurred
        :return: True if the exception was handled, False otherwise
        """
        pass


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
