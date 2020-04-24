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
    for i in range(len(o_list)):
        new_list.append(max(o_list))
        o_list.remove(max(o_list))
    print(new_list)


sort_list(get_list())
