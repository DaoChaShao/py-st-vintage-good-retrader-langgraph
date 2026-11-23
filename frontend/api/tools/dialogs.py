#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/22 00:41
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   dialogs.py
# @Desc     :

from datetime import datetime
from time import sleep
from typing import Any

from streamlit import (
    button,
    column_config,
    columns,
    data_editor,
    datetime_input,
    dialog,
    empty,
    form,
    form_submit_button,
    number_input,
    rerun,
    spinner,
    text_input,
)

from ...net import (
    URL,
    request_to_delete_tables,
    request_to_delete_users,
    request_to_get_users,
    request_to_init_admin,
    request_to_initialise_tables,
    request_to_manage_users,
    request_to_sign_up,
    request_to_update,
)


@dialog("Delete Tables", position="center", width="small", icon=":material/delete:")
def dialog_delete_tables():
    """ Delete all tables """
    left, right = columns(2)
    if left.button("Yes", type="secondary", width="stretch"):
        request_to_delete_tables(URL.DELETE_TABLES)
        rerun()

    if right.button("No", type="primary", width="stretch"):
        rerun()


@dialog("Delete Users", position="center", width="medium", icon=":material/delete:")
def dialog_delete_users(curr_id: int):
    """ Delete all users """
    notification = empty()

    filtered_users = [
        {**user, "selected": False}
        for user in request_to_get_users(URL.GET_USERS)
        if user["id"] != curr_id
    ]
    edited_users = data_editor(
        filtered_users,
        hide_index=True, width="stretch", height="stretch",
        column_config={
            "selected": column_config.CheckboxColumn("Delete"),
        },
        disabled=["id", "username", "role", "is_active", "created_at", "updated_at"],
    )

    deleted_ids = [int(user["id"]) for user in edited_users if user["selected"]]

    if button("Delete", type="primary", width="stretch"):
        with spinner("Updating...", show_time=True, width="stretch"):
            response = request_to_delete_users(URL.DELETE_USERS, ids=deleted_ids)
            if response.ok:
                rerun()
            else:
                notification.error(
                    f"Delete failed ({response.status_code}): {response.text}",
                    icon=":material/error:"
                )


@dialog("Initialise Tables", position="center", width="small", icon=":material/add:")
def dialog_init_tables():
    """ Initialise all tables and an administrator """
    left, right = columns(2)
    if left.button("Yes", type="secondary", width="stretch"):
        request_to_initialise_tables(URL.INITIALISE_TABLES)
        sleep(1)
        request_to_init_admin(URL.INIT_ADMIN)
        rerun()

    if right.button("No", type="primary", width="stretch"):
        rerun()


@dialog("Register", position="center", width="small", icon=":material/account_circle:")
def dialog_sign_up():
    """ Dialog for user registration """
    notification = empty()

    with form("registration_form", border=True, clear_on_submit=True, width="stretch", height="stretch"):
        username: str = text_input(
            "Username", placeholder="Enter your username", required=True,
            type="default", icon=":material/person:",
            help="Enter your username here"
        )
        password: str = text_input(
            "Password", placeholder="Enter your password", required=True,
            type="password", icon=":material/vpn_key_alert:",
            help="Enter your password here"
        )
        confirmation: str = text_input(
            "Confirm Password", placeholder="Re-enter your password", required=True,
            type="password", icon=":material/vpn_key:",
            help="Re-enter your password here"
        )

        if form_submit_button("Register", type="primary", width="stretch", icon=":material/input:"):
            if password != confirmation:
                notification.warning("Passwords do not match", icon=":material/warning:")
            else:
                response = request_to_sign_up(URL.SIGN_UP, username=username, password=password)
                if response.ok:
                    rerun()
                else:
                    notification.error("Registration failed", icon=":material/error:")


