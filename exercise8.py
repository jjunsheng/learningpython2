# 1
scores_list = [
    [78, 109, 78, 77, 118, 63, 99, 150],
    [77, 57, 98, 145, 106, 99, 169, 174],
    [158, 85, 55, 25, 26, 67, 96, 23],
    [25, 50, 80, 101, 136, 87, 106, 165],
    [155, 170, 32, 107, 70, 141, 50, 84]
]


# print(scores_list[0][0])
# print(scores_list[1][1])
# print()


def average_score(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    average = total / int(len(list))
    return average


def highest_score(list):
    highest = 0
    for i in range(len(list)):
        if list[i] >= highest:
            highest = list[i]
    return highest


def lowest_score(list):
    lowest = list[0]
    for i in range(len(list)):
        if list[i] <= lowest:
            lowest = list[i]
    return lowest


# players_average = [scores_list[0],
#                    scores_list[1],
#                    scores_list[2],
#                    scores_list[3],
#                    scores_list[4]
#                    ]

# print(average_score(scores_list[0]))
# print(highest_score(scores_list[0]))
# print(lowest_score(scores_list[0]))


players = 0
highest_average = average_score(scores_list[0])
lowest_average = average_score(scores_list[0])
best_performer = 0
worst_performer = 0
print("--------------- Player Statistics ------------")
for i in range(len(scores_list)):
    players += 1
    print("Player {0}".format(players))
    print("Score ({0} games): {1}".format(len(scores_list[0]), scores_list[i]))
    print("Average Score: {0}".format(average_score(scores_list[i])))
    print("Highest Score: {0}".format(highest_score(scores_list[i])))
    print("Lowest Score: {0}".format(lowest_score(scores_list[i])))
    print()
    if average_score(scores_list[i]) > highest_average:
        highest_average = average_score(scores_list[i])
        best_performer = players
    if average_score(scores_list[i]) < lowest_average:
        lowest_average = average_score(scores_list[i])
        worst_performer = players

print("------------ Best Performer of the Day------------")
print("The best performer of the day is player {0}".format(best_performer))
print("The player has an average score of {0}".format(highest_average))
print()

print("------------ Worst Performer of the Day------------")
print("The worst performer of the day is player {0}".format(worst_performer))
print("The player has an average score of {0}".format(lowest_average))
