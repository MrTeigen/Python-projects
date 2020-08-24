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
