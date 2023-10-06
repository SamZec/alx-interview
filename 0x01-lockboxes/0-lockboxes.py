#!/usr/bin/python3
"""module for lockbox implementation"""


def canUnlockAll(boxes):
    """a method that determines if all lockboxes can be opened"""
    index = 0
    keys = list(set(boxes[0]) | {0})
    opened = True
    _boxes = []

    while opened:
        opened = False
        for key in join(boxes, keys[index:]):
            if key <= len(boxes):
                _boxes.append(key)
            if key not in keys:
                keys.append(key)
                index += 1
                opened = True
    return len(set(_boxes)) == len(boxes)


def join(boxes, keys):
    """open a box with the key"""
    res = []
    for key in keys:
        if key > len(boxes) - 1:
            continue
        res += boxes[key]
    return res
