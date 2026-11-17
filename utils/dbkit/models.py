#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/5 22:17
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   models.py
# @Desc     :

from datetime import datetime
from typing import Annotated

from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func


class GENERAL:
    PK = Annotated[int, mapped_column(Integer, nullable=False, primary_key=True)]
    CT = Annotated[datetime, mapped_column(DateTime, nullable=False, server_default=func.now())]
    UT = Annotated[datetime, mapped_column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())]
    STR = Annotated[str, mapped_column(String(100), nullable=True)]
    NUM = Annotated[float, mapped_column(Float, nullable=True)]
    TXT = Annotated[str, mapped_column(Text, nullable=True)]
