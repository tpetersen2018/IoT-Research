#!/usr/bin/python3

from z3 import *

v = []
for vn in 'abcdef':
    v.append(BitVec(vn, 32))

s = Solver()

for var in v:
    # Constraints to be applied to every character go here
    
    # # #
    
# More constraints may be added outside of the for loop

# # #

if str(s.check()) == 'sat':
    solution = 'FL'
    for var in v:
        solution += chr(s.model()[var].as_long())
        
    print("Valid license found: " + solution)
else:
    print('Z3 was unable to find a valid license given the constraints')
