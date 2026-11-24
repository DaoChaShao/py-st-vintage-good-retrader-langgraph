#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 13:13
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   dashboard.py
# @Desc     :

from streamlit import (
    data_editor,
    empty,
    expander,
    rerun,
    session_state,
    spinner,
)

from frontend.net import (
    URL,
    request_to_get_goods,
)

NOTIFICATION = empty()

for key in ["GOODS", "ACCESS_TOKEN", "TOKEN_EXPIRES_AT"]:
    if key not in session_state:
        session_state[key] = None

if session_state.GOODS is None:
    with spinner("Loading Vintage Goods Information...", show_time=True, width="stretch"):
        session_state.GOODS = request_to_get_goods(URL.GET_GOODS)
        rerun()
else:
    NOTIFICATION = empty()
    QUERY = empty()

    left, mid, right = QUERY.columns([8, 1, 1])
    query: str | None = left.text_input(
        "Search Vintage Goods", placeholder="Enter good SKU (Stock Keeping Unit)",
        type="default", icon=":material/search:", width="stretch",
        label_visibility="collapsed", max_chars=15,
        help="Enter the SKU (Stock Keeping Unit) of the good you are looking for",
        disabled=False, value=None,
        key="GET_QUERY",
    )
    mid.button(
        "Clear",
        type="secondary", width="stretch",
        on_click=lambda: session_state.update(
            GET_QUERY=None,
            QUERY_GOODS=None,
        )
    )
    if right.button("Search", type="primary", width="stretch"):
        with spinner("Searching Vintage Goods...", show_time=True, width="stretch"):
            if query:
                session_state.QUERY_GOODS = query.strip().lower() if query else None

    with expander("Vintage Goods Information", expanded=False, icon=":material/data_check:", width="stretch"):
        data_editor(session_state.GOODS, hide_index=True, disabled=True, width="stretch", height="stretch")
        NOTIFICATION.success("Records loaded successfully.", icon=":material/check_circle:")
