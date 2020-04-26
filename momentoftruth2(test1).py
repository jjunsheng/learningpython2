def findSmallest4(L):
    only_list = []
    smallest = min(L)
    # insert the number times of smallest
    for i in range(L.count(smallest)):
        only_list.insert(0, smallest)
    # up to 4 loops
    for x in range(4 - len(only_list)):
        # using this as benchmark cause i tried to use None then cannot use > to compare
        next_smallest = max(L)
        similar_count = 1
        for y in range(len(L)):
            if next_smallest >= L[y] > only_list[0]:
                next_smallest = L[y]
                similar_count = 1
            elif next_smallest == L[y]:
                similar_count += 1
        # print(next_smallest, similar_count)
        for j in range(similar_count):
            # adding the next smallest number to left # sorting*
            only_list.insert(0, next_smallest)
    only_tuple = tuple(only_list)
    return only_tuple


print(findSmallest4([5, 3, 2, 6, 7, 8, 1, 99]))
print(findSmallest4((1, 2, 3, 4, 5, 6, 8, 9, 1)))
# print(findSmallest4((1, 2, 5, 3, 9)))
