# This is also the taylor expansion of arctan(x) for x = 1, where we multiplied both sides by 4,
# we then get pi = 4 - 4/3 + 4/5 - 4/7 + 4/9..., the right side of this equation is given in the formula below

def pi():
    n = 1
    current, later = 4, 4
    while True:
        yield current
        later = later * ((-1) * (1 + 2 * (n - 1)) / (1 + 2 * (n)))
        current = current + later
        n += 1

leib = pi()
for x in range(10000000):
    print(next(leib))
