#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/4 00:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   config.py
# @Desc     :

from pathlib import Path
from typing import Annotated, Literal

from pydantic import Field
from pydantic.dataclasses import dataclass
from sqlalchemy.engine import URL

from .types import ExecutionMode


@dataclass
class DBCONFIG:
    mode: str | ExecutionMode | Literal["sync", "async"] = ExecutionMode.ASYNC
    echo: bool = True
    timeout: Annotated[int, Field(gt=0)] = 30
    pool_size: Annotated[int, Field(ge=0)] = 5
    max_overflow: Annotated[int, Field(ge=0)] = 10


@dataclass(kw_only=True)
class SQLiteConfig(DBCONFIG):
    path: Path
    database: str

    @property
    def driver(self) -> str:
        return "sqlite+aiosqlite" if self.mode == ExecutionMode.ASYNC else "sqlite"

    @property
    def url(self) -> str:
        return f"{self.driver}:///{self.path.resolve()}"


@dataclass(kw_only=True)
class PostgresSQLConfig(DBCONFIG):
    user: str
    password: str
    host: str
    port: int
    database: str
    ssl: str = "require"

    @property
    def driver(self) -> str:
        return "postgresql+asyncpg" if self.mode == ExecutionMode.ASYNC else "postgresql+psycopg"

    @property
    def url(self) -> str:
        return URL.create(
            drivername=self.driver,
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        ).render_as_string(hide_password=False)
