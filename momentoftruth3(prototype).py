# 3
# each number is unique
resistorList = (75, 80, 90, 77, 88, 91, 60, 74, 73, 70, 55, 93, 59)


def matchResistors(L, R):
    match_list = []
    for x in range(len(L)):
        for y in range(len(L)):
            if L[x] == L[y]:
                break
            if L[x] + L[y] == R:
                match_list.insert(-1, (L[x], L[y]))
                break
    return tuple(match_list)


print(matchResistors(resistorList, 150))
print(matchResistors(resistorList, 152))