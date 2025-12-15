n = int(input("Nhập số n: "))
tong = 0
for i in range(1,n+1):
    if (i % 2 == 0) and (i % 3 == 0):
        tong = tong + i
print(f"Tổng các số từ 1 đến {n} chia hết cho 2 và 3 là {tong}")