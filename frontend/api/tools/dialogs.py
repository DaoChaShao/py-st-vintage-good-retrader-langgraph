#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/22 00:41
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   dialogs.py
# @Desc     :

from streamlit import (
    dialog,
    empty,
    form,
    form_submit_button,
    rerun,
    text_input,
)

from ...net import URL, request_to_post_signup


@dialog("Register", position="center", width="small", icon=":material/account_circle:")
def dialog_for_registration():
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
                response = request_to_post_signup(URL.REGISTRATION, username=username, password=password)
                if response.ok:
                    rerun()
                else:
                    notification.error("Registration failed", icon=":material/error:")
