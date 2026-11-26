#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/26 23:05
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   services.py
# @Desc     :

from sqlalchemy import insert, select, text
from sqlalchemy.ext.asyncio import AsyncEngine

from backend import (
    DECLARATION,
    YAML,
    DBType,
    InitEngine,
    PostgresSQLConfig,
    load_yaml,
)


async def create_supabase_tables() -> None:
    """ Create Supabase Tables """
    print(YAML)
    print(load_yaml(YAML, DBType.POSTGRES))

    yaml = load_yaml(YAML, DBType.POSTGRES)
    config = PostgresSQLConfig(
        echo=yaml.echo,
        user=yaml.user,
        password=yaml.password,
        host=yaml.host,
        port=yaml.port,
        database=yaml.database,
        ssl=yaml.ssl,
    )

    postgres = InitEngine(config)
    engine = postgres.engine
    if not isinstance(engine, AsyncEngine):
        raise TypeError("Expected an AsyncEngine")

    try:
        async with engine.begin() as connection:
            await connection.run_sync(DECLARATION.metadata.create_all)
    finally:
        await postgres.async_dispose()
    print(DECLARATION.metadata.tables.keys())


async def migrate_data(
        source: AsyncEngine,
        target: AsyncEngine,
) -> None:
    async with source.connect() as src, target.begin() as dst:
        for table in DECLARATION.metadata.sorted_tables:
            result = await src.execute(select(table))
            records = [dict(row) for row in result.mappings()]

            if records:
                await dst.execute(insert(table), records)

            print(f"{table.name}: {len(records)} records migrated")

            # Synchronise PostgreSQL primary key sequence
            await dst.execute(text(
                f"""
                    SELECT setval(
                        pg_get_serial_sequence('{table.name}', 'id'),
                        COALESCE(MAX(id), 1),
                        MAX(id) IS NOT NULL
                    )
                    FROM "{table.name}"
                    """
            ))
