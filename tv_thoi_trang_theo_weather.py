nhiet_do = float(input("Nhập nhiệt độ (độ C): "))
thoi_tiet = input("Nhập thời tiết: ") #"Nắng","Mưa","Âm u"
if thoi_tiet == "Mưa" :
    ket_qua = "Nhớ mang áo mưa hoặc ô"
elif nhiet_do > 30 :
    ket_qua = "Mặc đồ thoáng mát,cẩn thận say nắng."
elif thoi_tiet == "Nắng" and 20 < nhiet_do < 30 :
    ket_qua = "Thời tiết đẹp,mặc đồ thoải mái"
else :
    ket_qua = "Trời lạnh,nhớ mặc áo khoác"
print(f"Hôm nay {ket_qua}")
    