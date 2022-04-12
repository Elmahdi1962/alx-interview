#!/usr/bin/env python3
'''LockBoxes Challenge'''


from multiprocessing.dummy import Array
from typing import List


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < length:
        oldi = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                i = key
                break
        if oldi != i:
            continue
        else:
            break
    
    for i in range(length):
        if i not in opened_boxes and i != 0:
            print(f'i = {i}  |  opened boxes : {opened_boxes}')
            return False
    return True
