# 1
marks = {}
marks["John"] = [76, 65, 43]
marks["Mary"] = [68, 56, 74]
marks["Peter"] = [46, 55, 48]

# 2
marks["Ada"] = [56, 45, 65]

# 3
print(marks)
marks["Mary"][2] = 87
print(marks)
print()

# 4
del marks["Peter"]
print(marks)
print()


# 6
def showMarks(marks, name):
    if not marks[name]:
        print("{0} not found.".format(name))
    else:
        score = marks.get(name)
        print("Marks for " + name)
        print("Science:" + str(marks[name][0]))
        print("Math:" + str(marks[name][1]))
        print("English:" + str(marks[name][2]))


print(showMarks(marks, "Ada"))
print()


# 7
def showAllMarks(marks):
    print("Show all students marks")
    for name in marks:
        showMarks(marks, name)


showAllMarks(marks)
print()

# 8
for name in marks:
    score = marks[name][0]
    if int(score) > 50:
        print("{0} pass English Exam".format(name))
print()

# 9
Laptops = {
    "acer": 20,
    "hp": 10,
    "toshiba": 15,
    "apple": 12
}

fifteen_level = []
for i in Laptops:
    print("{0} : {1}".format(i, Laptops.get(i, 1)))
    if Laptops.get(i, 1) > 15:
        fifteen_level.append(i)

print("Brand that have laptop stock level of 15 or more:")
for i in fifteen_level:
    print(i)

total_lappy = 0
for i in Laptops:
    total_lappy += Laptops.get(i, 1)

print("Total number of laptop: {0}".format(total_lappy))
print()

# 10 why is the question sequence jumble up?
names = ["alan", "peter", "mary", "john"]
ages = [17, 18, 19, 20]
dict = {}

for x in range(len(names)):
    dict[names[x]] = ages[x]

print(dict)
