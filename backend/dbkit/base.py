#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/4 00:02
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   base.py
# @Desc     :

from datetime import datetime
from decimal import Decimal
from typing import Annotated

from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

DECLARATION = declarative_base()


class GENERAL:
    PK = Annotated[int, mapped_column(Integer, nullable=False, primary_key=True)]
    CT = Annotated[datetime, mapped_column(DateTime, nullable=False, server_default=func.now())]
    UT = Annotated[datetime, mapped_column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())]
    FLT = Annotated[float, mapped_column(Float, nullable=True)]
    INT = Annotated[int, mapped_column(Integer, nullable=True)]
    DEC = Annotated[Decimal, mapped_column(Float, nullable=True)]
    STR = Annotated[str, mapped_column(String(100), nullable=True)]
    TXT = Annotated[str, mapped_column(Text, nullable=True)]
