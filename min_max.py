# Cho một danh sách các số: numbers = [10, 5, 8, 20, 3, 15]. Hãy tìm số lớn nhất và số nhỏ nhất trong danh sách này mà không dùng hàm max() hay min()
numbers = [10, 5, 8, 20, 3, 15]
so_lon_nhat = numbers[0]
so_nho_nhat = numbers[0]
for num in numbers:
    if num > so_lon_nhat :
        so_lon_nhat = num
    if num < so_nho_nhat :
        so_nho_nhat = num
print(f"Số lớn nhất trong danh sách là {so_lon_nhat}")
print(f"Số nhỏ nhất trong danh sách là {so_nho_nhat}")