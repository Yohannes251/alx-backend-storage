#!/usr/bin/env python3
"""list of collection"""


def schools_by_topic(mongo_collection, topic):
    """
    returns list of school that having same topic
    """
    return [i for i in mongo_collection.find({"topics": topic})]