@dialog("Manage User", position="center", width="medium", icon=":material/person:")
def dialog_manage_users(curr_id: int):
    """ Dialog for managing users """
    notification = empty()

    filtered_users = [
        user
        for user in request_to_get_users(URL.GET_USERS)
        if user["id"] != curr_id
    ]
    edited_users = data_editor(
        filtered_users,
        hide_index=True, width="stretch", height="stretch",
        column_config={
            "is_active": column_config.CheckboxColumn("Active Status"),
            "role": column_config.SelectboxColumn("Account Role", options=["user", "admin"]),
        },
        disabled=["id", "username", "created_at", "updated_at"],
    )

    original_users = {user["id"]: user for user in filtered_users}
    changed_users = [
        user
        for user in edited_users
        if (
                user["role"] != original_users[user["id"]]["role"]
                or user["is_active"] != original_users[user["id"]]["is_active"]
        )
    ]

    if button("Manage", type="primary", width="stretch"):
        with spinner("Updating...", show_time=True, width="stretch"):
            response = request_to_manage_users(URL.MANAGE_USERS, changed_users=changed_users)
            if response.ok:
                rerun()
            else:
                notification.error(
                    f"Update failed ({response.status_code}): {response.text}",
                    icon=":material/error:"
                )


@dialog("Update User Information", position="center", width="small", icon=":material/person:")
def dialog_update(user: Any):
    """ Dialog for updating user information """
    notification = empty()

    with form("update_user_info_form", border=True, clear_on_submit=True, width="stretch", height="stretch"):
        _id = number_input(
            "User ID", placeholder="Your user ID", required=True,
            icon=":material/id_card:", width="stretch", disabled=True,
            help="Your user ID here",
            value=user["id"],
        )
        _username = text_input(
            "Username", placeholder="Your username", required=True,
            type="default", icon=":material/person:", width="stretch", disabled=True,
            help="Your username here",
            value=user["username"],
        )
        _old_password = text_input(
            "Password", placeholder="Your password", required=False,
            type="password", icon=":material/vpn_key_alert:", width="stretch", disabled=False,
            help="Your password here", key="old_password"
        )
        _new_password = text_input(
            "Password", placeholder="Your password", required=False,
            type="password", icon=":material/vpn_key_alert:", width="stretch", disabled=False,
            help="Your password here", key="new_password"
        )
        _confirmation = text_input(
            "Confirm Password", placeholder="Re-enter your password", required=False,
            type="password", icon=":material/vpn_key:", width="stretch", disabled=False,
            help="Re-enter your password here", key="confirmation"
        )

        info_left, info_right = columns(2)
        default_role = user["role"]
        _role = info_left.segmented_control(
            "Account Role", ["User", "Admin"], required=True,
            selection_mode="single", width="stretch", disabled=True,
            help="Your account role",
            default="User" if default_role == "user" else "Admin",
        )
        _status: bool = info_right.toggle(
            "Active Status",
            width="stretch", disabled=True,
            help="Your active status",
            value=user["is_active"],
        )
        _created_at: datetime = datetime_input(
            "Registration Date", required=True,
            width="stretch", disabled=True,
            help="Your registration date here",
            value=user["created_at"],
        )
        _updated_at: datetime = datetime_input(
            "Last Updated", required=True,
            width="stretch", disabled=True,
            help="Your last updated date here",
            value=datetime.today(),
        )

        if form_submit_button("Update", type="primary", width="stretch", icon=":material/input:"):
            if _new_password != _confirmation:
                notification.warning("Passwords do not match", icon=":material/warning:")
            elif _new_password and not _old_password:
                notification.warning("Original password is required", icon=":material/warning:")
            else:
                response = request_to_update(
                    URL.UPDATE,
                    user_id=_id,
                    username=_username,
                    old_password=_old_password,
                    new_password=_new_password,
                    role=_role.lower(),
                    status=_status,
                    updated_at=_updated_at,
                )
                if response.ok:
                    rerun()
                else:
                    notification.error("Update failed", icon=":material/error:")
