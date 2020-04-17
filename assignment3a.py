import random

1
fibo = int(input("Enter how many Fibonacci number you want to print: "))
fibo_list = [0, 1]
for i in range(2, fibo+1):
    n = fibo_list[i-1] + fibo_list[i-2]
    fibo_list.append(n)
print(fibo_list)
print()

fibo_list = [0, 1]
while len(fibo_list) <= fibo:
    n = fibo_list[-1] + fibo_list[-2]
    fibo_list.append(n)
print(fibo_list)
print()

# 2
n = int(input("Enter the first number: "))
n_list = [n]
# ending with 1
odd = 1
even = 0
while n_list[-1] != 1:
    if n_list[-1] % 2 == 0:
        even += 1
        n_list.append(n_list[-1]//2)
    else:
        odd += 1
        n_list.append((n_list[-1] * 3) + 1)
print("The sequence is : {}.".format(n_list))

avg = sum(n_list) / len(n_list)
stddv_total = 0
for i in range(len(n_list)):
    stddv_total += (avg - i) ** 2

stddv = round(((stddv_total/avg) ** 0.5), 2)

print("Total sum: {}.".format(sum(n_list)))
print("Average: {}.".format(round(avg, 2)))
# print(len(n_list))
print("Number of odd numbers: {}.".format(odd))
print("Number of even numbers: {}.".format(even))
print("Population standard deviation: {}.".format(stddv))
print()


# 3
def math_challenge():
    print("Maths Challenge\n"
          "Type e at any time to exit")
    str_answer = ""
    right = 0
    wrong = 0
    while True:
        blank = "__"
        n1 = random.randint(0, 100)
        n2 = random.randint(0, 100)
        # print(n1, n2, blank)
        arrange_list = [blank, n1, n2]
        shuffle_list = random.sample(arrange_list, len(arrange_list))
        # print(shuffle_list)
        c1 = random.randint(1, 2)
        if c1 == 1:
            print(str(shuffle_list[0]) + " + " + str(shuffle_list[1]) + " = " + str(shuffle_list[2]))
        else:
            print(str(shuffle_list[0]) + " - " + str(shuffle_list[1]) + " = " + str(shuffle_list[2]))
        str_answer = input("Answer :")
        if str_answer == "e":
            break
        answer = int(str_answer)
        if c1 == 1:
            if n1 + n2 == answer or n1 + answer == n2 or n2 + answer == n1:
                right += 1
                print("Right")
            else:
                wrong += 1
                print("Wrong")
        if c1 == 2:
            if n1 - n2 == answer or n1 - answer == n2 or n2 - answer == n1 or n2 - n1 == answer or answer - n1 == n2 or answer - n2 == n1:
                right += 1
                print("Right")
            else:
                wrong += 1
                print("Wrong")

    print("Thank you for using Math Challenge program.")
    print("Number of rights: {}".format(right))
    print("Number of wrongs: {}".format(wrong))


math_challenge()