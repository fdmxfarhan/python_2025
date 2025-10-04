def koochaktarin(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def jadval_zarb(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i*j, end="\t")
        print()

def miangin(a, b, c):
    return (a+b+c)/3

