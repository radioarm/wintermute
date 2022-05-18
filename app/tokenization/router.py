# -*- coding: utf-8 -*-

from fastapi import APIRouter, Depends

from app.tokenization.dependencies import tokenizer_provider, TextTokenizer

router = APIRouter()

@router.get("/")
async def tokenizer(tokenizer: TextTokenizer = Depends(tokenizer_provider)):
    return ', '.join(tokenizer.stop_words)