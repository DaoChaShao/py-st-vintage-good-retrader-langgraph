#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 23:28
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   repository.py
# @Desc     :

from typing import Any, Literal

from streamlit import (
    button,
    container,
    rerun,
    session_state,
    space,
    spinner,
)

from frontend.net import URL, DBReadyStatus, request_to_get_goods


def async_db_ready(
        state: Any,
        *,
        status: str | DBReadyStatus | Literal["init", "stop"] = "init",
        notification: Any
) -> bool:
    """
    Check whether the database and specified table are ready

    :param state: The state of the database, typically a list of records
    :param status: The status of the database
    :param notification: The notification object
    :return: True if the database is ready, otherwise False
    """

    def _init_button() -> None:
        with container(horizontal=True, width="stretch", height="stretch"):
            if button("Load Records", type="primary", width="content"):
                with spinner("Requesting Records...", show_time=True, width="stretch"):
                    session_state.GOODS = request_to_get_goods(URL.GET_GOODS)
                    rerun()
            space("stretch")

    _status = DBReadyStatus(status)

    if state is None:
        notification.error("Records not loaded. Please load them first.", icon=":material/error:")
        if _status == DBReadyStatus.INIT:
            _init_button()
        return False

    if len(state) == 0:
        notification.warning("No records found in the database.", icon=":material/warning:")
        if _status == DBReadyStatus.INIT:
            _init_button()
        return False

    return True
