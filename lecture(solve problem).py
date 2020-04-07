for x in range(1, 6):
    for y in range(1, 6):
        lhs = x * y
        rhs = x + y
        if lhs == rhs:
            print("x={0}, y={1}\n{0} X {1} = {0} + {1}".format(x, y))

for x in range(1, 6):
    for y in range(1, 6):
        lhs = x * y
        rhs = x + y
        if lhs == rhs:
            print("Solution found x = {0}, y = {1}".format(x, y))

for x in range(1,101):
    for y in range(1, 101):
        lhs = (x + y)**5
        rhs = x ** 5 + y ** 5 + 3000000
        if lhs == rhs:
            print("x={0}, y={1}\n ({0} X {1})*5 = {0}*5 + {1}*5 + 3000000".format(x, y))
            print("Solution found x = {0}, y = {1}".format(x, y))

for x in range(1,101):
    for y in range(1, 101):
        for z in range(1, 101):
            lhs = x + y + z
            rhs = x * y * z
            if lhs == rhs:
                print("x={0}, y={1}, z={2}\n  {0} + {1} + {2} = {0} X {1} X {2}".format(x, y, z))
                print("Solution found x = {0}, y = {1}".format(x, y))
