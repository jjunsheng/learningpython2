# 4
import random

life = 3
guess_count = 1
computer_number = random.randint(0, 99)
print("Try to guess the number between 0 to 99 I'm thinking of.")
print(computer_number)
player_guess = int(input("Enter a number:"))
while player_guess != computer_number:
    life -= 1
    print("life remaining:{}".format(life))
    if life > 1:
        if life != 1:
            if player_guess > computer_number:
                player_guess = int(input("too high - guess again: "))
                guess_count += 1
            elif player_guess < computer_number:
                player_guess = int(input("too low - guess again: "))
                guess_count += 1
    elif life == 1:
        lower_range = computer_number - random.randint(0, 10)
        upper_range = computer_number + random.randint(0, 10)
        # x = range(lower_range, upper_range)
        # print(lower_range, upper_range, x)
        player_guess = int(input("Try to guess the number between {0} to {1} I'm thinking of: "
                                 .format(lower_range, upper_range)))
        while player_guess < lower_range or player_guess > upper_range:
            player_guess = int(input("Invalid number input, please guess a number between {0} to {1}: "
                                     .format(lower_range, upper_range)))
        guess_count += 1
    if life == 0:
        print(f"Sorry Game Over, it was {computer_number}.")
        break

if player_guess == computer_number:
    print("Correct! The number of guesses you made was {}.".format(str(guess_count)))
