# -*- coding: utf-8 -*-

from functools import lru_cache
from os.path import abspath, dirname, join, normpath
from pydantic import BaseSettings
from typing import Set


APP_ROOT = dirname(abspath(__file__))
PROJECT_ROOT = dirname(APP_ROOT)


class Settings(BaseSettings):
    app_name: str = 'Wintermute'
    allowed_origins: Set[str] = set()
    word2vec_model_path: str
    spacy_model_path: str
    tokenizer_type: str = 'basic_english'

    class Config:
        env_file = normpath(join(PROJECT_ROOT, '.env'))


@lru_cache()
def get_settings():
    return Settings()