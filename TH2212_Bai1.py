w = float(input("Nhập chiều rông (m): "))
h = float(input("Nhập chiều dài (m): "))
if (w <= 0) and (h >= 100):
    print("Dữ liệu nhập không hợp lệ")
else:
    cv = (h + w)*2
    dt = h*w
print(f"Chu vi hình chữ nhật là {cv:.2f} m")
print(f"Diện tích hình chữ nhật là {dt:.2f} m")