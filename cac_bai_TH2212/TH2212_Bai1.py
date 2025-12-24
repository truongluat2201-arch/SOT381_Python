while True:
    w = float(input("Nhập chiều rông (m): "))
    h = float(input("Nhập chiều dài (m): "))
    if (w >= 0.0) and (h <= 100.0):
        break
    else:
        print("Nhập sai dữ liệu")
cv = (h + w)*2
dt = h*w
print(f"Chu vi hình chữ nhật là {cv:.2f} m")
print(f"Diện tích hình chữ nhật là {dt:.2f} m")