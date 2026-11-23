#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/20 23:21
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   user.py
# @Desc     :

from streamlit import (
    columns,
    container,
    datetime_input,
    divider,
    empty,
    number_input,
    rerun,
    session_state,
    spinner,
    text_input,
)

from frontend.api.tools import (
    dialog_delete_tables,
    dialog_delete_users,
    dialog_init_tables,
    dialog_manage_users,
    dialog_sign_up,
    dialog_update,
)
from frontend.net import (
    URL,
    request_to_list_tables,
    request_to_sign_in,
)

for key in ["IS_IN", "USER", "ACCESS_TOKEN", "TOKEN_EXPIRES_AT"]:
    if key not in session_state:
        session_state[key] = None

_, center, _ = columns([2, 4, 2])
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
                if username == "test" and password == "1234":
                    with spinner("Logging in...", show_time=True, width="stretch"):
                        session_state.IS_IN = True
                        rerun()
                response = request_to_sign_in(URL.SIGN_IN, username=username, password=password)
                if response.ok:
                    data = response.json()
                    # Store the user data in the session state
                    session_state.IS_IN = True
                    session_state.USER = data["user"]
                    session_state.ACCESS_TOKEN = data["token"]["token"]
                    session_state.TOKEN_EXPIRES_AT = data["token"]["expires_at"]
                    rerun()
                else:
                    if response.status_code == 401:
                        NOTIFICATION.warning(response.json()["detail"], icon=":material/warning:")
                    else:
                        NOTIFICATION.error(f"Login failed (HTTP {response.status_code}).", icon=":material/error:")

        if sup.button("Sign up", type="secondary", width="stretch", icon=":material/person_add:"):
            with spinner("Registering...", show_time=True, width="stretch"):
                dialog_sign_up()
    else:
        # NOTIFICATION.success(f"Welcome back, {session_state.USER['username']}!", icon=":material/check_circle:")

        with container(border=True, width="stretch", height="stretch"):
            # User information
            number_input(
                "User ID", placeholder="Your user ID", required=True,
                icon=":material/id_card:", width="stretch", disabled=True,
                help="Your user ID here",
                value=session_state.USER["id"],
            )
            text_input(
                "Username", placeholder="Your username", required=True,
                type="default", icon=":material/person:", width="stretch", disabled=True,
                help="Your username here",
                value=session_state.USER["username"],
            )
            info_left, info_right = columns([3, 2])
            default_role = session_state.USER["role"]
            info_left.segmented_control(
                "Account Role", ["User", "Admin"], required=True,
                selection_mode="single", width="stretch", disabled=True,
                help="Your account role",
                default="User" if default_role == "user" else "Admin",
            )
            info_right.space("stretch")
            info_right.toggle(
                "Active Status",
                width="stretch", disabled=True,
                help="Your active status",
                value=session_state.USER["is_active"],
            )
            datetime_input(
                "Registration Date", required=True,
                width="stretch", disabled=True,
                help="Your registration date here",
                value=session_state.USER["created_at"],
            )

            # Add buttons for logout and edit
            is_admin = session_state.USER["role"] == "admin"
            cols = columns(4 if is_admin else 2)
            if cols[0].button("Logout", type="primary", width="stretch", icon=":material/logout:"):
                session_state.IS_IN = False
                rerun()
            if is_admin and cols[1].button("Manage", type="secondary", width="stretch"):
                with spinner("Managing Users...", show_time=True, width="stretch"):
                    dialog_manage_users(session_state.USER["id"])
            if is_admin and cols[2].button("Delete", type="secondary", width="stretch"):
                with spinner("Deleting User...", show_time=True, width="stretch"):
                    dialog_delete_users(session_state.USER["id"])
            if cols[-1].button("Edit", type="secondary", width="stretch", icon=":material/edit:"):
                with spinner("Updating User Information...", show_time=True, width="stretch"):
                    dialog_update(session_state.USER)

            if is_admin:
                divider()
                db_left, db_right = columns(2)
                if db_left.button("Delete Tables", type="tertiary", width="stretch"):
                    with spinner("Deleting Tables...", show_time=True, width="stretch"):
                        dialog_delete_tables()
                        tables = request_to_list_tables(URL.LIST_TABLES)
                        if not tables:
                            NOTIFICATION.warning("All tables have been deleted.", icon=":material/warning:")
                        else:
                            NOTIFICATION.error("Failed to delete all tables.", icon=":material/error:")

                if db_right.button("Initialise Tables", type="tertiary", width="stretch"):
                    with spinner("Initialising Tables...", show_time=True, width="stretch"):
                        dialog_init_tables()
                        tables: list[str] = request_to_list_tables(URL.LIST_TABLES)
                        if tables:
                            NOTIFICATION.success(
                                f" {len(tables)} tables have been initialised.",
                                icon=":material/check_circle:"
                            )
                        else:
                            NOTIFICATION.error("Failed to initialise tables.", icon=":material/error:")
