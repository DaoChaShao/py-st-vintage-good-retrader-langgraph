#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/22 00:41
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   dialogs.py
# @Desc     :

from datetime import date, datetime
from decimal import Decimal
from re import fullmatch
from time import sleep
from typing import Any

from streamlit import (
    button,
    caption,
    column_config,
    columns,
    data_editor,
    date_input,
    datetime_input,
    dialog,
    empty,
    form,
    form_submit_button,
    number_input,
    rerun,
    segmented_control,
    selectbox,
    session_state,
    spinner,
    text_area,
    text_input,
)

from ...net import (
    URL,
    request_to_delete_good,
    request_to_delete_tables,
    request_to_delete_users,
    request_to_get_category,
    request_to_get_goods,
    request_to_get_users,
    request_to_init_admin,
    request_to_initialise_tables,
    request_to_manage_users,
    request_to_post_good,
    request_to_restock_good,
    request_to_sell_good,
    request_to_sign_up,
    request_to_update,
    request_to_update_good,
)

CATEGORY = request_to_get_category(URL.GET_CATEGORY)


@dialog("Delete Tables", position="center", width="small", icon=":material/delete:")
def dialog_delete_tables() -> None:
    """ Delete all tables """
    left, right = columns(2)
    if left.button("Yes", type="secondary", width="stretch"):
        request_to_delete_tables(URL.DELETE_TABLES)
        rerun()

    if right.button("No", type="primary", width="stretch"):
        rerun()


@dialog("Delete Users", position="center", width="medium", icon=":material/delete:")
def dialog_delete_users(curr_id: int) -> None:
    """ Delete all users """
    notification = empty()

    filtered_users = [
        {**user, "selected": False}
        for user in request_to_get_users(URL.GET_USERS)
        if user["id"] != curr_id
    ]
    edited_users = data_editor(
        filtered_users,
        hide_index=True, width="stretch", height="stretch",
        column_config={
            "selected": column_config.CheckboxColumn("Delete"),
        },
        disabled=["id", "username", "role", "is_active", "created_at", "updated_at"],
    )

    deleted_ids = [int(user["id"]) for user in edited_users if user["selected"]]

    if button("Delete", type="primary", width="stretch"):
        with spinner("Updating...", show_time=True, width="stretch"):
            response = request_to_delete_users(URL.DELETE_USERS, ids=deleted_ids)
            if response.ok:
                rerun()
            else:
                notification.error(
                    f"Delete failed ({response.status_code}): {response.text}",
                    icon=":material/error:"
                )


@dialog("Initialise Tables", position="center", width="small", icon=":material/add:")
def dialog_init_tables() -> None:
    """ Initialise all tables and an administrator """
    left, right = columns(2)
    if left.button("Yes", type="secondary", width="stretch"):
        request_to_initialise_tables(URL.INITIALISE_TABLES)
        sleep(1)
        request_to_init_admin(URL.INIT_ADMIN)
        rerun()

    if right.button("No", type="primary", width="stretch"):
        rerun()


@dialog("Register", position="center", width="small", icon=":material/account_circle:")
def dialog_sign_up() -> None:
    """ Dialog for user registration """
    notification = empty()

    with form("registration_form", border=True, clear_on_submit=True, width="stretch", height="stretch"):
        username: str = text_input(
            "Username", placeholder="Enter your username", required=True,
            type="default", icon=":material/person:",
            help="Enter your username here"
        )
        password: str = text_input(
            "Password", placeholder="Enter your password", required=True,
            type="password", icon=":material/vpn_key_alert:",
            help="Enter your password here"
        )
        confirmation: str = text_input(
            "Confirm Password", placeholder="Re-enter your password", required=True,
            type="password", icon=":material/vpn_key:",
            help="Re-enter your password here"
        )

        if form_submit_button("Register", type="primary", width="stretch", icon=":material/input:"):
            if password != confirmation:
                notification.warning("Passwords do not match", icon=":material/warning:")
            else:
                response = request_to_sign_up(URL.SIGN_UP, username=username, password=password)
                if response.ok:
                    rerun()
                else:
                    notification.error("Registration failed", icon=":material/error:")


