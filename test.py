#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 14:32
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   test.py
# @Desc     :

from backend import (
    SQLITE,
    Goods,
    InitEngine,
    InitSession,
    SQLiteConfig,
    count_records,
    create_db,
    drop_tables,
    table_ready,
)


def main() -> None:
    """ Main Function """
    print(SQLITE)

    config = SQLiteConfig(SQLITE, True)
    print(config)

    sqlite = InitEngine(config)
    print(sqlite)

    create_db(sqlite.engine)
    print(table_ready(sqlite.engine, Goods.__tablename__))

    with InitSession(sqlite.engine).initialise() as session:
        print(count_records(session, Goods))

    drop_tables(sqlite.engine)
    print(table_ready(sqlite.engine, Goods.__tablename__))


if __name__ == "__main__":
    main()
