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

# 7
