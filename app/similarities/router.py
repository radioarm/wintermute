# -*- coding: utf-8 -*-

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from .dependencies import get_calculator
from .calculator import Word2VecSimilarityCalculator

router = APIRouter()


class WordSetsIn(BaseModel):
    wordset_1: list[str] = []
    wordset_2: list[str] = []


class SimilarityOut(BaseModel):
    value: float = 0
    details: list[tuple] = []


@router.post('/', response_model=SimilarityOut)
async def tokenizer(
    wordsets: WordSetsIn,
    calculator: Word2VecSimilarityCalculator = Depends(get_calculator),
):
    result_tuple = await calculator.calculate_wordset_similarity(
        wordsets.wordset_1, wordsets.wordset_2
    )
    return SimilarityOut(value=result_tuple[0], details=result_tuple[1])
