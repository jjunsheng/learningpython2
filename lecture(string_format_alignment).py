# string format, didnt know can do this
# note the {} refer to the positioning in the tuple
fname = "Jun"
lname = "Sheng"
print("Hi {0} {1}!".format(fname, lname))
print("{1} {2} is {0} years old".format(24, fname, lname))
print("And his favorite number is {0}\n".format(7))

# strong format with alignment, take note of '<' & '>' & '^'
print("Exam result:")
print("{0:<10}{1:<15}{2:>5}{3:>5}".format("COMM104", "Commerce I", "75", "D"))
print("{0:<10}{1:<15}{2:>5}{3:>5}".format("FIN201", "Accounting", "85", "HD"))
print("{0:<10}{1:<15}{2:>5}{3:>5}".format("MTH202", "Analysis", "100", "HD"))
print("{0:<10}{1:<15}{2:^5}{3:^5}".format("ECTE110", "Circuits", "90", "HD"))
print("1234567890123456789012345678901234567890")
print()

# ugly alignment
print("{0} x {1} = {2}".format(1, 5, 1 * 5))
print("{0} x {1} = {2}".format(2, 5, 2 * 5))
print("{0} x {1} = {2}".format(3, 5, 3 * 5))
print("{0} x {1} = {2}".format(4, 5, 4 * 5))
print("{0} x {1} = {2}".format(5, 5, 5 * 5))
print("{0} x {1} = {2}".format(6, 5, 6 * 5))
print("{0} x {1} = {2}".format(7, 5, 7 * 5))
print("{0} x {1} = {2}".format(8, 5, 8 * 5))
print("{0} x {1} = {2}".format(9, 5, 9 * 5))
print("{0} x {1} = {2}".format(10, 5, 10 * 5))
print()

# better output and alignment
print("{0:>2} x {1:>1} = {2:>2}".format(1, 5, 1 * 5))
print("{0:>2} x {1:>1} = {2:>2}".format(2, 5, 2 * 5))
print("{0:>2} x {1:>1} = {2:>2}".format(3, 5, 3 * 5))
print("{0:>2} x {1:>1} = {2:>2}".format(4, 5, 4 * 5))
print("{0:>2} x {1:>1} = {2:>2}".format(5, 5, 5 * 5))
print("{0:>2} x {1:>1} = {2:>2}".format(6, 5, 6 * 5))
print("{0:>2} x {1:>1} = {2:>2}".format(7, 5, 7 * 5))
print("{0:>2} x {1:>1} = {2:>2}".format(8, 5, 8 * 5))
print("{0:>2} x {1:>1} = {2:>2}".format(9, 5, 9 * 5))
print("{0:>2} x {1:>1} = {2:>2}".format(10, 5, 10 * 5))
