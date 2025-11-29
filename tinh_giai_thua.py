n = int(input("Nhập số n: "))
if n < 0:
    print("Không hợp lệ")
else:
    t = 1
    for i in range(1,n+1):
        t = t*i
    print(f"{n} giai thừa là {t}")