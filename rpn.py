#!/usr/bin/env python3

import readline
from termcolor import colored

def calculate(arg):
    stack = []

    tokens = arg.split()
    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            # if there is a problem, its probably because the thing is an op
            val2 = stack.pop()
            val1 = stack.pop()

            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val1 - val2
            elif token == '*':
                result = val1 * val2

            stack.append(result)
            if len(stack) > 1:
                raise ValueError('Too many arguments on the stack')
    return stack[0]

def main():
    while True:
        try:
            result = calculate(input('rpn calc> '))
            if (result >= 0):
                print(colored(result, 'green'))
            else:
                print(colored(result, 'yellow'))
        except ValueError:
            # we need to allow the valueerror exception to let the code proceed
            pass



if __name__ == '__main__':
    main()


