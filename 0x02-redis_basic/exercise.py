#!/usr/bin/env python3
"""
    This script contains the Cache class
"""

import redis
import uuid
from typing import Union


class Cache:
    """Implementation of Cache class"""
    def __init__(self):
        """Initializes the class"""
        self._redis = redis.Redis()
        self._redis.ping()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores input data by in Redis generating a random uuid key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
