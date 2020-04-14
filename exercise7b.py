# 4
names = ['alan', 'peter', 'john']
names.append('mary')
print(names)
names.insert(0, 'bob')
print(names)
names.remove('peter')
print(names)
names.remove(names[1])
print(names)
print(len(names))
print()

# 5
sentence = "Dell profit surges on revived business spending in 2014"
words = sentence.split()
print(words)
print(len(words))
output = ""
for i in range(len(words)):
    print(i, words[i])
    wanted = [0, 4, 5, 7, 8]
    if i in wanted:
        output += words[i] + " "
print(output)
print(len(words))

# 6
animals = "fish cat dog lion tiger mouse cow"
names = animals.split()
print(names)
for i in names:
    print(i)
print()

for i in range(len(names)):
    if len(names[i]) == 4:
        print(names[i])

7
numberList = [14, 22, 28]


def divisible_7(list):
    count = 0
    output_list = []
    output_string = ""
    for i in range(len(list)):
        if list[i] % 7 == 0:
            count += 1
            output_list.append(list[i])
            # lol i forget can use the end=
            output_string += str(list[i]) + " and "
    print(output_string[0:-4] + "are both divisible by 7")
    print(count)
    print(output_string)


divisible_7(numberList)
print()

# 8
num_list = list(range(0, 33, 4))
print(num_list)
sum = 0
for i in num_list:
    sum = sum + i
print(sum)

# 9
num_list = list(range(0, 35, 3))
sum = 0
for i in num_list:
    if i % 2 == 0:
        sum = sum + i
print(sum)

# 10
num_list = list(range(0, 35, 3))
count = 0
for i in num_list:
    if i % 2 == 0:
        count += 1
print(count)

# 11
name_input = input("Key in your name: ")


def calculate_lucky_number(name):
    namelist = name.split()
    print(namelist)
    F = len(namelist[0])
    S = len(namelist[1])
    T = len(namelist[2])
    lucky_number = (2 * F + S) % 10 + T
    return lucky_number


print(calculate_lucky_number(name_input))


# 12
def calculate_average(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + i
    average = sum / len(list)
    return average


list = [1, 2, 3, 4, 5, 6, 7, 8]
print(calculate_average(list))
print()


# 13
def calculate_population_stddev(list):
    average = calculate_average(list)
    stddev_total = 0
    for i in range(len(list)):
        stddev_individual = (list[i]-average) ** 2
        stddev_total += stddev_individual
        # print(stddev_individual, stddev_total)
    mean_stddev = stddev_total / len(list)
    stddev = mean_stddev ** 0.5
    print(stddev)


calculate_population_stddev(list)
print()


def calculate_population_stddev1(num_list):
    avg = calculate_average(num_list)
    count = 0
    total = 1
    for num in num_list:
        count = (num - avg) ** 2 + count
    stddev = count / len(num_list)
    return stddev ** 0.5


print(calculate_population_stddev1(list))
