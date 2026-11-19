#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 13:13
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   dashboard.py
# @Desc     :

from streamlit import (
    button,
    columns,
    container,
    data_editor,
    empty,
    rerun,
    session_state,
    space,
    stop,
)

from frontend.api.tools import async_db_ready
from frontend.app.tools import DBReadyStatus

NOTIFICATION = empty()

for key in ["GOODS"]:
    if key not in session_state:
        session_state[key] = None

if not async_db_ready(session_state.GOODS, status=DBReadyStatus.INIT, notification=NOTIFICATION):
    stop()
else:
    with container(horizontal=True, width="stretch", height="stretch"):
        if button("Clear Records", type="secondary", width="content"):
            session_state.GOODS = None
            rerun()
        space("stretch")

    left, right = columns([9, 1])
    left.space("stretch")
    query: str = left.text_input(
        "Search for a record", placeholder="Enter a search term",
        type="search", label_visibility="collapsed", width="stretch",
        help="Enter a search term to filter the records.",
        icon=":material/search:"
    )
    right.space("stretch")
    if right.button("Search", type="primary", width="stretch"):
        pass

    data_editor(
        session_state.GOODS,
        hide_index=True, disabled=True,
        width="stretch", height="stretch"
    )
    NOTIFICATION.info("Records loaded successfully.")
