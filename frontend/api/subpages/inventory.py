#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/20 00:36
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   database.py
# @Desc     :

from streamlit import (
    empty,
    session_state,
    stop,
)

from frontend.api.tools import async_db_ready
from frontend.app.tools import DBReadyStatus

NOTIFICATION = empty()

for key in ["GOODS", "ACCESS_TOKEN", "TOKEN_EXPIRES_AT"]:
    if key not in session_state:
        session_state[key] = None

if not async_db_ready(session_state.GOODS, status=DBReadyStatus.INIT, notification=NOTIFICATION):
    stop()
else:
    pass
