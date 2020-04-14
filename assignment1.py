# 2
var1 = 'ong'
var2 = 'jun'
var3 = 'sheng'

# print(f'{var1} {var2} {var3}')
# print(f'{var1} {var3} {var2}')
# print(f'{var2} {var1} {var3}')
# print(f'{var2} {var3} {var1}')
# print(f'{var3} {var1} {var2}')
# print(f'{var3} {var2} {var1}')

matrix = [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
    ]

for i in range(len(matrix)):
    count = 0
    for x in matrix[i]:
        count += 1
        if True:
            if x == 1:
                print(var1, end=" ")
            if x == 2:
                print(var2, end=" ")
            if x == 3:
                print(var3, end=" ")
        if count == 3:
            print()
print()

# 3
print("Christma Tree:")
print("{0:^9}".format("*"))
print("{0:^9}".format("* *"))
print("{0:^9}".format("* # *"))
print("{0:^9}".format("* # # *"))
print("{0:^9}".format("* # # # *"))
print()

# 4
fibo = [0, 1]
string_input = input("Key in number of entries: ")
int_input = int(string_input)
for i in range(2, int_input+1):
    fibo.append(fibo[i-1] + fibo[i-2])
fibo.remove(0)

print("The first {0} entries of Fibonacci series are:{1}.".format(int_input, fibo))
print("The sum of these entries is {0}.".format(sum(fibo)))
print()

# 5
print("The quick brown fox")
print("jumps over the lazy dog")

print("The quick brow fox \njumps over the lazy dog")
print()

# 6
print("{0:<15}{1:>15}{2:>20}{3:^20}".format("CSIT 127", "Monday", "8:30-11:30", "B3-12"))
print("{0:<15}{1:>15}{2:>20}{3:^20}".format("CSIT 111", "Thursday", "12:00-15:00", "A2-01"))
print("{0:<15}{1:>15}{2:>20}{3:^20}".format("CSIT 221", "Monday", "15:30-17:30", "B4-11"))
print("{0:<15}{1:>15}{2:>20}{3:^20}".format("CSIT 301", "Tuesday", "8:30-11:30", "A2-07"))
print()

# 7
shoe_size = 10.5
dob = 1995
int1 = shoe_size * 5
int2 = int1 + 50
int3 = int2 * 20
int4 = int3 + 1017
int5 = int4 - dob
print("Step 1: my shoe size is {0}, multiplying with 5 gives {1}.\nStep 2: adding 50 gives {2}."
      "\nStep 3: multiplying with 20 gives {3}."
      .format(str(shoe_size), str(int1), str(int2), str(int3)))
print("Step 4: adding 1018 gives {0}."
      "\nStep 5: Subtracting the year i was born {1}, gives {2}!"
      .format(str(int4), str(dob), str(int5)))
print()

print("Step 1: my shoe size is " + str(shoe_size) + ",multiplying with 5 gives " + str(int1) + ".\nStep 2: adding 50 gives " + str(int2) + ".\nStep 3: multiplying with 20 gives " + str(int3) + ".\nStep 4: adding 1018 gives " + str(int4) + ".\nStep 5: Subtracting the year i was born " + str(dob) + ", gives " + str(int5) + "!")