# # 1 2 3
# def even_index_string(s):
#     word = ""
#     for i in range(len(s)):
#         if i % 2 == 0:
#             word = word + s[i]
#     return word
#
#
# def upper_half_string(s):
#     word = ""
#     if len(s) % 2 == 0:
#         word = s[0:len(s)//2]
#     else:
#         word = s[0:len(s)//2+1]
#     return word
#
#
# def middle_char_in_string(s):
#     word = ""
#     # odd number, remember that the int always round down and when it starts to count, it count from 0 1 2 3. hence d
#     if len(s) % 2 != 0:
#         word = s[len(s)//2]
#     else:
#         word = s[len(s)//2-1:len(s)//2]
#     return word
#
#
# print(even_index_string("abcdef"))
# print(upper_half_string("abcdef"))
# print(upper_half_string("abcdefg"))
# print(middle_char_in_string("abcdefg"))
# print(middle_char_in_string("abcdef"))
# print()
# # print(fact(10))
#
# a = "123456789"
# b = "12345678"
#
# print(len(a)//2)
# print(a[4])
# print(len(a)//2-1)
# print(len(b)//2)
# print(len(b)//2-1)
# print()
#
#
# # 4
# def fact(num):
#     total_sum = 1
#     for i in range(1, num+1):
#         total_sum = total_sum * i
#     return total_sum
#
#
# print(fact(10))
# print()
#
#
# # 5
def multiply(num1, num2):
    multi_ttl = 0
    for i in range(1, num1 + 1):
        multi_ttl = multi_ttl + num2
    return multi_ttl


print(multiply(10, 10))
print(multiply(6, 8))
print()


# 7
def power(num1, num2):
    sum = 1
    for i in range(num2):
        sum = multiply(sum, num1)
    return sum


print(power(8, 6))