#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/4 00:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   engines.py
# @Desc     :

from sqlalchemy import Engine, create_engine, event
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from utils.helper import Access

from .config import PostgresSQLConfig, SQLiteConfig
from .types import ExecutionMode


class InitEngine(Access):
    """
    Initialise Engine with SQLAlchemy for database connection

    - Sync: Synchronous database connection (uv add sqlalchemy)
    - Async: Asynchronous database connection (uv add sqlalchemy, greenlet)
    """

    def __init__(self, config: SQLiteConfig | PostgresSQLConfig) -> None:
        """ Configure database engine settings """
        super().__init__()
        _connect_args = self._init_args(config)

        match config.mode:
            case ExecutionMode.SYNC:
                self._engine = create_engine(
                    config.url,
                    echo=config.echo,
                    pool_size=config.pool_size,
                    max_overflow=config.max_overflow,
                    connect_args=_connect_args,
                )
            case ExecutionMode.ASYNC:
                self._engine = create_async_engine(
                    config.url,
                    echo=config.echo,
                    pool_size=config.pool_size,
                    max_overflow=config.max_overflow,
                    connect_args=_connect_args,
                )
            case _:
                raise ValueError(f"Invalid execution mode: {config.mode}")

        self._configure_sqlite()

    @staticmethod
    def _init_args(config: SQLiteConfig | PostgresSQLConfig) -> dict[str, int | str]:
        """ Initialize connection arguments based on the database configuration """
        if isinstance(config, SQLiteConfig):
            _connect_args = {"timeout": config.timeout}
        elif isinstance(config, PostgresSQLConfig):
            if config.mode == ExecutionMode.ASYNC:
                _connect_args = {"timeout": config.timeout, "ssl": config.ssl}
            else:
                _connect_args = {"connect_timeout": config.timeout, "sslmode": config.ssl}
        else:
            raise TypeError("Unsupported database configuration")
        return _connect_args

    def _configure_sqlite(self) -> None:
        """ Configure foreign keys for database """
        _engine = (
            self._engine.sync_engine
            if isinstance(self._engine, AsyncEngine)
            else self._engine
        )

        if _engine.dialect.name != "sqlite3":
            return

        @event.listens_for(_engine, "connect")
        def set_sqlite_pragma(dbapi_connection, _) -> None:
            """
            Set database pragma to enable foreign keys

            :param dbapi_connection: The database connection
            :param _:
            :return: None
            """
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()

    def dispose(self) -> None:
        """ Dispose the engine """
        if isinstance(self._engine, AsyncEngine):
            raise TypeError("Use await async_dispose() for AsyncEngine.")
        self._engine.dispose()

    async def async_dispose(self) -> None:
        """Dispose an asynchronous engine."""
        if not isinstance(self._engine, AsyncEngine):
            raise TypeError("Use dispose() for synchronous Engine.")

        await self._engine.dispose()

    @property
    def engine(self) -> Engine | AsyncEngine:
        """ Return the SQLAlchemy engine """
        return self._engine


if __name__ == "__main__":
    pass
