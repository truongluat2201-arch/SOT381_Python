n = int(input("Nhập số lượng phần tử: "))
ds_so = []
for i in range(n):
    a = int(input(f"Nhập số thứ {i}: "))
    ds_so.append(a)
print("Danh sách các số nguyên vừa nhập",ds_so)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
cac_so_nt = []
for k in ds_so:
    if is_prime(k):
        cac_so_nt.append(k)
print("Các số nguyên tố trong danh sách là", cac_so_nt)
so_luong = len(cac_so_nt)
print(f"Có tổng cộng {so_luong} số nguyên tố")