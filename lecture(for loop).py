# for loop
# recall that range 0 to 10, they always dont count the last "type" number
for i in range(0, 10):
    print(i)

for i in range(1, 10):
    print("{0} x {1} = {2}".format(i, 5, 5 * 1))

for i in range(0, 11):
    print("{0} + {1} = {2}".format(i, 10 - i, 10))

for i in range(0, 11):
    print(i, end="")
    if i < 10:
        print(", ", end="")
    else:
        print(".")

# understanding how end= works, usually to make it print back on the same line
print("something")
print("something", end="")
print("something", end=".")
print("something", end="blah")
print()

# count event numbers
for i in range(0,11):
    if i % 2 == 0:
        print(i, end="")
        if i < 10:
            print(", ", end="")
        else:
            print(".")

sum = 0
for i in range(0,11):
    sum += i
print(sum)

