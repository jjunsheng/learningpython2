# sample use case
num1 = 50
num2 = 16
sum = num1 + num2
print("The sum of {0} and {1} is {2}".format(num1, num2, sum))

# doesnt add up because they are seen as string
num1 = input("Enter the first integer: ")
num2 = input("Enter the second integer: ")
sum = num1 + num2
print("The sum of {0} and {1} is {2}".format(num1, num2, sum))

#  new program that adds up cause now they are integer
input1 = input("Enter the first integer: ")
num1 = int(input1)
input2 = input("Enter the second integer: ")
num2 = int(input2)
sum = num1 + num2
print("The sum of {0} and {1} is {2}".format(num1, num2, sum))
