#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/20 23:21
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   account.py
# @Desc     :

from streamlit import (
    columns,
    container,
    divider,
    empty,
    rerun,
    session_state,
    spinner,
    text_input,
)

from frontend.api.tools import dialog_for_registration
from frontend.net import (
    URL,
    request_to_delete_tables,
    request_to_initialise_tables,
    request_to_list_tables,
    request_to_post_signin,
)

for key in ["IS_IN"]:
    if key not in session_state:
        session_state[key] = None

_, center, _ = columns(3)
with center:
    NOTIFICATION = empty()

    if not session_state.IS_IN:
        NOTIFICATION.info("Please log in to continue.", icon=":material/info:")

        username: str = text_input(
            "Username", placeholder="Enter your username", required=True,
            type="default", icon=":material/person:",
            help="Enter your username here"
        )
        password: str = text_input(
            "Password", placeholder="Enter your password", required=True,
            type="password", icon=":material/lock:",
            help="Enter your password here"
        )
        sin, sup = columns(2)
        if sin.button("Sign in", type="primary", width="stretch", icon=":material/login:"):
            if not username:
                NOTIFICATION.warning("Username cannot be empty.", icon=":material/warning:")
            elif not password:
                NOTIFICATION.warning("Password cannot be empty.", icon=":material/warning:")
            else:
                if username == "admin" and password == "12345":
                    with spinner("Logging in...", show_time=True, width="stretch"):
                        session_state.IS_IN = True
                        rerun()
                request_to_post_signin(URL.SIGNIN, username=username, password=password)

        if sup.button("Sign up", type="secondary", width="stretch", icon=":material/person_add:"):
            with spinner("Registering...", show_time=True, width="stretch"):
                dialog_for_registration()
    else:
        NOTIFICATION.success("Welcome back, !", icon=":material/check_circle:")

        with container(border=True, width="stretch", height="stretch"):
            #

            # Add buttons for logout and edit
            mid_left, mid_right = columns(2)
            if mid_left.button("Logout", type="primary", width="stretch", icon=":material/logout:"):
                session_state.IS_IN = False
                rerun()

            if mid_right.button("Edit", type="secondary", width="stretch", icon=":material/edit:"):
                pass

            divider()
            db_left, db_right = columns(2)
            if db_left.button("Delete Tables", type="tertiary", width="stretch"):
                with spinner("Deleting Tables...", show_time=True, width="stretch"):
                    request_to_delete_tables(URL.DELETE_TABLES)
                    tables: list[str] = request_to_list_tables(URL.LIST_TABLES)
                    if not tables:
                        NOTIFICATION.warning(
                            "All tables have been deleted.",
                            icon=":material/warning:"
                        )
                    else:
                        NOTIFICATION.error("Failed to delete all tables.", icon=":material/error:")

            if db_right.button("Initialise Tables", type="tertiary", width="stretch"):
                with spinner("Initialising Tables...", show_time=True, width="stretch"):
                    request_to_initialise_tables(URL.INITIALISE_TABLES)
                    tables: list[str] = request_to_list_tables(URL.LIST_TABLES)
                    if tables:
                        NOTIFICATION.success(
                            f" {len(tables)} tables have been initialised.",
                            icon=":material/check_circle:"
                        )
                    else:
                        NOTIFICATION.error("Failed to initialise tables.", icon=":material/error:")
