# -*- coding: utf-8 -*-

from functools import lru_cache

from app.config import get_settings
from app.tokenization.tokenizer import (
    TextTokenizer,
    BasicEnglishTextTokenizer,
    BasicEnglishTextTokenizerNoAdjectives,
    BasicPolishTextTokenizer,
)

settings = get_settings()

tokenizer_dict = {
    'basic_english': BasicEnglishTextTokenizer,
    'english_no_adjectives': BasicEnglishTextTokenizerNoAdjectives,
    'basic_polish': BasicPolishTextTokenizer,
}


@lru_cache
def tokenizer_provider() -> TextTokenizer:
    tokenizer_class = tokenizer_dict.get(settings.tokenizer_type)
    return tokenizer_class(settings.spacy_model_path)


async def get_tokenizer() -> TextTokenizer:
    yield tokenizer_provider()
