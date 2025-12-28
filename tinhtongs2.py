# tính tổng s = 10 + 1/2 + 2/3 + .... + n-1/n
n = int(input("Nhập số n: "))
tong = 10
for i in range(1,n+1):
    tong = tong + (i-1)/i
print(f"Tổng S= {tong:.2f}")