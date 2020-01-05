# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:05:15 2019

@author: Jeffrey
"""

from itertools import permutations

class Intcode:
    
    def __init__(opcodes):
        self.i = 0
        self.opcodes = opcodes
        self.outputs = []

def get_params(pcode, num):
    params = []
    for _ in range(num):
        params.append(pcode%10)
        pcode = pcode // 10
    return params
        
def get_arg_length(instr):
    if instr in [1,2,7,8]:
        return 3
    elif instr in [5,6]:
        return 2
    return 1
        
def get_args(opcodes, pos, nargs):
    args = []
    pos += 1
    for i in range(nargs):
        args.append(opcodes[pos+i])
    return args
    
        
def param_mode_val(pmode, a, opcodes):
    if pmode == 0:
        return opcodes[a]
    else:
        return a
    
def param_mode_vals(pmodes, params, opcodes):
    out = []
    for p,v in zip(pmodes,params):
        out.append(param_mode_val(p,v,opcodes))
    return out

def run_vm(opcodes, inputs):
    i = 0
    outputs = []
    inputs.reverse()
    while opcodes[i] != 99:
        instr = opcodes[i] % 100
        if instr==99:
            break
        pcode = opcodes[i] // 100
        nargs =get_arg_length(instr)
        args = get_args(opcodes, i, nargs)
        params = get_params(pcode, nargs)
        
        vals = param_mode_vals(params, args, opcodes)
        print(f'{i}, {instr}, {params}, {args}, {vals}')
        if instr == 1:
            a,b,c=vals
            opcodes[args[2]] = a+b
        elif instr==2:
            a,b,c = vals
            opcodes[args[2]] = a*b
        elif instr==3:
            a, = vals
            opcodes[args[0]] = inputs.pop()
        elif instr==4:
            a, = vals
            outputs.append(a)
        elif instr==5:
            a,b = vals
            if a != 0:
                i = b
                continue
        elif instr== 6:
            a,b = vals
            if a  == 0:
                i = b
                continue
        elif instr == 7:
            a,b,c = vals
            opcodes[args[2]] = int(a<b)
        elif instr== 8:
            a,b,c = vals
            opcodes[args[2]] = int(a==b)
        else:
            print('unknown opcode')
            raise
        i+=nargs+1
    return outputs

with open('test.txt') as f:
    inp = f.readline()
opcodes = [int(s) for s in inp.split(',')]
run_vm(opcodes, [0])
# part 1
signalm = 0
for perm in permutations(range(0,5)):
    signal = 0  
    for phase in perm:
        opc = opcodes.copy()
        #print('starting')
        signal, = run_vm(opc, [phase, signal])
    signalm = max([signal, signalm])
print(signalm)
    

#part 2
opcodes=[3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
for perm in permutations(range(5,10)):
    states = [opcodes.copy() for i in range(0, 5)]
    outputs = [0 for i in range(0, 5)]
    perm = [9,8,7,6,5]
    for i,phase in enumerate(perm):
        outputs[i]=run_vm(states[i], [phase, outputs[i-1]])
    print(outputs)
    