#!/usr/bin/python3
"""
    method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened, else return False
    """
    unlocked_box = [0]
    for i in unlocked_box:
        for j in boxes[i]:
            if j < len(boxes):
                if j not in unlocked_box:
                    unlocked_box.append(j)

    # Look the the length of the open box and all the boxes
    if len(boxes) == len(unlocked_box):
        return True
    else:
        return False
