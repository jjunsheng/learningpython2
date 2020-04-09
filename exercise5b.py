# 5
def cal_discount():
    price_input = input("Enter the original price of item:- ")
    discount_input = input("Enter the discount in percentage:- ")
    discount_amount = int(price_input) * int(discount_input) / 100
    return print("You get to save ${0}".format(discount_amount))


cal_discount()
print()


# 6
def smaller_num(n1, n2):
    if n1 < n2:
        n3 = n1
        return print("The smaller number between {0} and {1} is {2}".format(n1, n2, n3))
    else:
        n3 = n2
        return print("The smaller number between {0} and {1} is {2}".format(n1, n2, n3))


num1 = input("Enter the first number:- ")
num2 = input("Enter the second number:- ")
smaller_num(num1, num2)
print()


# 7
def get_price(gender, age):
    if gender == 'male':
        if age >= 12:
            return 20
        else:
            return 12
    else:
        if age >= 12:
            return 18
        else:
            return 10


print(get_price("male", 10))
print(get_price("female", 15))
print()
