# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 10:56:29 2019

@author: Jeffrey
"""

import re

def sign(a, b):
    return 0 if a==b else (a-b)/abs(a-b)
    
def parse_line(line):
    l = re.sub('<|>','',line)
    coords = l.split(', ')
    return tuple([int(c.split('=')[1]) for c in coords])

def apply_grav(vec, vecs):
    dim = len(vec)
    grav = [0]*dim
    for v in vecs:
        for i in range(dim):
            grav[i] += sign(vec)
    

def simulate(vecs, vels):
    for vecs in 
    

def main():
    with open('input.txt') as f:
        vecs_strs=f.readlines()
    vecs = list(map(parse_line, vec_strs))
    
    
if __name__=='__main__':
    main()
    