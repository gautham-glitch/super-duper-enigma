def factorizer(n):
    if n == 1 or 0 :
        return n
    else: 
        return n * factorizer(n-1)
print(factorizer(5))

def adder(n):
    if n == 1 or 0:
        return n
    else:
        return n+adder(n-1)
print(adder(3))

