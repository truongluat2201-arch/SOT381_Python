a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
minn = a
if b < minn:
    minn = b
if c < minn:
    minn = c
print(f"Số nhỏ nhất là {minn}")