def so_LN(a,b,c):
    maxx = a
    if b > maxx:
        maxx = b
    if c > maxx:
        maxx = c
    return maxx

x = so_LN(1,2,3)
print(x)