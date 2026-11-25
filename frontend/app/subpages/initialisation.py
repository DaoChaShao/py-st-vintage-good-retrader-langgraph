#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 13:13
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   dashboard.py
# @Desc     :

from pandas import DataFrame
from streamlit import (
    dataframe,
    empty,
    session_state,
    sidebar,
    stop,
    text_input,
)

from backend import (
    SQLITE,
    Goods,
    InitEngine,
    InitSession,
    SQLiteConfig,
    count_records,
    read_records,
)
from frontend.app.tools import (
    DBReadyStatus,
    create_record,
    db_ready,
    delete_db,
    delete_records,
    delete_selected_record,
    delete_tables,
    update_record,
)

NOTIFICATION = empty()

config = SQLiteConfig(SQLITE, True)
sqlite = InitEngine(config)

for key in []:
    if key not in session_state:
        session_state[key] = None

if not db_ready(
        SQLITE,
        engine=sqlite.engine, table=Goods.__tablename__, status=DBReadyStatus.INIT, notification=NOTIFICATION
):
    stop()

with InitSession(sqlite.engine).initialise() as session:
    count = count_records(session, Goods)

    if count == 0:
        NOTIFICATION.info("SQLite database found, but no exercises recorded yet.")
    else:
        NOTIFICATION.success(f"QLite database found. Total exercises: {count}")

        query: str = text_input(
            "Enter a query to filter the data (optional):", label_visibility="collapsed",
            placeholder="Enter a query to filter the data (optional):",
            icon=":material/search:", width="stretch"
        )

        goods: DataFrame = read_records(session, Goods)
        selection = dataframe(
            goods,
            hide_index=True, width="stretch", height=600,
            selection_mode="single-row",
            on_select="rerun",
        )

        selected_row = selection.get("selection", {}).get("rows", [])
        if len(selected_row) > 0:
            # print(selected_row)
            df_idx = selected_row[0]
            db_idx = int(goods.iloc[df_idx]["id"])
            # print(f"Dataframe index: {df_idx}, Database index: {db_idx}, Database index type: {type(db_idx)}")

            if sidebar.button("Update Selected Data", type="secondary", width="stretch"):
                update_record(sqlite.engine, Goods, db_idx)

            if sidebar.button("Delete This Data", type="tertiary", width="stretch"):
                delete_selected_record(sqlite.engine, Goods, db_idx)

if sidebar.button("New Record", type="primary", width="stretch"):
    create_record(sqlite.engine, Goods)

if sidebar.button("Delete Records", type="secondary", width="stretch"):
    delete_records(sqlite.engine, Goods)

if sidebar.button("Drop Tables", type="secondary", width="stretch"):
    delete_tables(sqlite.engine)

sidebar.divider()
if sidebar.button("Eliminate Database", type="tertiary", width="stretch"):
    delete_db(sqlite.engine, SQLITE)
