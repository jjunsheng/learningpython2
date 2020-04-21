this_is_a_list = ["this", "is", "a", "list", 10]
this_is_a_dict = {
    "first": "this",
    "second": "is",
    "third": "a",
    "fourth": "dict",
    "fifth": 10
}

print(this_is_a_list)
print(this_is_a_dict)

fword = this_is_a_dict["first"]
# sword = this_is_a_dict["sixth"]
tword = this_is_a_dict.get("third")
print(fword)
print(tword)
# print(sword) # error
print(this_is_a_dict.get("sword"))

all_keys = this_is_a_dict.keys()
print(all_keys)
all_values = this_is_a_dict.values()
print(all_values)

for k in all_keys:
    v = this_is_a_dict.get(k)
    print("Key = {0}, Value = {1}".format(k, v))