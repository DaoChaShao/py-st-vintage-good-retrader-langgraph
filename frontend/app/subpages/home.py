#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 13:12
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :

from streamlit import caption, empty, expander, title

empty_message = empty()
empty_message.info("Please check the details at the different pages of core functions.")

title("Runner Pro")
with expander("**INTRODUCTION (Chinese)**", expanded=False):
    caption("-")

with expander("**INTRODUCTION (English)**", expanded=True):
    caption("-")
