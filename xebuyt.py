hk = input("Nhập loại hành khách: ") #"học sinh","sinh viên","người cao tuổi","thường"
if hk == "học sinh" :
    gia_ve = "3.000đ"
elif hk == "sinh viên" :
    gia_ve = "5.000đ"
elif hk == "người cao tuổi" :
    gia_ve = "Miễn phí"
else :
    gia_ve = "7.000đ"
print(f"Giá vé xe buýt của bạn là {gia_ve}")