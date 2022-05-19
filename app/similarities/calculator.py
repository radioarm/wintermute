# -*- coding: utf-8 -*-

from itertools import product
from statistics import mean

import gensim.models.keyedvectors as word2vec


class Word2VecSimilarityCalculator:
    def __init__(self, model_path, limit=0):
        self.model_path = model_path
        self.limit = limit
        self.model = word2vec.KeyedVectors.load_word2vec_format(
            model_path, binary=True, limit=limit
        )

    def calculate_word_similarity(self, word1, word2) -> float:
        try:
            return round(float(self.model.similarity(word1, word2)), 3)
        except KeyError:
            return 0

    async def calculate_wordset_similarity(
        self, wordset_1: list[str], wordset_2: list[str]
    ) -> tuple[float, list]:
        details = [
            pair + (self.calculate_word_similarity(*pair),)
            for pair in product(wordset_1, wordset_2)
        ]
        final_value = (
            round(float(mean([vec[-1] for vec in details])), 3) if details else 0
        )
        return final_value, details
