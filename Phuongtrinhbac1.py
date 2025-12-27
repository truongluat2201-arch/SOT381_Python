# Giải phương trình bậc 1  ax + b = 0 với a,b là các số nguyên
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b/a
    print(f"Nghiệm của phương trình đã cho là x = {x}")