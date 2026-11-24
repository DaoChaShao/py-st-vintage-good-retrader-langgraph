#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/20 00:36
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   database.py
# @Desc     :
from streamlit import (
    button,
    dataframe,
    empty,
    pills,
    rerun,
    session_state,
    space,
    spinner,
)

from frontend.api.tools import (
    dialog_create_good,
    dialog_delete_good,
    dialog_restock_good,
    dialog_sell_good,
    dialog_update_good,
)
from frontend.net import (
    URL,
    request_to_get_goods,
)

NOTIFICATION = empty()

for key in ["GOODS", "ACCESS_TOKEN", "TOKEN_EXPIRES_AT", "QUERY_GOODS"]:
    if key not in session_state:
        session_state[key] = None

if session_state.GOODS is None:
    with spinner("Loading Vintage Goods Information...", show_time=True, width="stretch"):
        session_state.GOODS = request_to_get_goods(URL.GET_GOODS)
        rerun()
else:
    FUNC = empty()
    BTN, FILTER = FUNC.columns([4, 1], vertical_alignment="center")
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

    with FILTER.container(border=False, width="stretch", height="stretch", horizontal=True):
        space("stretch")
        pill: str = pills(
            "Filter", required=True,
            options=["In Stock", "Sold", "All"], width=200,
            selection_mode="single", label_visibility="collapsed",
            help="Filter the goods by stock or sold",
            default="In Stock",
        )

    display_goods = [
        good for good in session_state.GOODS
        if (
                   not session_state.QUERY_GOODS
                   or query.strip().lower() in (good["sku"] or "").lower()
           )
           and (
                   pill == "All"
                   or (good["sale_date"] is None) == (pill == "In Stock")
           )
    ]

    selection = dataframe(
        display_goods,
        hide_index=True, width="stretch", height=600,
        on_select="rerun", selection_mode="single-row",
    )
    selected_row = selection.get("selection", {}).get("rows", [])

    with BTN.container(border=False, width="stretch", height="stretch", horizontal=True):
        if button("New Good", type="primary", width=120):
            with spinner("Creating New Vintage Good...", show_time=True, width="stretch"):
                dialog_create_good()
        if selected_row:
            df_idx: int = int(selected_row[0])
            good: dict = display_goods[df_idx]
            db_idx: int = int(display_goods[df_idx]["id"])

            if button("Update", type="secondary", width=120):
                with spinner("Updating Vintage Good...", show_time=True, width="stretch"):
                    dialog_update_good(db_id=db_idx, good=good)

            if good["sale_date"] is None:
                if button("Sell", type="secondary", width=120):
                    with spinner("Selling Vintage Good...", show_time=True, width="stretch"):
                        dialog_sell_good(db_idx)
            else:
                if button("Restock", type="secondary", width=120):
                    dialog_restock_good(db_idx)

        space("stretch")

        if selected_row and button("Delete", type="secondary", width=120):
            with spinner("Deleting Vintage Good...", show_time=True, width="stretch"):
                dialog_delete_good(db_idx)
