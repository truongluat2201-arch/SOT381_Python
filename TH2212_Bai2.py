a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
maxx = a
if b > maxx :
    maxx = b
if c > maxx:
    maxx = c
print(f"Số lớn nhất là {maxx}")