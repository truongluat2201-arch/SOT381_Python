gt = float(input("Nhập giá trị đơn hàng (đ): "))
if gt > 500000 :
    pgh = "0đ"
elif 100000 < gt < 500000 :
    pgh = "20.000đ"
else :
    pgh = "35.000đ"
print(f"Đơn của bạn có phí giao hàng là {pgh}")