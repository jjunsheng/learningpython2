a = 28.123456789

print(round(a))
print(round(a, 1))
print(round(a, 2))
print(round(a, 3))
print(round(a, 4))
print(round(a, 5))
print(round(a, 6))
print(round(a, 7))
print(round(a, 8))
print(round(a, 9))

a = 1.5
b = 5
c = 3

d = min(a, b, c)
e = max(a, b, c)
print(d)
print(e)

import random

for i in range(0, 10):
    r = random.randint(1, 6)
    print("Dice result: {0}".format(r))


def sum_of_two_numbers(n1, n2):
    s = n1 + n2
    return s


a = 2
b = 3
c = sum_of_two_numbers(a, b)
print(c)


def say_hi(name):
    print("Hi {0}!".format(name))


j = "John"
say_hi(j)

say_hi("Bob")
say_hi("Alicia")


def ask_info():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return first_name, last_name

u1_fname, u1_lname = ask_info()
print("User 1: {0} {1}".format(u1_fname, u1_lname))
u2_fname, u2_lname = ask_info()
print("User 2: {0} {1}".format(u2_fname, u2_lname))

