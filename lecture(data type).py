greeting = "Hi there!"
greeting_length = len(greeting)  # → 9
print(len(greeting))
print(greeting[0])  # → H
print(greeting[1])  # → i
print(greeting[2])  # → space
print(greeting[3])  # → t
print(greeting[4])  # → h
print(greeting[5])  # → e
print(greeting[6])  # → r
print(greeting[7])  # → e
print(greeting[8])  # → !

greeting = "Hi there!"
for i in range(0, len(greeting)):
    print(greeting[i])

s = "Python is cool!"
s1 = s[1:4]
s2 = s[1:]
s3 = s[:4]
print(s1)
print(s2)
print(s3)

# ask the user how brownies to be served
brownies_input = input("Would you like your chocolate brownies served hot or cold: ")
if (brownies_input == "hot"):
    brownies_serve_hot = True
else:
    brownies_serve_hot = False

# ask the user if they want to watch additional
star_show_input = input("Add Stargazing Show: (Y/N) ")
if ((star_show_input == "Y") or (star_show_input == "y")):
    include_star_show = True
else:
    include_star_show = False

