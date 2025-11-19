tong_thu_nhap = float(input("Nhập tổng thu nhập hàng tháng: "))
giam_tru_ban_than = 11000000
thu_nhap_chiu_thue = tong_thu_nhap - giam_tru_ban_than
if thu_nhap_chiu_thue <= 0 :
    ket_qua = 0
elif 0 < thu_nhap_chiu_thue < 5000000 :
    ket_qua = thu_nhap_chiu_thue * 5/100
else :
    ket_qua = thu_nhap_chiu_thue * 10/100
print(f"Số tiền thuế phải nộp là {ket_qua:,.0f} đồng")