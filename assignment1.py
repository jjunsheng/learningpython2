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

