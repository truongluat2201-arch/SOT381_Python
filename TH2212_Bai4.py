def so_LN_NN(a,b,c):
    # Tìm số lớn nhất
    maxx = a
    if b > maxx:
        maxx = b
    if c > maxx:
        maxx = c
    # tìm số nhỏ nhất
    minn = a
    if b < minn:
        minn = b
    if c < minn:
        minn = c
    return maxx, minn



x = so_LN_NN(4,5,6)
print(f"Số lớn nhất và số nhỏ nhất lần lượt là {x}")