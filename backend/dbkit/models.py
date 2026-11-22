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


class Goods(BASE):
    """ Goods Model """

    __tablename__ = "goods"
    __table_args__ = {"comment": "Goods Table"}

    purchase_date: Mapped[GENERAL.DT]
    sale_date: Mapped[GENERAL.DT]

    product: Mapped[GENERAL.STR]
    category: Mapped[GENERAL.STR]
    price: Mapped[GENERAL.DEC]
    quantity: Mapped[GENERAL.INT]
    description: Mapped[GENERAL.TXT]

    def __repr__(self) -> str:
        """ Return the string representation of the Goods class """
        return (
            f"<Goods("
            f"{super().__repr__()}"
            f"purchase_date={self.purchase_date}, "
            f"sale_date={self.sale_date}, "
            f"product={self.product}, "
            f"category={self.category}, "
            f"price={self.price}, "
            f"quantity={self.quantity}, "
            f"description={self.description})>"
        )


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
