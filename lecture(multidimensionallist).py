list2d = [[1, 2, 3, 4],
          [9, 8, 7, 6]
          ]
print(list2d[0][1])
print(list2d[0][2])
print(list2d[1][0])
print(list2d[1][3])

# basically is like x and y, first you find the row then you find the column
euler = [
    [68**2, 29**2, 41**2, 37**2],
    [17**2, 31**2, 79**2, 32**2],
    [59**2, 28**2, 23**2, 61**2],
    [11**2, 77**2,  8**2, 49**2]
    ]
r1 = euler[0][0] + euler[0][1] + euler[0][2] + euler[0][3]
r2 = euler[1][0] + euler[1][1] + euler[1][2] + euler[1][3]
r3 = euler[2][0] + euler[2][1] + euler[2][2] + euler[2][3]
r4 = euler[3][0] + euler[3][1] + euler[3][2] + euler[3][3]

c1 = euler[0][0] + euler[1][0] + euler[2][0] + euler[3][0]
c2 = euler[0][1] + euler[1][1] + euler[2][1] + euler[3][1]
c3 = euler[0][2] + euler[1][2] + euler[2][2] + euler[3][2]
c4 = euler[0][3] + euler[1][3] + euler[2][3] + euler[3][3]

d1 = euler[0][0] + euler[1][1] + euler[2][2] + euler[3][3]
d2 = euler[0][3] + euler[1][2] + euler[2][1] + euler[3][0]

print("r1={0}, r2={1}, r3={2}, r4={3}, c1={4}, c2={5}, c3={6}, c4={7}, d1={8}, d2={9}".format(r1, r2, r3, r4, c1, c2, c3, c4, d1, d2))
