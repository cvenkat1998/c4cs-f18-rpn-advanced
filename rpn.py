#!/usr/bin/env python3

import operator
from termcolor import colored

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
            if (arg1%2 == 0):
                print(colored(arg1, 'red'))
            else:
                print(colored(arg1, 'green'))

            print(colored(token, 'blue'))

            if (arg2%2 == 0):
                print(colored(arg2, 'red'))
            else:
                print(colored(arg2, 'green'))
            
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def printHello():
    print("Hello")


def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
