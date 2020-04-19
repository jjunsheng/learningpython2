from assignment4a import isValidLetter


def isValidNRIC():
    while True:
        user_nric = input("Please enter NRIC (S1234567A): ")
        nric_list = list(user_nric)
        test_list = []
        error_list = []
        for i in user_nric:
            c = 1
            try:
                i = int(i)
                c = 2
            except ValueError:
                pass
            test_list.append(c)
        if len(test_list) != 9:
            error_list.append("Must be at least 9 characters")
        if str(nric_list[0]).upper() != ("S" or "T"):
            error_list.append("NRIC must start with S or T")
        if test_list[-1] != 1:
            error_list.append("NRIC must end with letters")
        if test_list.count(2) != 7:
            error_list.append("NRIC must have only 7 digits in between 2 letters")
        if len(error_list) == 0:
            return True, nric_list, error_list, user_nric
        return False, nric_list, error_list, user_nric



while True:
    user_input = isValidNRIC()
    first_col = user_input[3]
    second_col = user_input[2]
    if user_input[0] and isValidLetter(user_input[1]):
        second_col.append("Valid")
        third_col = "Your NRIC is valid."
    else:
        second_col.append("Invalid last letter of NRIC")
        third_col = "Error. Your NRIC is invalid."
    print("{0:<20}{1:<60}{2:<40}".format("NRIC", "The NRIC rule to test", "Expected Output"))
    print("{0:<20}{1:<60}{2:<40}".format(first_col, second_col[0], third_col))
    for i in range(2, len(second_col)):
        print("{0:<20}{1:<60}".format("", second_col[i]))