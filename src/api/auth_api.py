from typing import Annotated

from fastapi import APIRouter, Depends

auth_router = APIRouter(
    prefix="/auth"
)


@auth_router.post("/login")
async def login_users():
    ...


@auth_router.post("/register")
async def register_users():
    ...
