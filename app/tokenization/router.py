# -*- coding: utf-8 -*-

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from .dependencies import tokenizer_provider, TextTokenizer


class RawText(BaseModel):
    body: str


class TokenizedText(BaseModel):
    tokens: list[str] = []


router = APIRouter()


@router.post("/", response_model=TokenizedText)
async def tokenizer(
    raw_text: RawText, tokenizer: TextTokenizer = Depends(tokenizer_provider)
):
    tokens = await tokenizer.tokenize(raw_text.body)
    return TokenizedText(tokens=tokens)
