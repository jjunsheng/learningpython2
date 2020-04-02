input_a = input("Enter number of cards with grade A: ")
grade_a = int(input_a)
input_b = input("Enter number of cards with grade B: ")
grade_b = int(input_b)
input_c = input("Enter number of cards with grade C: ")
grade_c = int(input_c)
total_cards = grade_a + grade_b + grade_c

# calculate percentage and round them off
pct_b = round(grade_b * 100 / total_cards)
pct_a = round(grade_a * 100 / total_cards)
pct_c = round(grade_c * 100 / total_cards)
print("Total number of cards: {0}".format(total_cards))
print("Grade statistics: A {0}%, B {1}%, C {2}%".format(pct_a, pct_b, pct_c))

# rounding them to a certain decimal digits print(round(pct_a, n) = 0.1 and so on
pct_a = grade_a * 100 / total_cards
print(pct_a)
print(round(pct_a))
print(round(pct_a, 1))
print(round(pct_a, 2))
print(round(pct_a, 3))
print(round(pct_a, 4))
print(round(pct_a, 5))
print(round(pct_a, 6))

# calculate average, always set input as str? then later change the nature of the input to int or float depend on situation?
input1 = input("Enter assignment 1 mark: ")
a1 = float(input1)
input2 = input("Enter assignment 2 mark: ")
a2 = float(input2)
input3 = input("Enter assignment 3 mark: ")
a3 = float(input3)
# calculate average mark
avg = round((a1 + a2 + a3) / 3, 2)

print("Average mark: {0}".format(avg))
