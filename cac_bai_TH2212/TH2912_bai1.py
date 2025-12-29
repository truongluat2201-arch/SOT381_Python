toan = float(input("Nhập điểm môn toán: "))
ly = float(input("Nhập điểm môn lý: "))
hoa = float(input("Nhập điểm môn hóa: "))
tong = toan + ly + hoa
if tong >= 15:
    if (toan>4) and (ly>4) and (hoa>4):
        ket_qua = "Đậu"
        if (toan>5) and (ly>5) and (hoa>5) and (ket_qua == "Đậu"):
            print("Học đều các môn")
        else:
            print("Học chưa đều các môn")
    else:
        print("Thi rớt")
else:
    print("Thi hỏng")