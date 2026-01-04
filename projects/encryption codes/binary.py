def decimal_to_b(x, b):
    list_of_vals = []
    while x != 0:
        z = x//b
        y = x%b
        x = z
        list_of_vals.append(y)
    
    list_of_vals = list(map(str, list_of_vals))
    return int("".join(reversed(list_of_vals)))

def b_to_decimal(x, b):
    return int(str(x), b)

def x_plus_y_in_b_base(x: list,y:list,b: int):
    val = b_to_decimal(int("".join(map(str,x))), b) + b_to_decimal(int("".join(map(str,y)),b),b)
    vals = list(str(decimal_to_b(val, b)))
    return list(map(int, vals))

print(x_plus_y_in_b_base([1],[1],2))