#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 00:21
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   server.py
# @Desc     :

from contextlib import asynccontextmanager

from fastapi import FastAPI
from uvicorn import run

from backend.fapi.routers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialise database
    # await init_db()

    yield

    # Dispose database engine
    # await engine.async_dispose()


app = FastAPI(
    title="Vintage Goods API",
    description="Backend API for Vintage Goods",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(router, prefix="/goods")


@app.get("/")
async def root():
    return {"message": "Vintage Goods API"}


if __name__ == "__main__":
    run("backend.api.main:app", host="127.0.0.1", port=8000, reload=True)
