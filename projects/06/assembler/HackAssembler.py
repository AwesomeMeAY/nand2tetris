#!/bin/python
import sys
from convert_decimal import convert_to_binary

# Returns a list of the program without useless lines
def clean_program(program):
    # Get rid of comments and empty lines
    return_lst = []
    for line in program:
        if line != '\n':
            # If '//' in line then get rid of everything after it 
            try:
                comment_less_line = line[:line.index('//')]
                if comment_less_line != '':
                    return_lst.append(comment_less_line.replace('\n', '').strip())
            except ValueError:
                return_lst.append(line.replace('\n', '').strip())
    return return_lst

def parser(program):
    for program_line in program:
        if '(' in program_line:
            continue
        # If A instruction: 
        if program_line[0] == '@':
            output_program.writelines([convert_to_hack(instruction_type=0, address=program_line[1:]), '\n'])
            continue
        # If C instruction:
        # Splits instruction into dest, comp, and jump
        program_line = program_line.replace('=', ' ').replace(';', ' ').split()
        try:
            # Need to remove comp because comp and dest can have same values
            if program_line[1] not in binary_jumps:
                comp = program_line.pop(1)
            else:
                comp = program_line.pop(0)
            if program_line[0] in binary_destinations:
                dest = program_line.pop(0)
            else:
                dest = 'null'
            if program_line:
                jump = program_line.pop(0)
            else:
                jump = 'null'
            output_program.writelines([convert_to_hack(comp=comp, dest=dest, jump=jump), '\n'])
        # If program_line has only one item in it then it will be comp
        except IndexError:
            print('One singular computation, no jumps or anything')
            output_program.writelines([convert_to_hack(comp=program_line[0], dest='null', jump='null'), '\n'])
        
    

# Defaults to C instruction 
# If an argument is -1 it is not used
def convert_to_hack(instruction_type=1, address=-1, comp=-1, dest=-1, jump=-1):
    if instruction_type:
        return f'{instruction_type}11{binary_instructions[comp]}{binary_destinations[dest]}{binary_jumps[jump]}'
    # If A instruction 
    # Check if it is a know symbol
    if address in symbols:
        return f'{instruction_type}{symbols[address]}'
    # Check if it is an integer or an unknown symbol
    try:
        machine_code = f'{instruction_type}{convert_to_binary(int(address))[1:]}'
        return machine_code
    # If unknown symbol:
    except ValueError:
        used_registers.append(used_registers[-1] + 1)
        symbols[address] = convert_to_binary(used_registers[-1])[1:]
        return f'{instruction_type}{symbols[address]}'

# line_number should be the next Line Number in binary 
def label_handler(program_line, line_number):
    if program_line[0] == '(':
        symbols[program_line[1:program_line.index(')')]] = line_number
        return True


if __name__ == '__main__':
    assembly_program = open(sys.argv[1]).readlines()
    output_program = open(f"{sys.argv[1].replace('.asm', '.hack')}", 'w')

    # Setting symbols
    symbols = {'SCREEN':convert_to_binary(16384)[1:], 'KBD':convert_to_binary(24576)[1:]}
    for i in range(16):
        symbols[f'R{i}'] = f'{convert_to_binary(i)[1:]}'

    used_registers = [15]

    # Searching a dictionary is faster than a conditionals
    binary_instructions = {'0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100', 'A':'0110000',
                           '!D':'0001101', '!A':'0110001', '-D':'0001111', '-A':'0110011', 'D+1':'0011111',
                           'A+1':'0110111', 'D-1':'0001110', 'A-1':'0110010', 'D+A':'0000010', 'D-A':'0010011',
                           'A-D':'0000111', 'D&A':'0000000', 'D|A':'0010101', 'M':'1110000', '!M':'1110001',
                           '-M':'1110011', 'M+1':'1110111', 'M-1':'1110010', 'D+M':'1000010', 'D-M':'1010011',
                           'M-D':'1000111', 'D&M':'1000000', 'D|M':'1010101'}

    binary_destinations = {'null':'000', 'M':'001', 'D':'010', 'MD':'011', 'A':'100', 'AM':'101', 'AD':'110', 'AMD':'111'}

    binary_jumps = {'null':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'}

    # Main():
    line_number = 0 
    cleaned_program = clean_program(assembly_program)
    for line in cleaned_program:
        if label_handler(line, convert_to_binary(line_number)[1:]):
            continue
        line_number += 1
    parser(cleaned_program)
        
