"""
CP1404/CP5632 Practical
List comprehensions
"""
def get_numbers(numbers):
    for x in range(0, 5):
        number = float(input("Number: "))
        numbers.append(number)


def basic_list_operation():
    numbers = []
    get_numbers(numbers)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    numbers_sum = sum(numbers)
    print(f"The average of the numbers is {numbers_sum/len(numbers)}")

basic_list_operation()


def inadequate_security_checker():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Enter Username: ")
    if username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


inadequate_security_checker()