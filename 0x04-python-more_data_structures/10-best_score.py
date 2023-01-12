#!/usr/bin/python3
# 10-best_score.py


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not forininstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret = list(a_dictionary.keys())[0]
    big = a_dictionary[ret]
    for i, v in a_dictionary.items():
        if v > big:
            big = v
            ret = i
    return (ret)