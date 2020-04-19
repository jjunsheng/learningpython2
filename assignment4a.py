# 1
def isValidNRIC():
    while True:
        user_nric = input("Please enter your NRIC (S1234567A): ")
        nric_list = list(user_nric)
        test_list = []
        for i in user_nric:
            c = 1
            try:
                i = int(i)
                c = 2
            except ValueError:
                pass
            test_list.append(c)
        if (len(test_list) == 9) and (nric_list[0] == ("S" or "T")) and (test_list[-1] == 1) and (
                test_list.count(2) == 7):
            # print(nric_list)
            return nric_list
        print("Invalid Input")


# 2
def isValidLetter(list):
    # print(list)
    valid_list = ["J", "Z", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
    last_digit = (((int(list[1]) * 2) + (int(list[2]) * 7) + (int(list[3]) * 6) + (int(list[4]) * 5) + (
            int(list[5]) * 4) + (int(list[6]) * 3) + (int(list[7]) * 2))) % 11
    # print(last_digit, valid_list[last_digit])
    if valid_list[last_digit] == str(list[-1]).upper():
        return True
    else:
        return False
