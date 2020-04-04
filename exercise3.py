# 1
temperature_input = input("Key in the temperature: ")
temperature_int = int(temperature_input)

if temperature_int >= 100:
    state = "gas"
elif temperature_int <= 0:
    state = "solid"
elif 0 < temperature_int < 100:
    state = "liquid"

print("The water is in {} state at {} temperature.".format(state, temperature_input))

# 2
gender = input("Key in gender(f/m): ")
amount = input("Key in amount: ")
amount_int = int(amount)
print("You have spend ${0}".format(amount), end="")
if amount_int > 100:
    if gender == "f":
        print(" " + "and received hand cream as free gift.")
    elif gender == "m":
        print(" " + "and received shaver as free gift.")
else:
    print(" " + "and received no free gift.")

# 3
gender = input("Key in gender(female/male): ")
age = input("Key in age: ")
age_int = int(age)

if gender == 'female' and age_int >= 17 or gender == 'male' and age_int >= 15:
    print("You are {0} years old {1} and allowed to participate.".format(age, gender))
else:
    print("You are {0} years old {1} and not allowed to participate.".format(age, gender))

4
gender = input("Key in gender(female/male): ")
age = input("Key in age: ")
age_int = int(age)

if age_int >= 12:
    if gender == "female":
        cost = "18"
    elif gender == "male":
        cost = "20"
else:
    if gender == "female":
        cost = "10"
    elif gender == "male":
        cost = "12"


print("You are {0} years old {1} and the cost of meal is ${2}.".format(age, gender, cost))

5
salary = input("Key in your monthly salary: ")
working_period = input("Key in months of employment: ")
salary_int = int(salary)
working_period_int = int(working_period)
annual_salary = salary_int * 12
annual_salary_str = str(annual_salary)

if annual_salary >= 30000 and working_period_int >= 24:
    print("You are eligible for loan.")
else:
    print("You are not eligible for loan.")

6
cost = input("Enter the total cost of purchase: ")
bank = input("Enter the bank of your credit card(DBS, OCBC, etc.): ")
cost_int = int(cost)
discount = 0

if cost_int > 200:
    if bank == "DBS":
        discount = 0.1
    elif bank == "OCBC":
        discount = 0.15
else:
    discount = 0

discount_price = (1 - discount) * cost_int

print("Please pay ${0}.".format(discount_price))