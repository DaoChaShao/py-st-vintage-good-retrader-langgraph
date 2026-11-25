#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/17 22:22
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   constants.py
# @Desc     :

from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parents[1]
SQLITE: Path = BASE_DIR / "data/sqlite3.db"
YAML: Path = BASE_DIR / "data/config.yaml"

if __name__ == "__main__":
    print(SQLITE.exists(), SQLITE)
    print(YAML.exists(), YAML)
