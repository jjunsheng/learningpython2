list1 = []
list2 = [1, 4, 4, 10, -1]
list3 = [1, "hi there", True, 10, "john"]
print(list1)
print(list2)
print(list3)
print()

list1_length = len(list1)  # → 0
list2_length = len(list2)  # → 5
list3_length = len(list3)  # → 5

print("list3 has {0} items".format(list3_length))
print("list3 has {0} items".format(len(list3)))
print()

print(list3[0])  # → 1
print(list3[1])  # → "hi there"
print(list3[2])  # → True
print(list3[3])  # → 10
print(list3[4])  # → "john

for i in range(0, len(list3)):
    print(list3[i])
print()

list3[0] = 3
list3[1] = 4
list3[2] = 5
list3[3] = 6
list3[4] = 7
print(list3)
print()

list2 = [1, 4, 4, 10, -1]
for i in range(0, len(list2)):
    list2[i] = list2[i] + 10
print(list2)   # → [11, 14, 14, 20, 9]

# delete
del list2[1]
print(list2)

#remove, only remove the first appearance
list2 = [1, 4, 4, 10, -1]
list2.remove(4)
list2.remove(10)
# list2.remove(5)

list2 = [1, 4, 4, 10, -1]
four_count = list2.count(4)  # → 2
ten_count = list2.count(10)  # → 1
five_count = list2.count(5)  # → 0

four_index = list2.index(4)  # → 1
ten_index = list2.index(10)  # → 3
# five_index = list2.index(5)  # ValueError: 5 is not in the list

list2.sort()
print(list2)
list2.reverse()
print(list2)
list2.clear()
print(list2)

# lol you can add list
list2 = [1, 4, 4, 10, -1]
list4 = [10, 7, 5]
# adding two lists
list5 = list2 + list4 # now list5 = [1, 4, 4, 10, -1, 10, 7, 5]
list6 = list4 + list2 # now list6 = [10, 7, 5, 1, 4, 4, 10, -1]
# multiply a list
list7 = list4 * 3 # now list7 = [10, 7, 5, 10, 7, 5, 10, 7, 5

# empty list
square = []
for i in range(0, 10):
    # in square list add i*i
    square.append(i*i)
print(square)

# Fibonacci
fibo = []
print(fibo)

fibo.append(0)
print(fibo)

fibo.append(1)
print(fibo)

for i in range(2, 5):
    new = fibo[i-1] + fibo[i-2]
    fibo.append(new)
print(fibo)
