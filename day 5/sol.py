# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:05:15 2019

@author: Jeffrey
"""

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

def run_vm(opcodes):
    i = 0
    while opcodes[i] != 99:
        instr = opcodes[i] % 100
        pcode = opcodes[i] // 100
        nargs =get_arg_length(instr)
        args = get_args(opcodes, i, nargs)
        params = get_params(pcode, nargs)
        vals = param_mode_vals(params, args, opcodes)
        if instr == 1:
            a,b,c=vals
            opcodes[args[2]] = a+b
        elif instr==2:
            a,b,c = vals
            opcodes[args[2]] = a*b
        elif instr==3:
            a, = vals
            opcodes[args[0]] =5
        elif instr==4:
            a, = vals
            print(opcodes[args[0]])
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

with open('input.txt') as f:
    inp = f.readline()
opcodes = [int(s) for s in inp.split(',')]
run_vm(opcodes)
    