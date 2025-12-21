# Viết hàm tìm số lớn nhất và số nhỏ nhất của 3 số a, b,c
def so(a,b,c):
    so_lon_nhat = max(a,b,c)
    so_nho_nhat = min(a,b,c)
    return so_lon_nhat, so_nho_nhat

x=so(5,6,7)
print(f"Số lớn nhất và số nhỏ nhất lần lượt là {x}")