@dialog("Manage User", position="center", width="medium", icon=":material/person:")
def dialog_manage_users(curr_id: int) -> None:
    """ Dialog for managing users """
    notification = empty()

    filtered_users = [
        user
        for user in request_to_get_users(URL.GET_USERS)
        if user["id"] != curr_id
    ]
    edited_users = data_editor(
        filtered_users,
        hide_index=True, width="stretch", height="stretch",
        column_config={
            "is_active": column_config.CheckboxColumn("Active Status"),
            "role": column_config.SelectboxColumn("Account Role", options=["user", "admin"]),
        },
        disabled=["id", "username", "created_at", "updated_at"],
    )

    original_users = {user["id"]: user for user in filtered_users}
    changed_users = [
        user
        for user in edited_users
        if (
                user["role"] != original_users[user["id"]]["role"]
                or user["is_active"] != original_users[user["id"]]["is_active"]
        )
    ]

    if button("Manage", type="primary", width="stretch"):
        with spinner("Updating...", show_time=True, width="stretch"):
            response = request_to_manage_users(URL.MANAGE_USERS, changed_users=changed_users)
            if response.ok:
                rerun()
            else:
                notification.error(
                    f"Update failed ({response.status_code}): {response.text}",
                    icon=":material/error:"
                )


@dialog("Update User Information", position="center", width="small", icon=":material/person:")
def dialog_update_user(user: Any) -> None:
    """ Dialog for updating user information """
    notification = empty()

    with form("update_user_info_form", border=True, clear_on_submit=True, width="stretch", height="stretch"):
        _id = number_input(
            "User ID", placeholder="Your user ID", required=True,
            icon=":material/id_card:", width="stretch", disabled=True,
            help="Your user ID here",
            value=user["id"],
        )
        _username = text_input(
            "Username", placeholder="Your username", required=True,
            type="default", icon=":material/person:", width="stretch", disabled=True,
            help="Your username here",
            value=user["username"],
        )
        _old_password = text_input(
            "Password", placeholder="Your password", required=False,
            type="password", icon=":material/vpn_key_alert:", width="stretch", disabled=False,
            help="Your password here", key="old_password"
        )
        _new_password = text_input(
            "Password", placeholder="Your password", required=False,
            type="password", icon=":material/vpn_key_alert:", width="stretch", disabled=False,
            help="Your password here", key="new_password"
        )
        _confirmation = text_input(
            "Confirm Password", placeholder="Re-enter your password", required=False,
            type="password", icon=":material/vpn_key:", width="stretch", disabled=False,
            help="Re-enter your password here", key="confirmation"
        )

        info_left, info_right = columns(2)
        _role = info_left.segmented_control(
            "Account Role", options=CATEGORY["user_roles"], required=True,
            selection_mode="single", width="stretch", disabled=True,
            help="Your account role",
            default=user["role"],
        )
        _status: bool = info_right.toggle(
            "Active Status",
            width="stretch", disabled=True,
            help="Your active status",
            value=user["is_active"],
        )
        _created_at: datetime = datetime_input(
            "Registration Date", required=True,
            width="stretch", disabled=True,
            help="Your registration date here",
            value=user["created_at"],
        )
        _updated_at: datetime = datetime_input(
            "Last Updated", required=True,
            width="stretch", disabled=True,
            help="Your last updated date here",
            value=datetime.today(),
        )

        if form_submit_button("Update", type="primary", width="stretch", icon=":material/input:"):
            if _new_password != _confirmation:
                notification.warning("Passwords do not match", icon=":material/warning:")
            elif _new_password and not _old_password:
                notification.warning("Original password is required", icon=":material/warning:")
            else:
                response = request_to_update(
                    URL.UPDATE,
                    user_id=_id,
                    username=_username,
                    old_password=_old_password,
                    new_password=_new_password,
                    role=_role.lower(),
                    status=_status,
                    updated_at=_updated_at,
                )
                if response.ok:
                    rerun()
                else:
                    notification.error("Update failed", icon=":material/error:")


