#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 13:48
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   dialogs.py
# @Desc     :

from datetime import date
from os import remove
from pathlib import Path
from typing import Any

from sqlalchemy.engine import Engine
from streamlit import (
    button,
    caption,
    columns,
    date_input,
    dialog,
    empty,
    number_input,
    rerun,
    segmented_control,
    slider,
    text_area,
    text_input,
)

from backend import DECLARATION, InitSession


@dialog("Create a new data", width="medium", position="center")
def create_record(engine: Engine, table: Any) -> None:
    """
    Add a new piece of record

    :param engine: The database engine
    :param table: The table object
    :return: None
    """
    caption("**Date Information**")
    left, right = columns(2)
    with left:
        purchase_date: date = date_input(
            "Purchase Date", required=True,
            value=date.today(), disabled=False,
            width="stretch", help="Select the purchase date."
        )
    with right:
        sale_date: date = date_input(
            "Sale Date", required=True,
            value=None, disabled=True,
            width="stretch", help="Select the sale date."
        )

    caption("**Product Information**")
    product: str = text_input(
        "Product Name", required=True,
        placeholder="Enter the product name",
        width="stretch", help="Enter the product name."
    )
    category: str = segmented_control(
        "Exercise Category",
        options=["Sterling Silver", "Silver Plated", "Karat Gold", "Bone China"],
        default="Bone China", disabled=False,
        width="stretch", help="Select the exercise category."
    )
    international_price: float = number_input(
        "Product Price ($)", required=True,
        min_value=0.0, max_value=100.0, step=0.01, value=3.0,
        width="stretch", help="Select the product price."
    )
    # currency: float = slider(
    #     "Currency on Purchase Date", min_value=0.0, max_value=10.0, value=3.0, step=1.0,
    #     width="stretch", help="Select the currency on purchase date."
    # )
    # domestic_price: float = number_input(
    #     "Product Price (¥)", min_value=0.0, max_value=100.0, step=0.01, value=3.0,
    #     width="stretch", help="Select the product price."
    # )
    quantity: int = slider(
        "Product Quantity",
        min_value=1, max_value=10, step=1, value=1,
        width="stretch", help="Select the product quantity."
    )
    # pieces: int = slider(
    #     "Product Pieces", min_value=0, max_value=10, step=1, value=1,
    #     width="stretch", help="Select the product pieces."
    # )
    desc: str = text_area(
        "Product Description", required=False,
        placeholder="Enter the product description",
        width="stretch", help="Enter the product description."
    )

    if button("Submit", type="primary", width="stretch"):
        with InitSession(engine).initialise() as session:
            good = table(
                purchase_date=purchase_date,
                sale_date=sale_date,

                product=product,
                category=category,
                price=international_price,
                quantity=quantity,
                description=desc,
            )
            session.add(good)
            session.commit()
        rerun()


@dialog("Delete the database", width="small", position="center")
def delete_db(engine: Engine, db_path: Path) -> None:
    """
    Confirm whether to delete the database from the specified path

    :param engine: The database engine
    :param db_path: The database path
    :return: None
    """
    caption("**Would you like to delete the database?**")

    left, right = columns(2)
    with left:
        if button("Yes", type="secondary", width="stretch"):
            engine.dispose()

            if db_path.exists():
                remove(db_path)

            rerun()
    with right:
        if button("No", type="primary", width="stretch"):
            rerun()


@dialog("Delete all records from the table", width="small", position="center")
def delete_records(engine: Engine, table: Any) -> None:
    """
    Confirm whether to delete all records from the selected table

    :param engine: The database engine
    :param table: The table object
    :return: None
    """
    caption("**Would you like to delete all records from the selected table?**")

    left, right = columns(2)
    with left:
        if button("Yes", type="secondary", width="stretch"):
            with InitSession(engine).init() as session:
                session.query(table).delete()
                session.commit()
            rerun()
    with right:
        if button("No", type="primary", width="stretch"):
            rerun()


