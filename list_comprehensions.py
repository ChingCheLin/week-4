"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

first_initials = [name[0] for name in names]
print(first_initials)

full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

a_names = [name for name in names if name.startswith('A')]
print(a_names)


# in lowercase format
lowercase_full_names = []
for names in full_names:
    lowercase_full_names.append(names.lower())
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = []
for number in almost_numbers:
    numbers.append(int(number))
print(numbers)

numbers_greater_than_9 = []
for number in numbers:
    if number > 9:
        numbers_greater_than_9.append(number)
print(numbers_greater_than_9)