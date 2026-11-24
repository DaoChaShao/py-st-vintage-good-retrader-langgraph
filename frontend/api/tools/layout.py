#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 12:38
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   layout.py
# @Desc     :

from pathlib import Path

from streamlit import (
    Page,
    logo,
    navigation,
    session_state,
    set_page_config,
)

from backend.dbkit import UserRoles

LOGO_DIR: Path = Path(__file__).resolve().parents[3]
PAGE_DIR: Path = Path(__file__).resolve().parents[1]


def async_configue_page() -> None:
    """ Set the window (https://favicon.io/) """
    set_page_config(
        page_title="Vintage Goods ReTrader",
        page_icon=":material/globe:",
        layout="wide",
        initial_sidebar_state="auto",
    )

    logo(
        Path(LOGO_DIR / "static" / "favicon.ico"),
        size="medium",
    )


def async_navigate_pages() -> None:
    """ Set the subpages on the sidebar (https://fonts.google.com/icons) """
    for key in ["IS_IN"]:
        if key not in session_state:
            session_state[key] = False

    for key in ["IS_IN", "USER"]:
        if key not in session_state:
            session_state[key] = None

    pages: dict = {
        "page": [
            Path(PAGE_DIR / "subpages" / "home.py").resolve(),
            Path(PAGE_DIR / "subpages" / "account.py").resolve(),
            Path(PAGE_DIR / "subpages" / "dashboard.py").resolve(),
            Path(PAGE_DIR / "subpages" / "inventory.py").resolve(),
        ],
        "title": [
            "Home",
            "Account",
            "Dashboard",
            "Inventory",
        ],
        "icon": [
            ":material/home:",
            ":material/account_circle:",
            ":material/bar_chart_4_bars:",
            ":material/shopping_bag:",
        ],
    }

    structure: list = [
        Page(page=pages["page"][0], title=pages["title"][0], icon=pages["icon"][0]),
        Page(page=pages["page"][1], title=pages["title"][1], icon=pages["icon"][1]),
    ]

    if session_state.IS_IN:
        structure.append(
            Page(page=pages["page"][2], title=pages["title"][2], icon=pages["icon"][2])
        )

        if session_state.USER["role"] == UserRoles.ADMIN:
            structure.append(
                Page(page=pages["page"][3], title=pages["title"][3], icon=pages["icon"][3])
            )

    pg = navigation(structure, position="top", expanded=True)
    pg.run()


if __name__ == "__main__":
    print(PAGE_DIR)
