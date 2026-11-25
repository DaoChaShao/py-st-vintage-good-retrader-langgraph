#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/25 20:33
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   domains.py
# @Desc     :

from enum import StrEnum, unique


@unique
class ProductTypes(StrEnum):
    CHINAWARE = "chinaware"
    CRYSTAL = "crystal"
    POTTERY = "pottery"
    WOOD = "wood"
