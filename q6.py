def large_odd_num(x, y, z):
    x_o = (x % 2 == 0)
    y_o = (y % 2 == 0)
    z_o = (z % 2 == 0)
    if (x_o and y_o and z_0):
        print("No odd number.")
    if (x_o):
        if (y_o):
            print(f"{z} is largest odd number")
        else:
            if (z_o):
                print(f"{y} is largest odd number")
            else:
                if (y > z):
                    print(f"{y} is largest odd number")
                else:
                    print(f"{z} is largest odd number")
    else:
        if (y_o and z_o):
            print(f"{x} is largest odd number")
        if (y_o):
            if (x > z):
                print(f"{x} is largest odd number")
            else:
                print(f"{z} is largest odd number")
        elif (z_o):
            if (x > y):
                print(f"{x} is largest odd number")
            else:
                print(f"{y} is largest odd number")
        else:
            if (x > y and x > z):
                print(f"{x} is largest odd number")
            elif (x < y and y > z):
                print(f"{y} is largest odd number")
            elif (x < z and y < z):
                print(f"{z} is largest odd number")

large_odd_num(11,13,9)
