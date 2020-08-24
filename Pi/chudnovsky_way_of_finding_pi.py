import math


def chudnovsky():
    k = 0
    current = (12 * (-1) ** k * math.factorial(6 * k) * (545140134 * k + 13591409)) / ((math.factorial(3 * k) * math.factorial(k) ** 3 * 640320 ** (3 * k + 3 / 2)))
    while True:
        yield 1 / current
        k += 1
        current = current + 12 * (-1) ** k * math.factorial(6 * k) * (545140134 * k + 13591409) / (math.factorial(3 * k) * math.factorial(k) ** 3 * 640320 ** (3 * k + 3 / 2))

chud = chudnovsky()
print(next(chud))
print(next(chud))
print(next(chud))
print(next(chud))
print(next(chud))
print(next(chud))
print(next(chud))
print(next(chud))
print(next(chud))
print(next(chud))
