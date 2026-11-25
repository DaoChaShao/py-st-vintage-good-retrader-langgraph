#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/25 18:23
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   services.py
# @Desc     :

from pathlib import Path
from random import choice
from typing import Literal

from yaml import safe_load

from .constants import YAML
from .schemas import PostgresSQL, SQLite
from .types import DBType


def load_yaml(
        filepath: Path,
        db_type: str | DBType | Literal["sqlite", "postgres"] = DBType.SQLITE,
        *,
        display: bool = False
) -> SQLite | PostgresSQL:
    """
    Load YAML File

    :param filepath: The path to the YAML file.
    :param db_type: The database type.
    :param display: Whether to display the YAML content.
    :return: The YAML content as a dictionary.
    """
    with filepath.open("r", encoding="utf-8") as file:
        _yaml = safe_load(file)

    match db_type:
        case DBType.SQLITE:
            _configration = SQLite(**_yaml[DBType.SQLITE.value])
        case DBType.POSTGRES:
            _configration = PostgresSQL(**_yaml[DBType.POSTGRES.value])
        case _:
            raise ValueError(f"Invalid database type: {db_type}")
    if display:
        print(_configration)
    return _configration


if __name__ == "__main__":
    load_yaml(YAML, db_type=choice([DBType.SQLITE, DBType.POSTGRES]), display=True)
