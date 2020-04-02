# + add
# - minus
# * multiply
# / division > decimal number
# // floor division > integer result
# ** exponent (square root), can do 0.5 also so half
# % modulus, remaining value
a = 3
b = 2
a = a + b
b = a ** b
a = b // a
print(a)
print(b)

a = 3
b = 2
a += 4
b *= a
a //= 3
print(a)
print(b)

# candy box: $4/each or $10/3boxes
# very nice coding, straight forward, instant pull the variable and no need for rename or remake another variable (box count)
box_count = 50
# remember that //returns a integer so is a whole number
group_of_3_count = box_count // 3
left_over_count = box_count - 3 * group_of_3_count
cost = group_of_3_count * 10 + left_over_count * 4
print("{0} candy boxes cost: ${1}".format(box_count, cost))