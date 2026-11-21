#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/7 16:00
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   services.py
# @Desc     :

from base64 import b64encode
from hashlib import pbkdf2_hmac, scrypt
from os import remove
from pathlib import Path
from secrets import token_bytes
from typing import Any, Literal

from bcrypt import gensalt, hashpw
from pandas import DataFrame, read_sql
from pwdlib import PasswordHash
from sqlalchemy import inspect
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from .base import DECLARATION
from .types import HashAlgorithms


def count_records(session: Session, table: Any) -> int:
    """
     Count the number of records in a database table.

    :param session: The database session
    :param table: The table name
    :return: The number of the table in the database
    """
    return session.query(func.count(table.id)).scalar()


def create_db(engine: Engine) -> None:
    """
    Create a database

    :param engine: The database engine
    :return: None
    """
    DECLARATION.metadata.create_all(engine.engine)


def delete_table_records(session: Session, table: Any) -> None:
    """
    Delete the data in the table

    :param session: The database session
    :param table: The table object
    :return: None
    """
    session.query(table).delete()
    session.commit()


def drop_tables(engine: Engine) -> None:
    """
    Drop all database tables

    :param engine: The database engine
    :return: None
    """
    DECLARATION.metadata.drop_all(engine)


def eliminate_db(engine: Engine, db_path: Path, *, display: bool = False) -> None:
    """
    Eliminate a database

    :param engine: The database engine
    :param db_path: The database path
    :param display: Display the message
    :return: None
    """
    engine.dispose()

    if db_path.exists():
        remove(db_path)
        if display:
            print(f"Database '{db_path.name}' eliminated successfully.")


def hash_password(
        password: str,
        *,
        algorithm: str | HashAlgorithms | Literal["bcrypt", "pbkdf2", "scrypt", "argon2"] = "argon2",
        display: bool = False
) -> str:
    """Hash a password using the selected algorithm."""
    _algorithm: HashAlgorithms = HashAlgorithms(algorithm)
    match _algorithm:
        case _algorithm.BCRYPT:
            _hashed = hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")
        case _algorithm.PBKDF2:
            _salt = token_bytes(16)
            _iterations: int = 600_000
            _digest = pbkdf2_hmac("sha256", password.encode("utf-8"), _salt, _iterations)
            _hashed = f"pbkdf2_sha256${_iterations}${b64encode(_salt).decode()}${b64encode(_digest).decode()}"
        case _algorithm.SCRYPT:
            _salt = token_bytes(16)
            _n, _r, _p = 2 ** 14, 8, 1
            _digest = scrypt(password.encode("utf-8"), salt=_salt, n=_n, r=_r, p=_p)
            _hashed = f"scrypt${_n}${_r}${_p}${b64encode(_salt).decode()}${b64encode(_digest).decode()}"
        case _algorithm.ARGON2:
            _hashed = PasswordHash.recommended().hash(password)
        case _:
            raise ValueError(f"Unsupported algorithm: {algorithm}")

    if display:
        print(f"Hashed password: {_hashed}")

    return _hashed


def read_records(session: Session, table: Any) -> DataFrame:
    """
    Get the data from the table

    :param session: The database session
    :param table: The table object
    :return: The data from the table
    """
    statement = session.query(table).statement
    return read_sql(statement, session.bind)


def table_ready(engine: Engine, table: str, *, display: bool = False) -> bool:
    """
    Check if the table exists in the database

    :param engine: The database engine
    :param table: The table name
    :param display: Display the table names in the database
    :return: True if the table exists, otherwise False
    """
    inspector = inspect(engine)
    if display:
        print(inspector.get_table_names())
    return table in inspector.get_table_names()
