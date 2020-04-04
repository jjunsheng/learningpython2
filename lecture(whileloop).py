# while loop
i = 0
while i < 10:
    print(i)
    i += 1

i = 0
while i < 10:
    print("(0) x {1} = {2}".format(i, 5, 5 * i))
    i += 1

i = 0
while i <= 10:
    print("{0:>2} + {1:>2} = {2:>2}".format(i, 10 - i, 10))
    i += 1

i = 0
while i <= 10:
    if i % 2 == 0:
        print(i, end="")
        if i < 10:
            print(", ", end="")
        else:
            print(end=".")
    i += 1

print()

i = 0
while (i <= 10):
    print(i, end="")
    if (i < 10):
        print(", ", end="")
    else:
        print(".")
# omg you can do this
    i += 2

while True:
    user_input = input("Key in something (or press q to quit): ")
    if user_input =="q":
        break
    print("You have entered: " + user_input)

