from typing import Annotated

from fastapi import APIRouter, Depends

auth_router = APIRouter(
    prefix="/auth"
)


@auth_router.post("/registration") # registration
async def registration_user(
        username: str,
        email: str,
        password: str,
        verification_code: str
):
    ...


@auth_router.post("/login/email") # login email
async def login_users(
        email: str,
        password: str
):
    ...


@auth_router.post("/login/username") # login username
async def login_users(
        username: str,
        password: str
):
    ...


@auth_router.delete("/logout") # logout
async def logout_user():
    ...
