# -*- coding: utf-8 -*-

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .auth import get_api_key
from .config import get_settings
from .tokenization.router import router as tokenization_router
from .similarities.router import router as calculator_router


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    dependencies=[Depends(get_api_key)]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(tokenization_router, prefix='/tokenizer', tags=['tokenizer', ])
app.include_router(calculator_router, prefix='/similarity', tags=['calculator', ])


@app.get('/')
async def homepage():
    return "Things aren't different. Things are things."
