#!/usr/bin/python3
'''determine if all the boxes can be opened
'''


def canUnlockAll(boxes):
    '''determines of all locked boxes can be opened

    Args:
        boxes: locked boxes

    Return:
        True or False
    '''

    i = 0
    length = len(boxes)
    stack = [0]
    opened = [1] + [0] * (length - 1)

    if length == 0:
        return True

    while stack:
        j = stack.pop()
        for k in boxes[j]:
            if k > 0 and k < length and opened[k] == 0:
                opened[k] = 1
                stack.append(k)
        i = i + 1
    if 0 in opened:
        return False

    return True
