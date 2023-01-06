# 04.01.2023 Sergii Logosha sergiilogosha@gmail.com
# Last modified 06.01.2023

# Program performs basic calculations

from art import logo

def add(n1, n2):
    return n1 + n2

def subtr(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations_dict = {
    '+': add, 
    '-': subtr, 
    '*': mult, 
    '/': div,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operator in operations_dict:
        print(operator)
    
    
    more_calculations = True
    while more_calculations:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        
        calculations = operations_dict[operation_symbol](num1, num2)
        
        print(f'{num1} {operation_symbol} {num2} = {calculations}')
    
        continue_calculations = input(f'Type "y" to continue calculations with {num1}, or type "n" to start with new numbers: ')
        if continue_calculations == 'y':
            num1 = calculations
        else:
            more_calculations = False
            calculator()

calculator()
