#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/26 21:59
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   supabase.py
# @Desc     :

from asyncio import run

from .services import create_supabase_tables


async def main() -> None:
    """ Main Function """
    await create_supabase_tables()


if __name__ == "__main__":
    run(main())
