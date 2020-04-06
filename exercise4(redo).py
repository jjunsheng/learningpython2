# 1
i = 0
while i <= 23:
    print(i + 3)
    i += 4
print()

i = 30
while i >= 20:
    print(i)
    i -= 2
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
    print("{0}) Hello UoW!".format(i))
    i += 1
print()

# 4
x = 10
while x > 0:
    print('Countdown: ' + str(x))
    print('Countdown: ' + str(x - 1))
    print('Countdown: ' + str(x - 2))
    x = x - 3
print()

for i in range(10, -2, -1):
    print("Countdown: " + str(i))
print()

# 5
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print(total)
print()

# 6
for i in range(0, 4):
    a = 1 + i * 3
    print("a = {0}".format(a))
    if a % 2 == 0:
        print("even")
    else:
        print("odd")
print()

# 7
i = 12
total = 0
while i < 20:
    print("i = {0}".format(i))
    total = total + i
    i += 2
print(f"Total of even numbers is {total}")
print()

# 8
for i in range(1, 100):
    if i % 2 != 0:
        total += i
print("Sum of odd numbers from 1 to 100 is {0}".format(total))
print(f"Sum of odd numbers from 1 to 100 is {total}")
print()

# 9
for i in range(5):
    print("A|A|A|A|A|")
print()

for i in range(1, 6):
    print("+=" * i)
print()

for i in range(5):
    print("B|" * (5 - i))
print()

for i in range(1, 6):
    print(":>" * (6 - i) + "  " + ":P" * i)
print()

for i in range(1, 9):
    if i % 3 != 0:
        print(f"{i})" * 5)
    else:
        print()
