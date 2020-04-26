# 2
thistuple = (1, 2, 3, 4, 5, 6, 8, 9, 1)
thislist = (1, 2, 3, 4, 5, 6, 8, 9, 1)
# print(len(thistuple))
# print(len(thislist))
# print(thistuple[0])
# print(thislist[0])
# for n in range(len(thislist)):
#     print(thislist[n])
# for n in range(len(thistuple)):
#     print(thistuple[n])


def findSmallest4(L):
    onelist = []
    for n in range(len(L)):
        count = 0
        for x in range(len(L)):
            if L[n] < L[x]:
                count += 1
        if count > 4:
            onelist.append(L[n])
    one_tuple = tuple(onelist)
    return one_tuple


print(findSmallest4([5, 3, 2, 6, 7, 8, 1, 99]))
print(findSmallest4((1, 2, 3, 4, 5, 6, 8, 9, 1)))

# so problem comes in, i need to sort the number with using one list and one tuple
# also is a wrong way to calculate this, haha no cheat way is it
# gonna try "register" each number and count before adding to list do it will also auto stop at 4