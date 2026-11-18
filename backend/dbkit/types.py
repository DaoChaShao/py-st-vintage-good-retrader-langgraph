#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 22:12
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   types.py
# @Desc     :

from enum import StrEnum, unique


@unique
class ExecutionModes(StrEnum):
    """ Execution Modes """
    SYNC = "sync"
    ASYNC = "async"
