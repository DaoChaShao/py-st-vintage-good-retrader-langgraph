#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/4 00:02
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   base.py
# @Desc     :

from datetime import date, datetime, time
from decimal import Decimal
from typing import Annotated

from sqlalchemy import Date, DateTime, Float, Integer, Numeric, String, Text, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

DECLARATION = declarative_base()


class GENERAL:
    """ General column definitions """
    PK = Annotated[int, mapped_column(Integer, nullable=False, primary_key=True)]
    CT = Annotated[datetime, mapped_column(DateTime, nullable=False, server_default=func.now())]
    UT = Annotated[datetime, mapped_column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())]
    INT = Annotated[int, mapped_column(Integer, nullable=True)]
    FLT = Annotated[float, mapped_column(Float, nullable=True)]
    DEC = Annotated[Decimal, mapped_column(Numeric(12, 2), nullable=True)]
    STR = Annotated[str, mapped_column(String(100), nullable=True)]
    TXT = Annotated[str, mapped_column(Text, nullable=True)]
    DT = Annotated[date, mapped_column(Date, nullable=True)]
    TM = Annotated[time, mapped_column(Time, nullable=True)]


class BASE(DECLARATION):
    """ Base class for all tables """
    __abstract__ = True

    # Main Keys
    id: Mapped[GENERAL.PK]
    # Timestamps
    created_at: Mapped[GENERAL.CT]
    updated_at: Mapped[GENERAL.UT]

    def __repr__(self):
        return (
            f"id={self.id}, "
            f"created_at={self.created_at}, "
            f"updated_at={self.updated_at}, "
        )