@dialog("Delete selected record", width="small", position="center")
def delete_selected_record(engine: Engine, table: Any, db_idx: int) -> None:
    """
    Confirm whether to delete selected data

    :param engine: The database engine
    :param table: The table object
    :param db_idx: The database index
    :return: None
    """
    caption("**Would you like to delete the selected record?**")

    left, right = columns(2)
    with left:
        if button("Yes", type="secondary", width="stretch"):
            with InitSession(engine).initialise() as session:
                record = session.query(table).filter(table.id == db_idx).first()
                if record:
                    session.delete(record)
                    session.commit()
                rerun()
    with right:
        if button("No", type="primary", width="stretch"):
            rerun()


@dialog("Delete all tables from the database", width="small", position="center")
def delete_tables(engine: Engine) -> None:
    """
    Confirm whether to delete all tables from the database

    :param engine: The database engine
    :return: None
    """
    caption("**Would you like to delete all tables from the database?**")

    left, right = columns(2)
    with left:
        if button("Yes", type="secondary", width="stretch"):
            DECLARATION.metadata.drop_all(engine)
            rerun()
    with right:
        if button("No", type="primary", width="stretch"):
            rerun()


@dialog("Update the selected record", width="medium", position="center")
def update_record(engine: Engine, table: Any, db_idx: int) -> None:
    """
    Update an existing record

    :param engine: The database engine
    :param table: The table object
    :param db_idx: The database index
    :return: None
    """
    notification = empty()

    with InitSession(engine).initialise() as session:
        record = session.query(table).filter(table.id == db_idx).first()
        print(record)

        if not record:
            notification.error("The record you are looking for does not exist.")
            return

        caption("**Date Information**")
        left, right = columns(2)
        with left:
            purchase_date: date = date_input(
                "Purchase Date", required=True,
                value=record.purchase_date, disabled=True,
                width="stretch", help="Select the purchase date."
            )
        with right:
            sale_date: date = date_input(
                "Sale Date", required=False,
                value=record.sale_date, disabled=False,
                width="stretch", help="Select the sale date."
            )

        caption("**Product Information**")
        product: str = text_input(
            "Product Name", required=True,
            placeholder="Enter the product name", value=record.product,
            width="stretch", help="Enter the product name."
        )
        category: str = segmented_control(
            "Exercise Category",
            options=["Sterling Silver", "Silver Plated", "Karat Gold", "Bone China"],
            default=record.category, disabled=False,
            width="stretch", help="Select the exercise category."
        )
        international_price: float = number_input(
            "Product Price ($)", required=True,
            min_value=0.0, max_value=100.0, step=0.01, value=record.price,
            width="stretch", help="Select the product price."
        )
        # currency: float = slider(
        #     "Currency on Purchase Date", min_value=0.0, max_value=10.0, value=3.0, step=1.0,
        #     width="stretch", help="Select the currency on purchase date."
        # )
        # domestic_price: float = number_input(
        #     "Product Price (¥)", min_value=0.0, max_value=100.0, step=0.01, value=3.0,
        #     width="stretch", help="Select the product price."
        # )
        quantity: int = slider(
            "Product Quantity",
            min_value=1, max_value=10, step=1, value=record.quantity,
            width="stretch", help="Select the product quantity."
        )
        # pieces: int = slider(
        #     "Product Pieces", min_value=0, max_value=10, step=1, value=1,
        #     width="stretch", help="Select the product pieces."
        # )
        desc: str = text_area(
            "Product Description", required=False,
            placeholder="Enter the product description", value=record.description,
            width="stretch", help="Enter the product description."
        )

        if button("Submit", type="primary", width="stretch"):
            if record:
                record.purchase_date = purchase_date
                record.sale_date = sale_date

                record.product = product
                record.category = category
                record.price = international_price
                record.quantity = quantity
                record.description = desc

                session.commit()
            rerun()
