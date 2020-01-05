# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 16:01:50 2019

@author: Jeffrey
"""
from math import gcd
from math import atan2
from math import pi

with open('input.txt') as f:
    belt = f.readlines()
    
    
def inbounds(num, interval):
    return num >= interval[0] and num <= interval[1]

def inbounds2d(y,x,size):
    return inbounds(y, (0, size[0])) and inbounds(x, (0, size[1]))
    
def get_asteroid_locs(belt):
    locs = set()
    for y in range(len(belt)):
        for x in range(len(belt[y])):
            if belt[y][x] == '#':
                locs.add((y,x))
    return locs
      

def get_slope(starting_loc, loc):
    rise = loc[0] - starting_loc[0]
    run = loc[1] - starting_loc[1]
    # reduce to smallest integer step
    div = abs(gcd(rise, run))
    rise = rise / div
    run = run / div
    return rise, run
    

def detected(belt, locs, starting_loc, loc):
    size = (len(belt), len(belt[0]))
    rise, run = get_slope(starting_loc, loc)
    # cast out until we hit the end of the board. If we hit an asteroid
    # close to starting_loc than l, we don't count it
    y,x = starting_loc
    y += rise
    x += run
    while(inbounds2d(y,x,size) and (y,x) != loc):
        if (y,x) in locs:
            return False
        y += rise
        x += run
    return True
                
def get_num_detected(belt, locs, starting_loc):
    count = 0
    for l in locs:
        if l==starting_loc:
            continue

        count += detected(belt, locs, starting_loc, l)
    return count


def vaporize(belt, locs, starting_loc):
    remaining = locs.copy()
    vaporized_enum = {}
    cur_rank = 1
    if starting_loc in remaining:
        remaining.remove(starting_loc)
    while len(remaining) > 0:
        vaporized = [l for l in remaining if detected(belt, remaining, starting_loc, l)]
        relative = [(l[0] - starting_loc[0], l[1] - starting_loc[1]) for l in vaporized]
        angles = [atan2(l[1],-l[0]) for l in relative]
        angles = [a + 2*pi if a < 0 else a for a in angles]
        sorted_angles = sorted(zip(vaporized, angles), key=lambda x: x[1])
        for loc,_ in sorted_angles:
            vaporized_enum[cur_rank] = loc 
            cur_rank += 1
        remaining.difference_update(set(vaporized))
    return vaporized_enum
    
locs2 = get_asteroid_locs(belt)

mdetected = 0
mloc = (0,0)
for l in locs2:
    ndetect = get_num_detected(belt, locs2, l)
    if ndetect > mdetected:
        mdetected = ndetect
        mloc = l
    
out= vaporize(belt, locs2, mloc)
ans2 = out[200]
print(ans2[1]*100 + ans2[0])
