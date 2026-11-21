#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/21 20:49
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   account.py
# @Desc     :

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ....dbkit import HashAlgorithms, hash_password
from ....dbkit import User as UserModel
from ...dependencies import yield_async_session
from ...schemas import AccessTokenResponse, SignInResponse, UserResponse
from ...schemas import User as UserSchema
from ...services import JWTAccessTokenEncoder
from ...types import AccessTokenTypes, ResponseStatus

router = APIRouter()


@router.post(
    "/verification",
    response_model=SignInResponse
)
async def verify_user(
        user: UserSchema,
        session: Annotated[AsyncSession, Depends(yield_async_session)],
):
    _username: str = user.username
    _password: str = user.password

    _algorithm: HashAlgorithms = HashAlgorithms.ARGON2
    _hashed_password: str = hash_password(_password, algorithm=_algorithm)
    print(_username, _password, _hashed_password)

    _result = await session.execute(select(UserModel).where(UserModel.username == _username))
    _user = _result.scalar_one_or_none()
    print(_user)

    _unauthorised = ResponseStatus.UNAUTHORIZED
    if _user is None:
        raise HTTPException(status_code=_unauthorised.code, detail="The user cannot be found.")
    elif not PasswordHash.recommended().verify(_password, _user.hashed_password):
        raise HTTPException(status_code=_unauthorised.code, detail="The password is incorrect.")
    else:
        with JWTAccessTokenEncoder() as encoder:
            _token, _expiration = encoder.create(_user.id)
        _status = ResponseStatus.SUCCESS
    return SignInResponse(
        code=_status.code,
        message=_status.message,
        user=UserResponse.model_validate(_user),
        token=AccessTokenResponse(
            token=_token,
            type=AccessTokenTypes.BEARER,
            expires_at=_expiration
        )
    )


@router.post(
    "/registration",
    # response_model=SignInResponse
)
async def register_user(
        user: UserSchema,
        session: Annotated[AsyncSession, Depends(yield_async_session)],
):
    _username: str = user.username
    _password: str = user.password
    print(_username, _password)

    # Check whether the username already exists
    _result = await session.execute(select(UserModel).where(UserModel.username == _username))
    _user = _result.scalar_one_or_none()

    if _user is not None:
        raise HTTPException(status_code=409, detail="The username already exists.")

    # Hash the password
    _hashed_password = hash_password(_password, algorithm=HashAlgorithms.ARGON2)

    # Create the user
    _user = UserModel(username=_username, password=_password, hashed_password=_hashed_password)

    # Save to the database
    session.add(_user)
    await session.commit()
    await session.refresh(_user)

    # Return the registered user
    return UserResponse.model_validate(_user)
