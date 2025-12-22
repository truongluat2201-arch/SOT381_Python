def tinh_s(n):
    tu_so = 0
    mau_so = 0
    # tính tử số
    for i in range(1,n+1):
        tu_so = tu_so + i
    #tính mẫu số
    for j in range(1,n+1):
        if j % 2 == 0:
            mau_so = mau_so + j
    s = tu_so / mau_so
    return s


x=tinh_s(3)
print(f"Vậy giá trị của s là {x}")