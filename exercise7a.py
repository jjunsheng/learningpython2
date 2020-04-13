# 1
a = "John Peter"
alist = a.split(" ")
print(len(a))
print(a[0])
print(a[8])
# print(a[9])
print(type(a))
print(type(alist))
print(alist)
print(alist[0])
print(alist[1])
print(alist[-1])
print(alist[-2])
# print(alist[3])
print((alist[0].split("h"))[0])
print((alist[0].split("h"))[1])
print(len(alist))

# 2
namelist = ["John", "Peter"]
for i in range(len(namelist)):
    print(namelist[i])

for i in (range(len(namelist) - 1, -1, -1)):
    print(namelist[i])
for i in range(5, 10, 2):
    print(i)
