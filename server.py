#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/19 00:21
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   server.py
# @Desc     :


from fastapi import FastAPI
from fastapi.responses import FileResponse
from uvicorn import run

from backend.fapi.routers import router

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Initialise database
#     # await init_db()
#
#     yield
#
#     # Dispose database engine
#     # await engine.async_dispose()


app = FastAPI(
    title="Vintage Goods API",
    description="Backend API for Vintage Goods Retrading",
    version="0.1.0",
    # lifespan=lifespan,
)

app.include_router(router.router, prefix="/api")


@app.get("/")
async def root():
    """ Return a message indicating that the API is up and running """
    return {"message": "Vintage Goods API"}


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Return the favicon icon for the API (https://favicon.io/)"""
    return FileResponse("static/favicon.ico")


if __name__ == "__main__":
    """ uv run uvicorn server:app --reload """
    run("server:app", host="127.0.0.1", port=8000, reload=True, log_level="info")
