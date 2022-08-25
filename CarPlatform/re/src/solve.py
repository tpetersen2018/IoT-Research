#!/usr/bin/python3

from z3 import *

v = []
for vn in 'abcdef':
    v.append(BitVec(vn, 32))

s = Solver()

for var in v:
    s.add(var > 47, var < 58)
s.add(54946352==(((((((((v[0]<<4)+v[1])<<4)+v[2])<<4)+v[3])<<4)+v[4])<<4)+v[5])

if str(s.check()) == 'sat':
    solution = 'FL'
    for var in v:
        solution += chr(s.model()[var].as_long())
        
    print("Valid license found: " + solution)
else:
    print('Z3 was unable to find a valid license given the constraints')
