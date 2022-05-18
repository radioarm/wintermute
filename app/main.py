# -*- coding: utf-8 -*-

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi_simple_security import api_key_router, api_key_security

from .config import get_settings
from .tokenization.router import router as tokenization_router


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    # dependencies=[Depends(api_key_security), ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_key_router, prefix='/auth', tags=['auth', ])
app.include_router(tokenization_router, prefix='/tokenizer', tags=['tokenizer', ])

@app.get('/')
async def homepage():
    return "Things aren't different. Things are things."
