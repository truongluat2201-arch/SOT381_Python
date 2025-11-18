loai_xe = input("Nhập loại xe: ") #"xe_may","o_to"
so_gio = float(input("Nhập số giờ: "))
if loai_xe == "xe_may" :
    if so_gio <= 2 :
        tien = 5000 * so_gio
    else :
        tien = 5000 * 2 + 2000 * (so_gio - 2)
else :
    if so_gio == 1 :
        tien = 20000
    else:
        tien = 20000 + 15000 * (so_gio - 1)
print(f"Số tiền đỗ xe {so_gio} giờ của bạn là {tien:,.0f} đồng")