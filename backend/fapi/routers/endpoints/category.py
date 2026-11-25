#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/25 22:24
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   category.py
# @Desc     :

from fastapi import APIRouter

from ....domains import (
    CHNCityCode,
    CityCode,
    Gender,
    NZLCityCode,
    ProductBrand,
    ProductType,
    UserRole,
)

router = APIRouter()


@router.get("", response_model=dict[str, dict[str, list[str]]])
async def to_get_category() -> dict[str, dict[str, list[str]]]:
    """ Get all categories """
    return {
        "category": {
            "user_roles": [item.value for item in UserRole],
            "nzl_cities": [item.value for item in NZLCityCode],
            "chn_cities": [item.value for item in CHNCityCode],
            "all_cities": [item.value for item in CityCode],
            "product_types": [item.value for item in ProductType],
            "product_brands": [item.value for item in ProductBrand],
            "gender": [item.value for item in Gender],
        }
    }