@dialog("New Vintage Good Creation", position="center", width="medium", icon=":material/add:")
def dialog_create_good() -> None:
    """ Dialog for creating a new good """
    notification = empty()

    date_left, date_right = columns(2)
    with date_left:
        _purchase_date: date = date_input(
            "Purchase Date", required=True,
            width="stretch",
            help="The purchase date of the good",
            disabled=False, value=date.today(),
        )
    with date_right:
        _sale_date: date = date_input(
            "Sale Date", required=False,
            width="stretch",
            help="The sale date of the good",
            disabled=True, value=None,
        )

    code_left, code_mid, code_right = columns(3)
    with code_left:
        _city: str = selectbox(
            "City", placeholder="The city where the good is from", required=True,
            options=CATEGORY["all_cities"],
            icon=":material/source_environment:", width="stretch",
            help="The city where the good is from",
            disabled=False, index=0,
        )
    with code_mid:
        _store: str = text_input(
            "Store", placeholder="The store where the good is from", required=False,
            type="default", icon=":material/store:", width="stretch",
            help="The store where the good is from",
            disabled=False, value=None,
        )
    with code_right:
        _sku: str = text_input(
            "Stock Keeping Unit", placeholder="The SKU of the good", required=True,
            type="default", icon=":material/barcode:", max_chars=15, width="stretch",
            help="The stock keeping unit of the good",
            disabled=False, value=f"{_city}{_purchase_date.strftime('%Y%m%d')}",
        )

    with form("create_good_form", border=True, clear_on_submit=True, width="stretch", height="stretch"):
        good_left, good_mid, good_right = columns(3)
        with good_left:
            _product: str = text_input(
                "Product", placeholder="The product name", required=True,
                type="default", icon=":material/emoji_food_beverage:", width="stretch",
                help="The product name",
                disabled=False, value=None,
            )
            _brand: str = selectbox(
                "Brand", placeholder="The brand of the good", required=True,
                options=CATEGORY["product_brands"],
                icon=":material/copyright:", width="stretch",
                help="The brand of the good",
                disabled=False, index=0,
            )
        with good_mid:
            _production_year_start: int = number_input(
                "Production Year Start", placeholder="The year start", required=False,
                min_value=1, max_value=9_999, step=1,
                icon=":material/line_start_circle:", width="stretch",
                help="The production year start",
                disabled=False, value=None,
            )
            _series: str = text_input(
                "Series", placeholder="The series of the good", required=False,
                type="default", icon=":material/timeline:", width="stretch",
                help="The series of the good",
                disabled=False, value=None,
            )
        with good_right:
            _production_year_end: int = number_input(
                "Production Year End", placeholder="The year end", required=False,
                min_value=1, max_value=9_999, step=1,
                icon=":material/line_end_circle:", width="stretch",
                help="The production year end",
                disabled=False, value=None,
            )
            _generation: int = number_input(
                "Generation", placeholder="The generation of the good", required=False,
                min_value=1, max_value=4, step=1,
                icon=":material/pin:", width="stretch",
                help="The generation of the good",
                disabled=False, value=None,
            )

        _category: str = segmented_control(
            "Category", required=True,
            options=CATEGORY["product_types"],
            selection_mode="single", width="stretch",
            help="The category of the good",
            disabled=False, default=CATEGORY["product_types"][0],
        )

        qty, fin_left, fin_right = columns(3)
        # Quantity
        with qty:
            _set: int = number_input(
                "Set", placeholder="The set number", required=True,
                min_value=1, max_value=9_999, step=1,
                icon=":material/coffee:", width="stretch",
                help="The set number",
                disabled=False, value=None,
            )
            _piece: int = number_input(
                "Piece/Set", placeholder="The piece number", required=True,
                min_value=1, max_value=9_999, step=1,
                icon=":material/toys_and_games:", width="stretch",
                help="The piece number",
                disabled=False, value=None,
            )
        # Financial Information
        with fin_left:
            _price: float = number_input(
                "Purchase Price (NZD)", placeholder="The price of the good", required=True,
                min_value=0.0, max_value=9_999.99, step=0.01, format="%.2f",
                icon=":material/paid:", width="stretch",
                help="The price of the good",
                disabled=False, value=None,
            )
            _exchange_rate: float = number_input(
                "Exchange Rate (NZD)", placeholder="The exchange rate", required=True,
                min_value=0.0, max_value=9_999.99, step=0.01, format="%.2f",
                icon=":material/currency_exchange:", width="stretch",
                help="The exchange rate",
                disabled=False, value=None,
            )
        with fin_right:
            _extra_fee: float = number_input(
                "Extra Fee (NZD)", placeholder="The extra fee", required=False,
                min_value=0.0, max_value=9_999.99, step=0.01, format="%.2f",
                icon=":material/delivery_truck_speed:", width="stretch",
                help="The extra fee",
                disabled=False, value=None,
            )
            _expected_profit: float = number_input(
                "Expected Profit (NZD)", placeholder="The expected profit", required=False,
                min_value=0.0, max_value=9_999.99, step=0.01, format="%.2f",
                icon=":material/money_bag:", width="stretch",
                help="The expected profit",
                disabled=False, value=None,
            )
        # Description
        _description: str = text_area(
            "Description", placeholder="The description of the good", required=False,
            width="stretch", height="stretch",
            help="The description of the good",
            disabled=False, value=None,
        )

        if form_submit_button("Create", type="primary", width="stretch", icon=":material/add:"):
            # SKU format validation
            _prefix: str = f"{_city}{_purchase_date:%Y%m%d}"
            if not fullmatch(rf"{_prefix}[0-9]{{4}}", _sku):
                notification.warning(
                    "Invalid SKU. Please enter a valid 4-digit product code.",
                    icon=":material/warning:"
                )
                return

            # SKU uniqueness validation
            if any(_sku == good["sku"] for good in session_state.GOODS):
                notification.warning(f"SKU '{_sku}' already exists.", icon=":material/warning:")
                return

            _good: dict[str, Any] = {
                # Dates
                "purchase_date": _purchase_date,
                "sale_date": _sale_date,
                # Good Infor
                "sku": _sku.strip(),
                "city": _city,
                "store": _store.strip().title() if _store else None,
                "product": _product.strip().title() if _product else None,
                "production_year_start": _production_year_start,
                "production_year_end": _production_year_end,
                "brand": _brand.strip().upper() if _brand else None,
                "series": _series.strip().lower() if _series else None,
                "generation": _generation,
                "category": _category,
                # Quantity
                "set": _set,
                "piece": _piece,
                # Financial Info
                "purchase_price": Decimal(_price),
                "extra_fee": Decimal(_extra_fee) if _extra_fee is not None else None,
                "exchange_rate": Decimal(_exchange_rate),
                "expected_profit": Decimal(_expected_profit) if _expected_profit is not None else None,
                # Description
                "description": _description.strip() if _description is not None else None,

            }
            _response = request_to_post_good(URL.CREATE_GOOD, _good)

            if _response.ok:
                request_to_get_goods.clear()
                session_state.GOODS = None
                notification.success("Creation successful", icon=":material/check_circle:")
                sleep(1)
                rerun()
            else:
                notification.error(
                    f"Creation failed ({_response.status_code}): {_response.text}",
                    icon=":material/error:",
                )


