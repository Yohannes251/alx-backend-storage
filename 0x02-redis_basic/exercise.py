#!/usr/bin/env python3
"""
    This script contains the Cache class
"""

import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Returns a callable that counts calls to methods"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapped function"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper

class Cache:
    """Implementation of Cache class"""
    def __init__(self):
        """Initializes the class"""
        self._redis = redis.Redis()
        self._redis.ping()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores input data by in Redis generating a random uuid key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Returns matched data for key in Redis processed by fn(if present)"""
        if fn is not None:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Performs automatic decoding of value from Cache.get to string"""
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """Performs automatic decoding of value from Cache.get to int"""
        try:
            return int(self._redis.get(key))
        except Exception:
            return 0
