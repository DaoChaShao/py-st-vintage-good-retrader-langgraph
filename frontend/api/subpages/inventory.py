#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/20 00:36
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   database.py
# @Desc     :

from streamlit import (
    button,
    columns,
    container,
    dataframe,
    empty,
    rerun,
    session_state,
    space,
    spinner,
)

from frontend.api.tools import (
    dialog_create_good,
    dialog_delete_good,
    dialog_update_good,
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
    if button("Load Vintage Goods Information", type="primary", width="stretch"):
        with spinner("Loading Vintage Goods Information...", show_time=True, width="stretch"):
            session_state.GOODS = request_to_get_goods(URL.GET_GOODS)
            rerun()
else:
    spades, hearts, clubs, diamonds, spaces = columns([1, 1, 1, 1, 6])

    left, mid, right = columns([8, 1, 1])
    query: str = left.text_input(
        "Search Vintage Goods", placeholder="Enter good SKU (Stock Keeping Unit)",
        type="default", icon=":material/search:", width="stretch",
        label_visibility="collapsed", max_chars=15,
        help="Enter the SKU (Stock Keeping Unit) of the good you are looking for"
    )
    if mid.button("Clear", type="secondary", width="stretch"):
        pass
    if right.button("Search", type="primary", width="stretch"):
        pass

    with container(width="stretch", height="stretch", horizontal=True):
        space("stretch")
        if spades.button("New Good", type="primary", width="stretch"):
            with spinner("Creating New Vintage Good...", show_time=True, width="stretch"):
                dialog_create_good()

    selection = dataframe(
        session_state.GOODS,
        hide_index=True, width="stretch", height="stretch",
        on_select="rerun", selection_mode="single-row",
    )
    selected_row = selection.get("selection", {}).get("rows", [])
    if selected_row:
        df_idx: int = int(selected_row[0])
        db_idx: int = int(session_state.GOODS[df_idx]["id"])
        good: dict = session_state.GOODS[df_idx]

        if hearts.button("Update", type="secondary", width="stretch"):
            with spinner("Updating Vintage Good...", show_time=True, width="stretch"):
                dialog_update_good(db_id=db_idx, good=good)
        if clubs.button("Delete", type="tertiary", width="stretch"):
            with spinner("Deleting Vintage Good...", show_time=True, width="stretch"):
                dialog_delete_good(db_idx)
