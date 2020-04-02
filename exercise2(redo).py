degree_celsius = input("Key in temperature in degree celsius: ")
converted_k = float(degree_celsius) + 273.15
print("{0} degree celcius is {1} Kelvin.".format(degree_celsius, converted_k))

degree_celsius = input("Key in temperature in degree celsius: ")
converted_f = float(degree_celsius) * 1.8 + 32
print("{0} degree celcius is {1} Fahrenheit.".format(degree_celsius, converted_f))

name1 = "John"
score1 = 56
name2 = "Mary"
score2 = 65
name3 = "Peter"
score3 = 89

print("{0:<10}{1:<6}".format("Name", "Score"))
print("{0:<10}{1:<6}".format(name1, score1))
print("{0:<10}{1:<6}".format(name2, score2))
print("{0:<10}{1:<6}".format(name3, score3))
print()

number = input("Key in a number:")
int_num = int(number)

print("Enter power:{0}".format(int_num))
print("{0:^12}{1:^12}".format("Number", "Power of " + number + " is"))
print("{0:^12}{1:^12}".format("1", int_num ** 1))
print("{0:^12}{1:^12}".format("2", int_num ** 2))
print("{0:^12}{1:^12}".format("3", int_num ** 3))
print()

from datetime import datetime
name = input("Key in your name:")
age = input("Key in your age:")
today = datetime.now()
hundredyear = 100 - int(age) + today.year
print("Hi {0}, you will be 100 years old in {1}!".format(name, hundredyear))