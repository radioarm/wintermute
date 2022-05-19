# -*- coding: utf-8 -*-

from functools import lru_cache

from app.config import get_settings
from .calculator import Word2VecSimilarityCalculator

settings = get_settings()


@lru_cache
def calculator_provider() -> Word2VecSimilarityCalculator:
    return Word2VecSimilarityCalculator(model_path=settings.word2vec_model_path)


async def get_calculator() -> Word2VecSimilarityCalculator:
    yield calculator_provider()