@dialog("Delete Good", position="center", width="small", icon=":material/delete:")
def dialog_delete_good(db_id: int) -> None:
    """
    Dialog for deleting a good

    :param db_id: The database ID of the good to delete
    :return: None
    """
    notification = empty()
    caption("**Are you sure you want to delete this good?**")

    left, right = columns(2)
    if left.button("Yes", type="secondary", width="stretch", icon=":material/check:"):
        _response = request_to_delete_good(URL.DELETE_GOOD, db_id)
        if _response.ok:
            request_to_get_goods.clear()
            session_state.GOODS = None
            notification.success("Deletion successful", icon=":material/check_circle:")
            sleep(1)
            rerun()
        else:
            notification.error(
                f"Deletion failed ({_response.status_code}): {_response.text}",
                icon=":material/error:",
            )
    if right.button("No", type="primary", width="stretch", icon=":material/close:"):
        notification.info("Deletion cancelled", icon=":material/info:")
        sleep(1)
        rerun()


@dialog("Update Good Information", position="center", width="medium", icon=":material/refresh:")
def dialog_update_good(*, db_id: int, good: dict[str, Any]) -> None:
    """
    Dialog for updating a good

    :param db_id: The database ID of the good to update
    :param good: The good to update
    :return: None
    """
    notification = empty()

    date_left, date_right = columns(2)
    with date_left:
        _purchase_date: date = date_input(
            "Purchase Date", required=True,
            width="stretch",
            help="The purchase date of the good",
            disabled=True, value=good["purchase_date"],
        )
    with date_right:
        _sale_date: date = date_input(
            "Sale Date", required=False,
            width="stretch",
            help="The sale date of the good",
            disabled=True, value=good["sale_date"],
        )

    code_left, code_mid, code_right = columns(3)
    with code_left:
        _city: str = selectbox(
            "City", placeholder="The city where the good is from", required=True,
            options=CATEGORY["all_cities"],
            icon=":material/source_environment:", width="stretch",
            help="The city where the good is from",
            disabled=True, index=CATEGORY["all_cities"].index(good["city"]),
        )
    with code_mid:
        _store: str = text_input(
            "Store", placeholder="The store where the good is from", required=False,
            type="default", icon=":material/store:", width="stretch",
            help="The store where the good is from",
            disabled=False, value=good["store"],
        )
    with code_right:
        _sku: str = text_input(
            "Stock Keeping Unit", placeholder="The SKU of the good", required=True,
            type="default", icon=":material/barcode:", max_chars=15, width="stretch",
            help="The stock keeping unit of the good",
            disabled=True, value=good["sku"],
        )

    with form("update_good_form", border=True, clear_on_submit=True, width="stretch", height="stretch"):
        good_left, good_mid, good_right = columns(3)
        with good_left:
            _product: str = text_input(
                "Product", placeholder="The product name", required=True,
                type="default", icon=":material/emoji_food_beverage:", width="stretch",
                help="The product name",
                disabled=False, value=good["product"],
            )
            _brand: str = selectbox(
                "Brand", placeholder="The brand of the good", required=True,
                options=CATEGORY["product_brands"],
                icon=":material/copyright:", width="stretch",
                help="The brand of the good",
                disabled=False, index=CATEGORY["product_brands"].index(good["brand"]),
            )
        with good_mid:
            _production_year_start: int = number_input(
                "Production Year Start", placeholder="The year start", required=False,
                min_value=1, max_value=9_999, step=1,
                icon=":material/line_start_circle:", width="stretch",
                help="The production year start",
                disabled=False, value=good["production_year_start"],
            )
            _series: str = text_input(
                "Series", placeholder="The series of the good", required=False,
                type="default", icon=":material/timeline:", width="stretch",
                help="The series of the good",
                disabled=False, value=good["series"],
            )
        with good_right:
            _production_year_end: int = number_input(
                "Production Year End", placeholder="The year end", required=False,
                min_value=1, max_value=9_999, step=1,
                icon=":material/line_end_circle:", width="stretch",
                help="The production year end",
                disabled=False, value=good["production_year_end"],
            )
            _generation: int = number_input(
                "Generation", placeholder="The generation of the good", required=False,
                min_value=1, max_value=4, step=1,
                icon=":material/pin:", width="stretch",
                help="The generation of the good",
                disabled=False, value=good["generation"],
            )

        _category: str = segmented_control(
            "Category", required=True,
            options=CATEGORY["product_types"],
            selection_mode="single", width="stretch",
            help="The category of the good",
            disabled=True, default=good["category"],
        )

        qty, fin_left, fin_right = columns(3)
        # Quantity
        with qty:
            _set: int = number_input(
                "Set", placeholder="The set number", required=True,
                min_value=1, max_value=9_999, step=1,
                icon=":material/coffee:", width="stretch",
                help="The set number",
                disabled=False, value=good["set"],
            )
            _piece: int = number_input(
                "piece/Set", placeholder="The piece number", required=True,
                min_value=1, max_value=9_999, step=1,
                icon=":material/toys_and_games:", width="stretch",
                help="The piece number",
                disabled=False, value=good["piece"],
            )
        # Financial Information
        with fin_left:
            _price: float = number_input(
                "Purchase Price (NZD)", placeholder="The price of the good", required=True,
                min_value=0.0, max_value=9_999.99, step=0.01, format="%.2f",
                icon=":material/paid:", width="stretch",
                help="The price of the good",
                disabled=False, value=float(good["purchase_price"]) if good["purchase_price"] is not None else None,
            )
            _exchange_rate: float = number_input(
                "Exchange Rate (NZD)", placeholder="The exchange rate", required=True,
                min_value=0.0, max_value=9_999.99, step=0.01, format="%.2f",
                icon=":material/currency_exchange:", width="stretch",
                help="The exchange rate",
                disabled=False, value=float(good["exchange_rate"]) if good["exchange_rate"] is not None else None,
            )
        with fin_right:
            _extra_fee: float = number_input(
                "Extra Fee (NZD)", placeholder="The extra fee", required=False,
                min_value=0.0, max_value=9_999.99, step=0.01, format="%.2f",
                icon=":material/delivery_truck_speed:", width="stretch",
                help="The extra fee",
                disabled=False, value=float(good["extra_fee"]) if good["extra_fee"] is not None else None,
            )
            _expected_profit: float = number_input(
                "Expected Profit (NZD)", placeholder="The expected profit", required=False,
                min_value=0.0, max_value=9_999.99, step=0.01, format="%.2f",
                icon=":material/money_bag:", width="stretch",
                help="The expected profit",
                disabled=False, value=float(good["expected_profit"]) if good["expected_profit"] is not None else None,
            )
        # Description
        _description: str = text_area(
            "Description", placeholder="The description of the good", required=False,
            width="stretch", height="stretch",
            help="The description of the good",
            disabled=False, value=good["description"],
        )

        if form_submit_button("Update", type="primary", width="stretch", icon=":material/refresh:"):
            _prefix: str = f"{_city}{_purchase_date:%Y%m%d}"
            if not fullmatch(rf"{_prefix}[0-9]{{4}}", _sku):
                notification.warning(
                    "Invalid SKU. Please enter a valid 4-digit product code.",
                    icon=":material/warning:"
                )
                return

            _good: dict[str, Any] = {
                # Dates
                "purchase_date": _purchase_date,
                "sale_date": _sale_date,
                # Good Infor
                "sku": _sku.strip(),
                "city": _city,
                "store": _store.strip().title() if _store else None,
                "product": _product.strip().title() if _product else None,
                "production_year_start": _production_year_start,
                "production_year_end": _production_year_end,
                "brand": _brand.strip().upper() if _brand else None,
                "series": _series.strip().lower() if _series else None,
                "generation": _generation,
                "category": _category,
                # Quantity
                "set": _set,
                "piece": _piece,
                # Financial Info
                "purchase_price": Decimal(_price),
                "extra_fee": Decimal(_extra_fee) if _extra_fee is not None else None,
                "exchange_rate": Decimal(_exchange_rate),
                "expected_profit": Decimal(_expected_profit) if _expected_profit is not None else None,
                # Description
                "description": _description.strip() if _description is not None else None,
            }
            _response = request_to_update_good(URL.UPDATE_GOOD, db_id=db_id, good=_good)

            if _response.ok:
                request_to_get_goods.clear()
                session_state.GOODS = None
                notification.success("Update successfully", icon=":material/check_circle:")
                sleep(1)
                rerun()
            else:
                notification.error(
                    f"Creation failed ({_response.status_code}): {_response.text}",
                    icon=":material/error:",
                )


