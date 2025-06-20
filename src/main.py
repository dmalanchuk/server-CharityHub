from fastapi import FastAPI
from src.api import router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(router.router)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
