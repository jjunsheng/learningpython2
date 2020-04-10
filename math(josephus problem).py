seat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(seat)

# what we are able to do is to code every step of kill 1 by 1, 1 step = A kills B and A survive then it will loop
while True:
    if len(seat) == 1:
        print("the winning seat is {0}".format(seat[0]))
        break

    turn = seat[0]
    next_person = seat[1]
    print("{0} kills {1}".format(turn, next_person))

    # remove the first two from the list that is invovle in this fight
    del seat[0]
    del seat[0]

    # adding back the one who survive to the back of the line
    seat.append(turn)
    print(seat)

