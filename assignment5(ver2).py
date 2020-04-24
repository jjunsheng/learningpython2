# 1
def get_list():
    n_list = []
    length = int(input("Enter the length of the list: "))
    for i in range(length):
        number = int(input("Enter the list element: "))
        n_list.append(number)
    return n_list


# print(get_list())
# print()

# 2
def sort_list(n_list):
    o_list = n_list
    new_list = []
    for i in range(len(o_list), 0, -1):
        highest = o_list[0]
        for x in range(i):
            if o_list[x] > highest:
                highest = o_list[x]
        new_list.append(highest)
        o_list.remove(highest)
    print(new_list)


sort_list(get_list())