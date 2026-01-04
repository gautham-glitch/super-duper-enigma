def calc_e(terms):
    e = 0
    factorial = 1
    for i in range(terms):
        if i > 0:
            factorial *= i
        e += 1 / factorial
    return e

print(calc_e(17)) 