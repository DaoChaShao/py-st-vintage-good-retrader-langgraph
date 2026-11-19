#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 12:38
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   layout.py
# @Desc     :

from pathlib import Path

from streamlit import Page, navigation, set_page_config

BASE_DIR: Path = Path(__file__).resolve().parents[1]


def async_configue_page() -> None:
    """ Set the window
    :return: None
    """
    set_page_config(
        page_title="Vintage Goods",
        page_icon=":material/globe:",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def async_navigate_pages() -> None:
    """ Set the subpages on the sidebar (https://fonts.google.com/icons)
    :return: None
    """
    pages: dict = {
        "page": [
            Path(BASE_DIR / "subpages" / "home.py").resolve(),
            Path(BASE_DIR / "subpages" / "initialisation.py").resolve(),
            # "app/subpages/preparation.py",
            # "app/subpages/ef.py",
            # "app/subpages/acwr.py",
            # "app/subpages/hrr.py"
        ],
        "title": [
            "Home",
            "Data Initialisation",
            # "Data Preparation",
            # "Efficiency Factor",
            # "Acute:Chronic Workload Ratio",
            # "Heart Rate Recovery",
        ],
        "icon": [
            ":material/home:",
            ":material/database:",
            # ":material/dashboard:",
            # ":material/looks_one:",
            # ":material/looks_two:",
            # ":material/looks_3:"
        ],
    }

    structure: list = [
        Page(page=pages["page"][0], title=pages["title"][0], icon=pages["icon"][0]),
        Page(page=pages["page"][1], title=pages["title"][1], icon=pages["icon"][1]),
    ]
    pg = navigation(structure, position="top", expanded=True)
    pg.run()


if __name__ == "__main__":
    print(BASE_DIR)
