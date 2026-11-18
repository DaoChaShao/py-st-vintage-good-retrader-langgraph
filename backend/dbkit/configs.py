#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/4 00:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   configs.py
# @Desc     :

from pathlib import Path
from typing import Annotated, Literal

from pydantic import Field
from pydantic.dataclasses import dataclass

from .types import ExecutionModes


@dataclass
class DBCONFIG:
    path: Path
    echo: bool = False
    mode: str | ExecutionModes | Literal["sync", "async"] = ExecutionModes.SYNC
    timeout: Annotated[int, Field(gt=0)] = 30
    pool_size: Annotated[int, Field(ge=0)] = 10
    max_overflow: Annotated[int, Field(ge=0)] = 20

    @property
    def url(self) -> str:
        """ Return the database URL """
        _driver: str = "sqlite+aiosqlite" if self.mode == ExecutionModes.ASYNC else "sqlite"
        return f"{_driver}:///{self.path.resolve()}"
