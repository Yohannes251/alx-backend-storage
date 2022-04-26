#!/usr/bin/env python3
""" inserts a new document in colln """

import pymongo


def insert_school(mongo_collection, **kwargs):
    """based on kwargs"""
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
