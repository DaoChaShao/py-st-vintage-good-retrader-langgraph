#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/17 21:37
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   main.py
# @Desc     :

from frontend import configue_page, navigate_pages


def main() -> None:
    """ streamlit run main.py """
    configue_page()
    navigate_pages()


if __name__ == "__main__":
    main()
