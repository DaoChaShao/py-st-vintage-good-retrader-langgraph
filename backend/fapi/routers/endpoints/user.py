#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/21 20:49
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   user.py
# @Desc     :

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from ....dbkit import HashAlgorithms, User, hash_password
from ...dependencies import yield_async_session
from ...schemas import (
    AccessTokenResponse,
    UserResponse,
    UserSignIn,
    UserUpdate,
    VerificationResponse,
)
from ...services import JWTAccessTokenEncoder
from ...types import AccessTokenTypes, ResponseStatus

router = APIRouter()


@router.post(
    "/sign/in",
    response_model=VerificationResponse
)
async def to_sign_in(
        user: UserSignIn,
        session: Annotated[AsyncSession, Depends(yield_async_session)],
):
    _username: str = user.username
    _password: str = user.password

    _result = await session.execute(select(User).where(User.username == _username))
    _user = _result.scalar_one_or_none()

    _status = ResponseStatus
    if _user is None:
        raise HTTPException(status_code=_status.UNAUTHORISED.code, detail="The user cannot be found.")
    elif not PasswordHash.recommended().verify(_password, _user.password):
        raise HTTPException(status_code=_status.UNAUTHORISED.code, detail="The password is incorrect.")
    else:
        with JWTAccessTokenEncoder() as encoder:
            _token, _expiration = encoder.create(_user.id)
        _status = ResponseStatus.SUCCESS
    return VerificationResponse(
        code=_status.SUCCESS.code,
        message=_status.SUCCESS.message,
        user=UserResponse.model_validate(_user),
        token=AccessTokenResponse(
            token=_token,
            type=AccessTokenTypes.BEARER,
            expires_at=_expiration
        )
    )


@router.post(
    "/sign/up",
    # response_model=SignInResponse
)
async def to_sign_up(
        user: UserSignIn,
        session: Annotated[AsyncSession, Depends(yield_async_session)],
):
    _username: str = user.username
    _password: str = user.password

    # Check whether the username already exists
    _result = await session.execute(select(User).where(User.username == _username))
    _user = _result.scalar_one_or_none()

    if _user is not None:
        raise HTTPException(status_code=409, detail="The username already exists.")

    # Hash the password
    _hashed_password = hash_password(_password, algorithm=HashAlgorithms.ARGON2)

    # Create the user
    _user = User(username=_username, password=_hashed_password)

    # Save to the database
    session.add(_user)
    await session.commit()
    await session.refresh(_user)

    # Return the registered user
    return UserResponse.model_validate(_user)


@router.post(
    "/update",
    response_model=UserResponse,
)
async def to_update(
        user: UserUpdate,
        session: Annotated[AsyncSession, Depends(yield_async_session)],
):
    """
    Update the user info in the database

    :param user: The user info
    :param session: The database session
    :return: The user info
    """
    _result = await session.execute(select(User).where(User.id == user.id))
    _user = _result.scalar_one_or_none()
    _status = ResponseStatus

    if _user is None:
        raise HTTPException(status_code=_status.NOT_FOUND.code, detail="The user cannot be found.")

    _updates = user.model_dump(exclude_unset=True)

    if "username" in _updates:
        _user.username = _updates["username"]
    if "role" in _updates:
        _user.role = _updates["role"]
    if "is_active" in _updates:
        _user.is_active = _updates["is_active"]

    if _updates.get("new_password"):
        if not _updates.get("old_password"):
            raise HTTPException(status_code=_status.BAD_REQUEST.code, detail="Original password is required.")

        if not PasswordHash.recommended().verify(_updates["old_password"], _user.password):
            raise HTTPException(status_code=_status.UNAUTHORISED.code, detail="Original password is incorrect.")

        _user.password = PasswordHash.recommended().hash(_updates["new_password"])

    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=_status.CONFLICT.code, detail="The username already exists.") from None

    await session.refresh(_user)

    return UserResponse.model_validate(_user)
