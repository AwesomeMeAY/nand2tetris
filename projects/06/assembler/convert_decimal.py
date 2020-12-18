#!/bin/python
## returns a list of all powers of two close to the given number 
def calculate_nearest_exponents(num):
    power = 0
    exponent = 0 
    exponents = [1]
    while num > exponent:
        power += 1
        exponent = 2**power
        exponents.append(exponent)
    
    exponents.reverse()
    return exponents

def convert_to_binary(num):
    return_string = ''
    exponents = calculate_nearest_exponents(num)
    for i in exponents:
        return_string += str(num // i)
        num %= i
    return '0' * (16-len(return_string)) + return_string

if __name__ == '__main__': 
    for i in range(100):
        print(convert_to_binary(i))


