def so_LN(a,b,c):
    maxx = a
    if b > maxx:
        maxx = b
    if c > maxx:
        maxx = c
    return maxx

def so_NN(a,b,c):
    minn = a
    if b < minn:
        minn = b
    if c < minn:
        minn = c
    return minn


x = so_LN(4,5,6)
y = so_NN(7,8,9)
print(f"Số lớn nhất là {x}")
print(f"Số nhỏ nhất là {y}")