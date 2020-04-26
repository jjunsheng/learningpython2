# 1
from math import pi


def myCos(angle, k):
    sum_k = 1.0
    for n in range(1, k):
        upper = (-1 ** n) * (angle ** (2* n))
        lower = 0
        for i in range(1, n + 1):
            lower += i
        answer = upper / lower
        print(sum_k, answer, upper, lower)
        if n % 2 == 0:
            sum_k += answer
        else:
            sum_k -= answer
    return sum_k


print("myCos(0, 5)")
print(myCos(0, 5))
print("myCos(45, 1)")
print(myCos(45, 1))
# print("myCos(45, 2)")
# print(myCos(45, 2))
print("myCos(45, 3)")
print(myCos(45, 3))
# print("myCos(45, 10)")
# print(myCos(45, 10))
# print("myCos(60, 1)")
# print(myCos(60, 1))
# print("myCos(60, 80)")
# print(myCos(60, 80))
# print("myCos(90, 80)")
# print(myCos(90, 80))
# print()

# gg lol