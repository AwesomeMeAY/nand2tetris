#!/bin/env python
# Not official nand2tetris software
# Created by JustJojo

# Formula for the amount of combinations is s**v
# s being the amount of states a variable has
# and v being the amount variables 

# Best way to find the different combinations is counting in base s
# if s=2 then we count in binary or if s=4 then we count in base 4

from sys import argv

def calculate_nearest_exponent(num,s):
    array = [1]
    power = 0
    exponent = 0
    while num > exponent:
        power += 1
        exponent = s**power
        array.append(exponent)

    array.reverse()
    return array

def convert_to_base(num,exponents):
    return_string = ''
    for i in exponents:
        return_string += str(num//i)
        num %= i
    return return_string
def run_program(s, v):
    for i in range(s**v):
        n = convert_to_base(i,calculate_nearest_exponent(i,s))
        while v > len(n):
            n = '0' + n
        while len(n) > v:
            n = n[1:]
        yield n
if __name__ == '__main__':
    s = int(argv[1])
    v = int(argv[2])
    for i in run_program(s,v):
        print(i)
        
            
