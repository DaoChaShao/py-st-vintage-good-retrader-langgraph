#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 13:31
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   services.py
# @Desc     :

from pathlib import Path
from typing import Any, Literal

from sqlalchemy.engine import Engine
from streamlit import rerun, sidebar

from backend import create_db, table_ready

from .types import DBReadyStatus


def db_ready(
        filepath: Path,
        *,
        engine: Engine, table: str,
        status: str | DBReadyStatus | Literal["init", "stop"] = "init",
        notification: Any
) -> bool:
    """
    Check whether the database and specified table are ready

    :param filepath: The path to the database file
    :param engine: The database engine
    :param table: The name of the table
    :param status: The status of the database
    :param notification: The notification object
    :return: True if the database is ready, otherwise False
    """

    def _init_button() -> None:
        if sidebar.button("Initialise Database", type="primary", width="stretch"):
            create_db(engine)
            rerun()

    _status = DBReadyStatus(status)

    if not filepath.exists():
        notification.error("**SQLite database** NOT found.")
        if _status == DBReadyStatus.INIT:
            _init_button()
        return False

    if not table_ready(engine, table):
        notification.warning("**SQLite database** found, but table NOT found.")
        if _status == DBReadyStatus.INIT:
            _init_button()
        return False

    return True
