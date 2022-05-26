# -*- coding: utf-8 -*-

from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

from .config import get_settings

settings = get_settings()


async def get_api_key(
    api_key_query: str = Security(
        APIKeyHeader(name=settings.api_key_name, auto_error=False)
    )
):
    if api_key_query == settings.api_key:
        return api_key_query
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid API key")
