ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
if 1 <= thang <= 12 and 1 <= ngay <= 31 :
    if thang in [4,6,9,11] :
        if ngay > 30 :
            ket_qua = f"Tháng {thang} chỉ có tối đa 30 ngày"
        else :
            ket_qua = f"Ngày {ngay}/tháng {thang}/năm {nam} là hợp lệ"
    elif thang == 2 :
        nam_nhuan = (nam % 4 == 0 and nam % 100 != 0 ) or (nam % 400 == 0)
        if nam_nhuan == True :
            if ngay > 29 :
                ket_qua = f"Tháng 2 năm nhuận {nam} chỉ có 29 ngày"
            else :
                ket_qua = f"Ngày {ngay}/tháng {thang}/năm {nam} là hợp lệ"
        else :
            if ngay > 28 :
                ket_qua = f"Tháng 2 năm không nhuận {nam} chỉ có tối đa 28 ngày"
            else :
                ket_qua = f"Ngày {ngay}/tháng {thang}/năm {nam} là hợp lệ"
    else :
        if ngay > 31 :
            ket_qua = f"Tháng {thang} chỉ có tối đa 31 ngày"
        else :
            ket_qua = f"Ngày {ngay}/tháng {thang}/năm {nam} là hợp lệ"
else :
    ket_qua = f"Ngày {ngay}/tháng {thang}/năm {nam} không tồn tại"
print(ket_qua)
            
        

    