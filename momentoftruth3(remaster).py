# 3
# each number is unique
resistorList = (75, 80, 90, 77, 88, 91, 60, 74, 73, 70, 55, 93, 59)


# order = ((73, 77), (70, 80), (59, 91), (60, 90))
# # order = (59, 93)
# print(len(order))


def matchResistors(L, R):
    new_list = []
    match_list = []

    for x in range(len(L)):
        for y in range(len(L)):
            order = ()
            if L[x] + L[y] == R and L[x] != L[y]:
                if L[x] > L[y]:
                    order = L[y], L[x]
                else:
                    order = L[x], L[y]
            if order:
                print(order)
                if order not in match_list:
                    if not match_list:
                        match_list.insert(-1, order)
                        break
                    # nice i discover this, so every loop it takes [0] as first and increase in position if larger
                    # until it finally finds it's spot and insert in
                    else:
                        position = 0
                        for i in range(len(match_list)):
                            # print(match_list[i][0], i, position)
                            if match_list[i][0] < order[0]:
                                position += 1
                            # if match_list[i][0] > order[0]:
                        match_list.insert(position, order)
    return tuple(match_list)


print(matchResistors(resistorList, 150))
print(matchResistors(resistorList, 152))