@dialog("Sell Good", position="center", width="small", icon=":material/sell:")
def dialog_sell_good(db_id: int) -> None:
    """
    Sell a good

    :param db_id: The database ID of the good to sell
    :return: None
    """
    notification = empty()
    caption("**Are you sure you want to sell this good right now?**")

    with form("sale_form", border=True, clear_on_submit=True, width="stretch", height="stretch"):
        upper_left, upper_right = columns(2)
        lower_left, lower_right = columns(2)
        with upper_left:
            _customer: str = text_input(
                "Customer Name", placeholder="The name of a customer", required=True,
                type="default", icon=":material/badge:", max_chars=15, width="stretch",
                help="The name of a customer",
                disabled=False, value=None,
            )
        with upper_right:
            _gender: str = segmented_control(
                "Gender", required=False,
                options=CATEGORY["gender"], format_func=lambda gender: gender.capitalize(),
                selection_mode="single", width="stretch",
                help="The category of the good",
                disabled=False, default=None,
            )
        with lower_left:
            _location: str = selectbox(
                "Location", placeholder="The buyer location where the good is from", required=False,
                options=CATEGORY["chn_cities"],
                icon=":material/source_environment:", width="stretch",
                help="The buyer location where the good is from",
                disabled=False, index=None,
            )
        with lower_right:
            _shipping_fee: float = number_input(
                "Shipping Fee (CNY)", placeholder="The shipping fee", required=True,
                min_value=0.0, max_value=9_999.99, step=0.01, format="%.2f",
                icon=":material/delivery_truck_speed:", width="stretch",
                help="The shipping fee",
                disabled=False, value=None,
            )
        _price: float = number_input(
            "Sale Price (CNY)", placeholder="The price of the good", required=True,
            min_value=0.0, max_value=9_999.99, step=0.01, format="%.2f",
            icon=":material/paid:", width="stretch",
            help="The price of the good",
            disabled=False, value=None,
        )

        if form_submit_button("Sell", type="primary", width="stretch", icon=":material/check:"):
            if _price == 0.0 or _price is None:
                notification.warning("Sale price cannot be zero", icon=":material/warning:")
                return

            _info: dict[str, Any] = {
                "customer": _customer.strip(),
                "gender": _gender.strip() if _gender else None,
                "location": _location.strip() if _location else None,
                "shipping_fee": Decimal(str(_shipping_fee)),
                "sale_price": Decimal(str(_price)),
            }

            _response = request_to_sell_good(URL.SELL_GOOD, db_id=db_id, customer=_info)
            if _response.ok:
                request_to_get_goods.clear()
                session_state.GOODS = None
                notification.success("Sell successfully", icon=":material/check_circle:")
                sleep(1)
                rerun()
            else:
                notification.error(
                    f"Sale failed ({_response.status_code}): {_response.text}",
                    icon=":material/error:",
                )


@dialog("Restock Good", position="center", width="small", icon=":material/sell:")
def dialog_restock_good(db_id: int) -> None:
    """
    Restock a good

    :param db_id: The database ID of the good to restock
    :return: None
    """
    notification = empty()
    caption("**Are you sure you want to restock this good?**")

    left, right = columns(2)
    if left.button("Yes", type="secondary", width="stretch", icon=":material/check:"):
        _response = request_to_restock_good(URL.RESTOCK_GOOD, db_id=db_id)
        if _response.ok:
            request_to_get_goods.clear()
            session_state.GOODS = None
            notification.success("Sell successfully", icon=":material/check_circle:")
            sleep(1)
            rerun()
        else:
            notification.error(
                f"Sale failed ({_response.status_code}): {_response.text}",
                icon=":material/error:",
            )
    if right.button("No", type="primary", width="stretch", icon=":material/close:"):
        notification.info("Sale cancelled", icon=":material/info:")
        sleep(1)
        rerun()
