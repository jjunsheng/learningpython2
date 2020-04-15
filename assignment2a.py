# 1
p1 = input("Enter the first phone model: ")
b1 = input("Enter the first phone brand: ")
p2 = input("Enter the second phone model: ")
b2 = input("Enter the second phone brand: ")
p3 = input("Enter the third phone model: ")
b3 = input("Enter the third phone brand: ")

print("{0:<20}{1:<20}".format("Model", "Phone"))
print("{0:<20}{1:<20}".format(p1, b1))
print("{0:<20}{1:<20}".format(p2, b2))
print("{0:<20}{1:<20}".format(p3, b3))
print()

# 2
number = input("Enter the first number: ")
n = int(number)

if n % 2 == 0:
    n2 = n // 2
else:
    n2 = 3 * n + 1

if n2 % 2 == 0:
    n3 = n2 // 2
else:
    n3 = 3 * n2 + 1

if n3 % 2 == 0:
    n4 = n3 // 2
else:
    n4 = 3 * n3 + 1

if n4 % 2 == 0:
    n5 = n4 // 2
else:
    n5 = 3 * n4 + 1

if n == 1:
    print("The sequence is : 1.")
elif n2 == 1:
    print("The sequence is: " + str(n) + ", 1.")
elif n3 == 1:
    print("The sequence is : " + str(n) + ", " + str(n2) + ", 1.")
elif n4 == 1:
    print("The sequence is : " + str(n) + ", " + str(n2) + ", " + str(n3) + ", 1.")
else:
    print("The sequence is : " + str(n) + ", " + str(n2) + ", " + str(n3) + ", " + str(n4) + ", 1.")
print()

if n == 1:
    print("The sequence is : 1.")
elif n2 == 1:
    print("The sequence is : {0}, 1.".format(n))
elif n3 == 1:
    print("The sequence is : {0}, {1}, 1.".format(n, n2))
elif n4 == 1:
    print("The sequence is : {0}, {1}, {2}, 1.".format(n, n2, n3))
else:
    print("The sequence is : {0}, {1}, {2}, {3}, 1.".format(n, n2, n3, n4))
print()

# 3
n = int(input("Enter an integer: "))
if n > 0:
    print("The number entered is positive.")
elif n < 0:
    print("The number is negative.")
else:
    print("The number is 0.")

if n % 2 == 0:
    print("The number entered is even.")
else:
    print("The number is odd.")
if n % 11 == 0:
    print("The number entered is divisible by 11.")
else:
    print("The number entered is not divisible by 11. The remainder when divided by 11 is {0}.".format(str(n % 11)))
if n % 15 == 0:
    print("The number entered is divisible by 15.")
else:
    print("The number entered is not divisible by 15. The remainder when divided by 15 is {0}.".format(str(n % 15)))
print()

