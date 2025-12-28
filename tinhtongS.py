# tính tổng s = 1+1/2+1/3+....+1/n
n = int(input("Nhập số n: "))
tong = 0
for i in range(1,n+1):
    tong = tong + 1/i
print(f"Tổng s= {tong:.2f}")