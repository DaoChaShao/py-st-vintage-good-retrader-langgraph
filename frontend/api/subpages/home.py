#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/11/18 13:12
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :

from streamlit import caption, empty, expander, title

empty_message = empty()
empty_message.info("Please check the details at the different pages of core functions.")

title("Runner Pro")
with expander("**INTRODUCTION (Chinese)**", expanded=False):
    caption("- 基于 Python、Streamlit、FastAPI 和 Requests 开发前后端分离的全栈 Web 应用。")
    caption("- 基于 SQLAlchemy、SQLite 和 aiosqlite 构建异步数据库访问层，实现数据持久化及 CRUD 操作。")
    caption("- 使用 Pydantic 实现 API 数据验证、类型约束及请求与响应模型管理。")
    caption("- 实现商品库存管理，包括商品录入、更新、删除、SKU 验证、关键词搜索及库存状态筛选。")
    caption("- 实现商品采购、销售和重新入库管理，记录商品成本、成交价格、汇率、运输费用及预期利润。")
    caption("- 实现客户信息管理，记录客户姓名、性别及所在地，支持跨境中古商品交易记录。")
    caption("- 实现用户注册、登录、密码哈希、JWT 签发及基于用户角色的页面访问控制。")
    caption("- 使用 Streamlit Session State 和数据缓存优化数据加载与交互体验。")
    caption("- 采用模块化架构组织前端、后端、网络通信及数据库工具，提高代码可维护性与可扩展性。")
    caption("- 使用 uv 管理项目依赖，并结合 Conventional Commits 和 git-changelog 管理版本变更。")

with expander("**INTRODUCTION (English)**", expanded=True):
    caption("- Developed a full-stack web application with a decoupled frontend and backend using Python, Streamlit, FastAPI, and Requests.")
    caption("- Built an asynchronous database access layer using SQLAlchemy, SQLite, and aiosqlite for data persistence and CRUD operations.")
    caption("- Implemented API data validation, type constraints, and request and response schemas using Pydantic.")
    caption("- Developed inventory management features, including product registration, updates, deletion, SKU validation, keyword search, and stock status filtering.")
    caption("- Implemented purchasing, resale, and restocking workflows, tracking acquisition costs, transaction prices, exchange rates, shipping fees, and expected profits.")
    caption("- Integrated customer information management, including customer names, gender, and locations, to support cross-border trading records.")
    caption("- Implemented user registration, authentication, password hashing, JWT issuance, and role-based page access control.")
    caption("- Optimised data loading and user interactions through Streamlit Session State and data caching.")
    caption("- Designed a modular architecture separating frontend, backend, network communication, and database utilities to improve maintainability and extensibility.")
    caption("- Managed project dependencies with uv and maintained version history using Conventional Commits and git-changelog.")
