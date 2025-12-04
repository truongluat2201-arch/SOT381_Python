n = int(input("Nhập số n: "))
if n < 0:
    print("Không hợp lệ")
elif n == 1:
    print(f"{n} không phải là số nguyên tố")
else:
    for i in range(2,n):
        if n % i == 0:
            print(f"{n} không phải số nguyên tố")
            break
        else:
            print(f"{n} là số nguyên tố")
            break
    
   
    
    