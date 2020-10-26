#!/bin/python
# Build test script for other chips you might want to build
# Not offical nand2tetris software
# Created by AwesomeMeAY

from combinations_generator import run_program as bit_calculator

def request():
    # get list of input and output variables
    return input("Please name your input variables (Space in between them): ").split(), input("Please name your output variables (Same as last time): ").split()
# Pack two lists together
def pack_lists(lst1, lst2):
        x = 0
        for i in lst1:
            yield i, lst2[x]
            x += 1
def write_file(inputs, outputs):
    # Write the first part of the tst files
    title = input("What is the name of your file? (No file extensions): ")
    with open(f"{title}.tst", 'w') as tstfile:
        tstfile.write(f"load {title}.hdl, output-file {title}.out,\n")
        output_list = "output-list"
        for var in inputs + outputs:
            output_list += f' {var}%B3.1.3'
        tstfile.write(output_list + ";")
        for i in bit_calculator(2, len(inputs)):
            for var, bit in pack_lists(inputs, i):
                tstfile.write(f"set {var} {bit}, \n")
            tstfile.write("eval, \noutput;\n\n\n")
        
if __name__ == '__main__':
    x, y = request()
    write_file(x,y) 


        
