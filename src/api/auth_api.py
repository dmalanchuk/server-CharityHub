from typing import Annotated

from fastapi import APIRouter, Depends

auth_router = APIRouter(
    prefix="/auth"
)


@auth_router.post("/login")
async def login_users(
        email: str,
        password: str
):
    ...


@auth_router.post("/register")
async def register_users(
        username: str,
        email: str,
        password: str
):
    ...


@auth_router.get("/info_user_me")
async def get_info_user_me():
    ...
