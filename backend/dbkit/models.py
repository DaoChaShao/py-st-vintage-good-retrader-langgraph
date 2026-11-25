#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/5 22:17
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   models.py
# @Desc     :

from sqlalchemy.orm import Mapped, mapped_column

from .base import BASE, GENERAL
from .types import UserRoles


class User(BASE):
    """ User Model """

    __tablename__ = "users"
    __table_args__ = {"comment": "Users Table"}

    username: Mapped[GENERAL.STR]
    password: Mapped[GENERAL.HAS]
    is_active: Mapped[GENERAL.BOL] = mapped_column(default=True, nullable=False)
    role: Mapped[GENERAL.STR] = mapped_column(default=UserRoles.USER.value, nullable=False)

    def __repr__(self) -> str:
        """ Return the string representation of the User class """
        return (
            f"<User("
            f"{super().__repr__()}"
            f"username={self.username}, "
            f"is_active={self.is_active}, "
            f"role={self.role})>"
        )


class Goods(BASE):
    """ Goods Model """

    __tablename__ = "goods"
    __table_args__ = {"comment": "Goods Table"}

    # Dates
    purchase_date: Mapped[GENERAL.DT]
    sale_date: Mapped[GENERAL.DT]

    # Product Information
    sku: Mapped[GENERAL.STR]  # Stock Keeping Unit (Item Code)
    city: Mapped[GENERAL.STR]
    store: Mapped[GENERAL.STR]
    product: Mapped[GENERAL.STR]
    production_year_start: Mapped[GENERAL.INT]
    production_year_end: Mapped[GENERAL.INT]
    brand: Mapped[GENERAL.STR]
    series: Mapped[GENERAL.STR]
    generation: Mapped[GENERAL.INT]
    category: Mapped[GENERAL.STR]

    # Quantity
    set: Mapped[GENERAL.INT]
    piece: Mapped[GENERAL.INT]

    # Financial Information for store
    purchase_price: Mapped[GENERAL.DEC]
    extra_fee: Mapped[GENERAL.DEC]
    exchange_rate: Mapped[GENERAL.DEC]
    expected_profit: Mapped[GENERAL.DEC]
    # Financial Information for customer
    customer: Mapped[GENERAL.STR]
    gender: Mapped[GENERAL.STR]
    location: Mapped[GENERAL.STR]
    shipping_fee: Mapped[GENERAL.DEC]
    sale_price: Mapped[GENERAL.DEC]

    # Description
    description: Mapped[GENERAL.TXT]

    def __repr__(self) -> str:
        """ Return the string representation of the Goods class """
        return (
            f"<Goods("
            f"{super().__repr__()}"
            f"purchase_date={self.purchase_date}, "
            f"sale_date={self.sale_date}, "
            f"city={self.city}, "
            f"store={self.store}, "
            f"sku={self.sku}, "
            f"product={self.product}, "
            f"production_year_start={self.production_year_start}, "
            f"production_year_end={self.production_year_end}, "
            f"brand={self.brand}, "
            f"series={self.series}, "
            f"generation={self.generation}, "
            f"category={self.category}, "
            f"set={self.set}, "
            f"piece={self.piece}, "
            # Financial Information for store
            f"purchase_price={self.purchase_price}, "
            f"extra_fee={self.extra_fee}, "
            f"exchange_rate={self.exchange_rate}, "
            f"expected_profit={self.expected_profit}, "
            # Financial Information for customer
            f"customer={self.customer}, "
            f"gender={self.gender}, "
            f"location={self.location}, "
            f"shipping_fee={self.shipping_fee}, "
            f"sale_price={self.sale_price}), "
            f"description={self.description}>"
        )
