def factorial(n):
    # basic steps
    if n == 1:
        return 1
    # recursive factorial function
    else:
        return n * factorial(n-1)


print(factorial(4))
for i in range(1,10):
    print("{0}! = {1}".format(i, factorial(i)))


def fibonacci(n):
    # basic
    if n == 0:
        return 0
    # basic
    elif n == 1:
        return 1
    # recursive
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(1,10):
    print("fibonacci({0}) = {1}".format(i, fibonacci(i)))