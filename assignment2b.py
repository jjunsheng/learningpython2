# def heartrate_resting():
#     heartrate_resting = int(input("Enter your Resting Heart Rate: "))
#     if heartrate_resting == "":
#         print("Invalid Input")
#         heartrate_resting()
#


# def start():
#     try:
#         age = input("Enter your age: ")
#         except int(age) < 0:
#             print("Age cannot be negative.")
#             start()
#         except int(age) == 0:
#             print("Age cannot be 0.")
#             start()
#         except ValueError:
#             print("Invalid Input")
#             start()
#         print(age)
#
#
# start()
age = float(input("Enter your age: "))
while age < 21 or age > 60:
    print("Invalid Input")
    age = float(input("Please enter a proper age: "))

rhr = float(input("Enter your resting heart rate: "))
while rhr < 60 or rhr > 160:
    print("Invalid Input")
    rhr = float(input("Please enter a resting heart rate: "))

mhr = 220 - age
vo2 = 15 * (mhr / rhr)
print(vo2)

print(f"Your age is {str(age)} and resting heart rate is at {str(rhr)}.")

if 18 < age < 30:
    if 40 < vo2 < 60:
        print("Your are within the guideline for Basketball if you are male.")
    elif 43 < vo2 < 60:
        print("Your are within the guideline for Basketball if you are female.")

if 18 < age < 26:
    if 62 < vo2 < 74:
        print("Your are within the guideline for Bicycling if you are male.")
    elif 55 < vo2 < 67:
        print("Your are within the guideline for Canoeing if you are female.")
    elif 47 < vo2 < 57:
        print("Your are within the guideline for Bicycling if you are female.")
    elif 47 < vo2 < 67:
        print("Your are within the guideline for Canoeing if you are female.")

if 18 < age < 22:
    if 52 < vo2 < 58:
        print("Your are within the guideline for Gymnastic if you are male.")
    elif 36 < vo2 < 50:
        print("Your are within the guideline for Gymnastic if you are female.")

if 10 < age < 25:
    if 50 < vo2 < 70:
        print("Your are within the guideline for Swimming if you are male.")
    elif 40 < vo2 < 60:
        print("Your are within the guideline for Swimming if you are female.")
print()