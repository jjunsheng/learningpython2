def print_steps(number):
    step = 0
    while True:
        print("Step {0}: {1}".format(step, number))

        if number == 1:
            break

        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1

        step += 1


num_input = input("Enter a positive integer: ")
n = int(num_input)

print_steps(n)

# if you study closely
# number of steps adding up is running on a different track with numbers calculation in the same function, interesting

