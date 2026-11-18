#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/5 22:17
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   models.py
# @Desc     :

from datetime import date

from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column

from .base import DECLARATION, GENERAL


class Goods(DECLARATION):
    """ Model """

    __tablename__ = "goods"

    # Main Keys
    id: Mapped[GENERAL.PK]

    # Attributes
    purchase_date: Mapped[date] = mapped_column(Date, nullable=True)
    sale_date: Mapped[date] = mapped_column(Date, nullable=True)

    product: Mapped[GENERAL.STR]
    category: Mapped[GENERAL.STR]
    price: Mapped[GENERAL.DEC]
    quantity: Mapped[GENERAL.INT]
    description: Mapped[GENERAL.TXT]

    # Timestamps
    created_at: Mapped[GENERAL.CT]
    updated_at: Mapped[GENERAL.UT]

    def __repr__(self) -> str:
        """ Return the string representation of the Goods class """
        return (
            f"<Goods("
            f"id={self.id}, "
            f"product={self.product}, "
            f"price={self.price}, "
            f"quantity={self.quantity}, "
            f"description={self.description}, "
            f"created_at={self.created_at}, "
            f"updated_at={self.updated_at})>"
        )
