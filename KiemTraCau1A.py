n = float(input("Nhập điểm trung bình: "))
if (n>10) and (n < 0):
    print("Điểm không hợp lệ")
else:
    if (8.0 < n < 10.0):
        print("Xếp loại giỏi")
    elif (6.5 < n < 8.0):
        print("Xếp loại khá")
    elif (5.0 < n < 6.5):
        print("Xếp loại trung bình")
    elif (3.5 < n < 5.0):
        print("Xếp loại yếu")
    else:
        print("Xếp loại kém")