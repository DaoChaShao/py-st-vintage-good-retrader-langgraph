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
from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from ....dbkit import HashAlgorithms, User, UserRoles, hash_password
from ...dependencies import yield_async_session
from ...schemas import (
    AccessTokenResponse,
    CRUDResponse,
    UserResponse,
    UsersDeletion,
    UserSignIn,
    UsersManagement,
    UsersResponse,
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
) -> VerificationResponse:
    """
    Sign in to the system

    :param user: The user info
    :param session: The database session
    :return: The user info and access token
    """
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
    response_model=UserResponse,
)
async def to_sign_up(
        user: UserSignIn,
        session: Annotated[AsyncSession, Depends(yield_async_session)],
) -> UserResponse:
    """
    Sign up a new user

    :param user: The user info
    :param session: The database session
    :return: The user info
    """
    _username: str = user.username
    _password: str = user.password
    _status = ResponseStatus

    # Check whether the username already exists
    _result = await session.execute(select(User).where(User.username == _username))
    _user = _result.scalar_one_or_none()

    if _user is not None:
        raise HTTPException(status_code=_status.CONFLICT.code, detail="The username already exists.")

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
) -> UserResponse:
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


@router.get(
    "/get/users",
    response_model=UsersResponse,
)
async def to_get_users(session: Annotated[AsyncSession, Depends(yield_async_session)]) -> UsersResponse:
    """
    Get all users

    :param session: The database session
    :return: The user info¬
    """
    _result = await session.execute(select(User).where(User.id != 1))
    _users = _result.scalars().all()
    _status = ResponseStatus
    return UsersResponse(
        code=_status.SUCCESS.code,
        message=_status.SUCCESS.message,
        users=[UserResponse.model_validate(_user) for _user in _users]
    )


@router.post(
    "/init/admin",
    response_model=UserResponse,
)
async def to_init_admin(session: Annotated[AsyncSession, Depends(yield_async_session)]) -> UserResponse:
    """
    Sign up a new user

    :param session: The database session
    :return: The user info
    """
    _username: str = "admin"
    _password: str = "12345"
    _status = ResponseStatus

    # Check whether the username already exists
    _result = await session.execute(select(User).where(User.username == _username))
    _user = _result.scalar_one_or_none()

    if _user is not None:
        raise HTTPException(status_code=_status.CONFLICT.code, detail="The username already exists.")

    # Hash the password
    _hashed_password = hash_password(_password, algorithm=HashAlgorithms.ARGON2)

    # Create the user
    _user = User(username=_username, password=_hashed_password, role=UserRoles.ADMIN.value)

    # Save to the database
    session.add(_user)
    await session.commit()
    await session.refresh(_user)

    # Return the registered user
    return UserResponse.model_validate(_user)


@router.patch(
    "/manage/users",
    response_model=UsersResponse,
)
async def to_manage_users(
        users: UsersManagement,
        session: Annotated[AsyncSession, Depends(yield_async_session)],
) -> UsersResponse:
    """
    Manage users

    :param users: The users to manage
    :param session: The database session
    :return: The updated users
    """
    _updated_users: list[User] = []
    _status = ResponseStatus

    for user in users.users:
        _result = await session.execute(select(User).where(User.id == user.id))
        _user = _result.scalar_one_or_none()

        if _user is None:
            raise HTTPException(status_code=_status.NOT_FOUND.code, detail=f"User {user.id} not found.") from None

        _user.role = user.role.value
        _user.is_active = user.is_active
        _updated_users.append(_user)

    await session.commit()

    for _user in _updated_users:
        await session.refresh(_user)

    return UsersResponse(
        code=_status.SUCCESS.code,
        message=_status.SUCCESS.message,
        users=[UserResponse.model_validate(_user) for _user in _updated_users],
    )


@router.delete(
    "/delete",
    response_model=CRUDResponse,
)
async def to_delete_user(
        users: UsersDeletion,
        session: Annotated[AsyncSession, Depends(yield_async_session)]
) -> CRUDResponse:
    """
    Delete users

    :param users: The users to delete
    :param session: The database session
    :return: The result of the operation
    """
    _status = ResponseStatus

    await session.execute(delete(User).where(User.id.in_(users.ids)))
    await session.commit()

    return CRUDResponse(
        code=_status.SUCCESS.code,
        message=_status.SUCCESS.message,
    )
