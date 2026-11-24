#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/21 21:27
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   database.py
# @Desc     :

from fastapi import APIRouter
from sqlalchemy import inspect

from ....dbkit import BASE
from ...dependencies import sqlite
from ...schemas import CRUDResponse, TablesResponse
from ...types import ResponseStatus

router = APIRouter()


@router.delete(
    "/delete/tables",
    response_model=CRUDResponse,
)
async def delete_tables():
    """ Delete the tables in the database """
    async with sqlite.engine.begin() as connection:
        await connection.run_sync(BASE.metadata.drop_all)

    _status = ResponseStatus.SUCCESS

    return CRUDResponse(
        code=_status.code,
        message=_status.message
    )


@router.get(
    "/list/tables",
    response_model=TablesResponse,
)
async def list_tables():
    """ List the tables in the database """
    async with sqlite.engine.connect() as connection:
        _tables = await connection.run_sync(lambda conn: inspect(conn).get_table_names())

    _status = ResponseStatus.SUCCESS

    return TablesResponse(
        code=_status.code,
        message=_status.message,
        tables=_tables,
    )


@router.post(
    "/initialise/tables",
    response_model=CRUDResponse,
)
async def initialise_tables():
    """ Initialise the tables in the database """
    async with sqlite.engine.begin() as connection:
        await connection.run_sync(BASE.metadata.create_all)

    _status = ResponseStatus.SUCCESS

    return CRUDResponse(
        code=_status.code,
        message=_status.message
    )
