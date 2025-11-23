# tính tổng các số từ 1 đến n
n = int(input("Nhập số n: "))
tong = 0
for i in range(1,n+1):
    tong = tong + i
print(f"Tổng các số từ 1 đến {n} là {tong}")