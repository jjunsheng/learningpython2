degree_celsius = int(input('Celsius : '))
degree_kelvin = degree_celsius + 273.15
print(f'{degree_kelvin}C')

degree_celsius = int(input('Celsius : '))
degree_fahrenheit = (degree_celsius * (9/5)) + 32
print(f'{degree_fahrenheit}F')

name1 = "John"
score1 = 56
name2 = "Mary"
score2 = 65
name3 = "Peter"
score3 = 89

print(f'''
Name      Score
{name1}      {score1}
{name2}      {score2}
{name3}     {score3}
''')

power = int(input('Enter power :'))
for i in range(3):
    i += 1
    print(f'{i} {i ** power}')

from datetime import datetime
name = (input('Name :'))
age = int(input('Age :'))

today = datetime.now()
hundredyear = today.year + 100 - age
print(f'{name} will turn 100 years old in year {hundredyear}.')