# Viết hàm kiểm tra số nguyên tố
def so_nguyen_to(n):
    kq = True
    if (n==1) and (n==2):
        kq = True
    else:
        for i in range(2,n):
            if n%i==0:
                kq = False
                break
    return kq

x=so_nguyen_to(7)
print(f"Kết quả kiểm tra là {x}")