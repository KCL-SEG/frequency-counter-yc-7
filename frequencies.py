"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    for item in items:
        if str(item) not in frequencies:
            frequencies[str(item)] = 1
        else:
            frequencies[str(item)] = frequencies.get(str(item)) + 1

    return frequencies
