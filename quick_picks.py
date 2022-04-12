"""
CP1404/CP5632 Practical
Quick Picks
"""
import random

def main():
    number_of_quick_picks = int(input("How many quick picks?: "))
    for x in range (0,number_of_quick_picks):
        numbers = quick_picks()
        for x in range(0,len(numbers)):
            print(numbers[x], end=" ")
        print()

def verify_quick_picks(random_number, numbers):
    """Verify the quick pick number validity"""
    while True:
        if random_number in numbers:
            random_number = random.randint(1, 45)
        else:
            return random_number

def quick_picks():
    numbers = []
    for x in range(1, 7):
        random_number = random.randint(1, 45)
        random_number = verify_quick_picks(random_number, numbers)
        numbers.append(random_number)
    return numbers

main()