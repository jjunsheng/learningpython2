# # if else, if A else B
# num_input = input("Choose a number :")
# num_int = int(num_input)
#
# UNIT_PRICE = 4
# cost = UNIT_PRICE * num_int
#
# # must change to int if not when multiply is string*4
# if num_input == 1:
#     print("{0} unit: ${1}".format(num_int, cost))
# else:
#     print("{0} unit: ${1}".format(num_int, cost))
#
# # if elif elif.. else
# mark_input = input("Please enter mark: ")
# mark = int(mark_input)
# if (mark >= 80):
#     grade = "A"
# elif (mark >= 60):
#     grade = "B"
# elif (mark >= 40):
#     grade = "C"
# else:
#     grade = "D"
# print("Mark {0}, Grade {1}".format(mark, grade))
#
# # let's try with 2nd layer of if
# num_input = input("Enter an integer: ")
# num = int(num_input)
#
# if (num == 0):
#     print("This number is zero")
#
# elif (num > 0):
#     if (num % 2 == 0):
#         print("This number is positive and even")
#     else:
#         print("This number is positive and odd")
# else:
#     if (num % 2 == 0):
#         print("This number is negative and even")
#     else:
#         print("This number is negative and odd")
#
# # if (alone)
# if True:
#     print("Ongoing")
#
# # example on how to find the largest number, a bit of hardcode, could have use loop but haven learn at this point
# input1 = input("Enter the 1st integer: ")
# n1 = int(input1)
# input2 = input("Enter the 2nd integer: ")
# n2 = int(input2)
# input3 = input("Enter the 3rd integer: ")
# n3 = int(input3)
# max_n = n1
# if (n2 > max_n):
#     max_n = n2
# if (n3 > max_n):
#     max_n = n3
# print("Max of {0}, {1}, {2} is {3}".format(n1, n2, n3, max_n))
#
# # and or not, BOTH if A and B, OR if A or B
#
child_input = input("Enter number of children: ")
child_int = int(child_input)
adult_input = input("Enter number of adult: ")
adult_int = int(adult_input)
show_input = input("Enter number attending stargazing show: ")
show_int = int(show_input)

child_price = 20
adult_price = 35
show_price = 10

TOTAL_PRICE = child_int * child_price + adult_int * adult_price + show_int * show_price

# some learning tips, is not good to put in 10% discount by calculating using 90%. we should use 100 - discount rate
# this way our code will be more readable and friendly
if TOTAL_PRICE > 150:
    if TOTAL_PRICE > 200:
        discount_price = TOTAL_PRICE * 0.9
        print("Your total bill is ${0} and you received a free science park hats.".format(discount_price))
    else:
        print("Your total bill is ${0} and you received a free science park hats.".format(TOTAL_PRICE))
else:
    print("Your total bill is ${0}.".format(TOTAL_PRICE))


