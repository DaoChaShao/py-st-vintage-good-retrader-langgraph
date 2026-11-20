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
    empty,
    form,
    rerun,
    session_state,
    spinner,
    text_input,
)

for key in ["IS_IN"]:
    if key not in session_state:
        session_state[key] = None

_, center, _ = columns(3)
with center:
    NOTIFICATION = empty()

    if not session_state.IS_IN:
        NOTIFICATION.info("Please log in to continue.", icon=":material/info:")

        with form("sign_form", True, border=True, width="stretch", height="stretch"):
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
            if sin.form_submit_button("Sign in", type="primary", width="stretch", icon=":material/login:"):
                if username == "admin" and password == "12345":
                    with spinner("Logging in...", show_time=True, width="stretch"):
                        session_state.IS_IN = True
                        rerun()
                else:
                    NOTIFICATION.error("Invalid username or password.", icon=":material/error:")

            if sup.form_submit_button("Sign up", type="secondary", width="stretch", icon=":material/person_add:"):
                pass
    else:
        NOTIFICATION.success("Welcome back, !", icon=":material/check_circle:")

        with container(border=True, width="stretch", height="stretch"):

            left, right = columns(2)
            if left.button("Logout", type="primary", width="stretch", icon=":material/logout:"):
                session_state.IS_IN = False
                rerun()

            if right.button("Edit", type="secondary", width="stretch", icon=":material/edit:"):
                pass
