# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

    # create a method that willl get the name and age
    def name_age_hyphen(self):
        return f'{self.name}-{self.age}'

    def name_age_tuple(self):
        return f'{self.name}, {self.age}'


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
a = [
    # print the human name
    human.name for human in humans
    # filter the name if it starts with d
    if human.name.startswith('D')
]
print('\nStarts with D:', a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
b = [
    # print the human name
    human.name for human in humans
    # filter the name if it starts with e
    if human.name.endswith('e')
]
print('\nEnds with e:', b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.

c = [
    # print the human name
    human.name for human in humans
    # filter the name if it starts with e
    if (human.name[0] >= 'C') and (human.name[0] <= 'G')
]
print('\nStarts between C and G, inclusive:', c)

# Write a list comprehension that creates a list of all the ages plus 10.
d = [
    human.age + 10 for human in humans
]
print('\nAges plus 10:', d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
e = [
    human.name_age_hyphen() for human in humans
]
print("\nName hyphen age:", e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.

f = [
    tuple([human.name, human.age])
    for human in humans if human.age >= 27 if human.age <= 32
]
print("\nNames and ages between 27 and 32:", f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
g = [
    Human(name=human.name.upper(), age=human.age+5) for human in humans
]
print("\nAll names uppercase:", g)

# Write a list comprehension that contains the square root of all the ages.
h = [
    math.sqrt(human.age) for human in humans
]
print("\nSquare root of ages:", h)
