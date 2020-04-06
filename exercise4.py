# 1
increasing = 4
decreasing = 2
i = 0
while i < 6:
    print(str(increasing * i + 3))
    i += 1
i = 0
print()

while i < 6:
    print(30 - decreasing * i)
    i += 1
print()

# 2
for i in range(0, 5):
    print(12 + i * 3)
print()

for i in range(0, 6):
    print(46 - i * 4)
print()

# 3
i = 1
while i <= 3:
    print("{0}) Hellow UoW!".format(i))
    i += 1
print()

# 4
x = 10
while x > 0:
    print('Countdown:' + str(x))
    print('Countdown:' + str(x - 1))
    print('Countdown:' + str(x - 2))
    x = x - 3

# count down from 10 to -1
for i in range(10, 0, -1):
    print('Countdown:' + str(i))

# 5
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

# 6
for i in range(0, 4):
    value = i * 3 + 1
    print("a = {}".format(value))
    if value % 2 == 0:
        print("even")
    else:
        print("odd")

7
i = 11
sum = 0
while i < 20:
    if i % 2 == 0:
        print("i = {0}".format(i))
        sum = sum + i
    i += 1
print("Total of even number is {0}.".format(sum))
print()

8
for i in range(0, 5):
    print("A|A|A|A|A|")
print()

for i in range(1, 6):
    print("+=" * i)
print()

for i in range(5, 0, -1):
    print("B|" * i)
print()

for i in range(1, 6):
    a = 6 - i
    print(":>" * a, end="  ")
    print(":P" * i)
print()

for i in range(1, 9):
    if i % 3 == 0:
        print()
    else:
        i = str(i)
        print(("{0})".format(i) * 5))
print()
