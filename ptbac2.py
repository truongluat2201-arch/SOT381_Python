# Giải phương trình bậc 2
import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
if a==0:
    if b==0:
        if c==0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c/b
        print(f"Phương trình có nghiệm x= {x:.2f}")
else:
    denta = (b*b) - (4*a*c)
    if denta < 0:
        print("Phương trình vô nghiệm")
    elif denta == 0:
        x = -b/(2*a)
        print(f"Phương trình có nghiệm kép x = {x:.2f}")
    else:
        x1 = (-b + math.sqrt(denta)) / (2*a)
        x2 = (-b - math.sqrt(denta)) / (2*a)
        print(f"PHương trình có 2 nghiệm phân biệt x1 = {x1:.2f}, x2 = {x2:.2f}")