#!/usr/bin/env python3
from math import *

BOTTOM_LEFT = (0,0)
TOP_RIGHT   = (0,0)
SOURCE      = (0,0)
TARGET      = (0,0)
DISTANCE    = 0
BOTTOM_RIGHT    = (0,0)
TOP_LEFT    = (0,0)

def answer(tr, src, bp, dist):
    global BOTTOM_LEFT
    BOTTOM_LEFT = (0,0)
    global TOP_RIGHT
    TOP_RIGHT = tr
    global SOURCE
    SOURCE = src
    global TARGET
    TARGET = bp
    global DISTANCE
    DISTANCE = dist
    global BOTTOM_RIGHT
    BOTTOM_RIGHT = (TOP_RIGHT[0], BOTTOM_LEFT[1])
    global TOP_LEFT
    TOP_LEFT = (BOTTOM_LEFT[0], TOP_RIGHT[1])
    all_targets = get_targets(start_point = TARGET, distance = DISTANCE)
    CORNERS = [BOTTOM_LEFT, BOTTOM_RIGHT, TOP_LEFT, TOP_RIGHT]
    corner_angles = [4]
    i = 0
    while i < 4:
        ca = degrees(atan2(CORNERS[i][1] - SOURCE[1], CORNERS[i][0] - SOURCE[0]))
        corner_angles.append(ca)
        i = i+1
    valid_angles = set()
    for tgt in all_targets:
        pa = degrees(atan2(tgt[1] - SOURCE[1], tgt[0] - SOURCE[0]))
        if(tgt[0] - SOURCE[0] > 0 ):
            valid_angles.add(pa)
        elif(tgt[0] - SOURCE[0] < 0):
            if pa % 45 != 0 and pa not in corner_angles:
                valid_angles.add(pa)
        else:
            valid_angles.add(pa)
    if(src == bp):
        return 0
    else:
        return len(valid_angles)

def get_mirrored(point):
    ret = []
    x = point[0]
    y = point[1] - 2*(point[1] - TOP_RIGHT[1])
    ret.append((x,y))
    ret.append((point[0], point[1] - 2*(point[1] - BOTTOM_LEFT[1])))
    ret.append((point[0] - 2*(point[0] - BOTTOM_LEFT[0]), point[1]))
    ret.append((point[0] - 2*(point[0] - TOP_RIGHT[0]), point[1]))
    return ret

def get_targets(start_point, distance):
    targets = []
    targets.append(start_point)
    all_targets = set()
    all_targets.add((start_point[0],start_point[1]))
    last_targets = all_targets
    while True:
        new_level_targets = set()
        for tgt in last_targets:
            new_targets = get_mirrored(tgt)
            new_targets = set(t for t in new_targets if hypot(SOURCE[0] - t[0], SOURCE[1] - t[1]) <= DISTANCE)
            new_targets -= all_targets
            new_level_targets |= new_targets
        if not new_level_targets:
            break
        all_targets |= new_level_targets
        last_targets = new_level_targets
    return all_targets

print(answer((3,2), (1,1), (2,1), 4)) #Answer 7
print(answer((300,275), (150,150), (185,100), 500)) #Answer 9
