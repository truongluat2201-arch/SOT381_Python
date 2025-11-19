so_gio_lam = float(input("Nhập số giờ làm việc: "))
muc_luong = float(input("Nhập mức lương mỗi giờ: "))
# Giờ chuẩn là 40 giờ/tuần
if so_gio_lam <= 40 :
    luong = so_gio_lam * muc_luong
else :
    luong = (40 * muc_luong) + ((so_gio_lam - 40) * muc_luong * 1.5)
print(f"Số tiền lương nhận được là {luong:,.0f}")
    