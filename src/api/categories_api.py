from fastapi import APIRouter


categories_router = APIRouter(
    tags=["categories"]
)


@categories_router.get("/")
async def get_categories():
    pass


@categories_router.post("/")
async def post_categories():
    pass
