import math


def delta(a, b, c):
    return (b**2) - (4 * a * c)


def bhaskara(a, b, c):
    result_delta = delta(a, b, c)

    if result_delta < 0:
        return "delta negativo!"
    square_root_delta = round(math.sqrt(result_delta), 2)

    x1 = round((-b + square_root_delta) / (2 * a), 2)

    x2 = round((-b - square_root_delta) / (2 * a), 2)

    return f"x1 = {x1}, x2 = {x2}"


print(bhaskara(7, 3, 4))

print(bhaskara(1, 5, 2))

print(bhaskara(1, -3, 2))
