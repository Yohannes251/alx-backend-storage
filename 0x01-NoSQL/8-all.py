#!/usr/bin/env python3
""" lists all doc in a colln """

import pymongo


def list_all(mongo_collection):
    """ lists all documents """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
