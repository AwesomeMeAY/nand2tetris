#!/bin/python
import sys
from convert_decimal import convert_to_binary

assembly_program = open(sys.argv[1]).readlines()

# Setting symbols
symbols = {'SCREEN':convert_to_binary(16384)[1:], 'KBD':convert_to_binary(24576)[1:]}
for i in range(16):
    symbols[f'R{i}'] = f'{convert_to_binary(i)}'
print(symbols)

## Searching a dictionary is faster than a conditional "if 'A' in comp then a_bit = 0"
binary_instructions = {'0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100', 'A':'0110000',
                       '!D':'0001101', '!A':'0110001', '-D':'0001111', '-A':'0110011', 'D+1':'0011111',
                       'A+1':'0110111', 'D-1':'0001110', 'A-1':'0110010', 'D+A':'0000010', 'D-A':'0010011',
                       'A-D':'0000111', 'D&A':'0000000', 'D|A':'0010101', 'M':'1110000', '!M':'1110001',
                       '-M':'1110011', 'M+1':'1110111', 'M-1':'1110010', 'D+M':'1000010', 'D-M':'1010011',
                       'M-D':'1000111', 'D&M':'1000000', 'D|M':'1010101'}
binary_destinations = {'null':'000', 'M':'001', 'D':'010', 'MD':'011', 'A':'100', 'AM':'101', 'AD':'110', 'AMD':'111'}
binary_jumps = {'null':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'}

## Recursivly reads over a file and gets rid of comments and new lines
def recurse_over_file(program):
    for line in program:
        ## Get rid of comments and empty lines
        if '//' in line or line == '\n':
            continue

        # Get rid of new lines in non-empty lines
        yield line.replace('\n','')

def parser(program_line):
    ## If A instruction:
    if program_line[0] == '@':
        return convert_to_hack(instruction_type=0, address=program_line[1:])

    ## If C instruction:
    ## Splits instruction into dest, comp, and jump
    program_line = program_line.replace('=', ' ').replace(';', ' ').split()
    
    try:
        ## Need to remove comp because comp and dest can have same values
        if program_line[1] not in binary_jumps:
            comp = program_line.pop(1)
        else:
            comp = program_line.pop(0)
        ## If any item in program_line is in binary_destinations:
        if any(i in program_line for i in binary_destinations):
            ## If dest in program_line then it will be at index 0
            dest = program_line[0]
        else:
            dest = 'null'
        ## Have to do it the bloat way because jump could be at index 0 or 1
        for i in program_line:
            if i in binary_jumps:
                jump = i
        else:
            jump = 'null'
        return convert_to_hack(comp=comp, dest=dest, jump=jump)
    ## If program_line has only one item in it then it will be comp
    except IndexError:
        return convert_to_hack(comp=binary_instructions[program_line[0]], dest='null', jump='null')
        
    

## Defaults to C instruction 
## If an argument is -1 it is not used
def convert_to_hack(instruction_type=1, address=-1, comp=-1, dest=-1, jump=-1):
    if instruction_type:
        return f'{instruction_type}11{binary_instructions[comp]}{binary_destinations[dest]}{binary_jumps[jump]}'
    ## If A instruction 
    ## Check if it is a know symbol
    if address in symbols:
        return f'{instruction_type}{symbols[address]}'
    ## Check if it is an integer or an unknown symbol
    try:
        return f'{instruction_type}{convert_to_binary(int(address))[1:]}'
    except ValueError:
        pass    

## Line number is in binary
def label_handler(program_line, line_number):
     

for i in recurse_over_file(assembly_program):
    print('i', i)
    print(parser(i))
