def geo3(x, y, z):
    if x != 0 and y != 0 and z != 0 and x // abs(x) == y // abs(y) and x // abs(x) == z // abs(z):
        print("Same sign")
        return (x * y * z) ** (1 / 3)
    return 0
