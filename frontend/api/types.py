#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/24 20:21
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   types.py
# @Desc     :

from enum import StrEnum, unique


@unique
class NZLCityCode(StrEnum):
    AUCKLAND = "AKL"
    WELLINGTON = "WLG"
    CHRISTCHURCH = "CHC"
    HAMILTON = "HLZ"
    DUNEDIN = "DUD"
    TAURANGA = "TRG"


@unique
class CHNCityCode(StrEnum):
    # China - Municipalities
    BEIJING = "BJS"
    TIANJIN = "TJS"
    SHANGHAI = "SHS"
    CHONGQING = "CQS"

    # China - Provinces
    HEBEI = "HEB"
    SHANXI = "SHX"
    LIAONING = "LIA"
    JILIN = "JIL"
    HEILONGJIANG = "HLJ"
    JIANGSU = "JSU"
    ZHEJIANG = "ZHE"
    ANHUI = "ANH"
    FUJIAN = "FUJ"
    JIANGXI = "JXI"
    SHANDONG = "SHD"
    HENAN = "HEN"
    HUBEI = "HUB"
    HUNAN = "HUN"
    GUANGDONG = "GUD"
    HAINAN = "HAI"
    SICHUAN = "SIC"
    GUIZHOU = "GUZ"
    YUNNAN = "YUN"
    SHAANXI = "SNX"
    GANSU = "GAN"
    QINGHAI = "QHA"
    TAIWAN = "TWN"

    # China - Autonomous Regions
    INNER_MONGOLIA = "NMG"
    GUANGXI = "GXI"
    TIBET = "XIZ"
    NINGXIA = "NXA"
    XINJIANG = "XJI"

    # China - Special Administrative Regions
    HONG_KONG = "HKG"
    MACAU = "MAC"


CityCode = unique(
    StrEnum(
        "CityCode",
        {
            **{item.name: item.value for item in NZLCityCode},
            **{item.name: item.value for item in CHNCityCode},
        },
    )
)


@unique
class ProductBrand(StrEnum):
    AYNSLEY = "AYNSLEY"
    ROYAL_ALBERT = "ROYAL ALBERT"
    SHELLEY = "SHELLEY"
    WOODLAND = "WOODLAND"
    PARAGON = "PARAGON"


@unique
class Gender(StrEnum):
    FEMALE = "female"
    Male = "male"
