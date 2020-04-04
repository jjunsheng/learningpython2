# concatenating strings
string = "hello" + " world"
print(string)

# multiplicative concatenation
string = "junsheng" * 3
print(string)

# concatenation non strings
string = "Chicken Rice = " + str(3)
print(string)

# comparing strings, is OR ==
string1 = "Jun"
string2 = "Sheng"
if string1 == string2:
    print("The string are equal value.")
else:
    print("The string are not equal value.")


# looking for a substring
string1 = "My name is Jun Sheng"
print("Jun" in string1)
print("SIT" in string1)

# finding the index of a sub string
print(string1.find('Jun'))
print(string1.find('jun'))

# finding a substring after a certain arrangement
print(string1.find('My', 4))

# TBC