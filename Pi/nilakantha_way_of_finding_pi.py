def nilakantha():
    k = 1
    later = 4 / 24
    current = 3
    while True:
        current = 3 + later
        yield current
        later = later + 4 * (-1) ** k / ((2 * k + 2) * (2 * k + 3) * (2 * k + 4))
        k += 1


nila = nilakantha()
print(next(nila))
print(next(nila))
print(next(nila))
print(next(nila))
print(next(nila))
print(next(nila))
print(next(nila))
print(next(nila))
print(next(nila))
print(next(nila))
print(next(nila))
print(next(nila))
print(next(nila))
print(next(nila))
print(next(nila))
print(next(nila))
