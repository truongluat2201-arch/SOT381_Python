from math import sqrt
n = int(input("Nhập số n: "))
t = 0
if n < 0:
    print("Không hợp lệ")
else:
    for i in range(2,n+1):
        rs = True
        for j in range(2,int(sqrt(i)+1)):
            if i % j == 0:
                rs = False
        if rs == True:
            t = t+1
print(f"Có {t} số nguyên tố trong [1,{n}]")
                
            