# Viết hàm tính chỉ số BMI và phân loại
def chi_so_bmi(w,h):
    bmi = (w / h**2)
    if bmi < 18.5:
        phan_loai = "Gầy"
    elif 18.5 <= bmi <= 25:
        phan_loai = "Bình thường"
    elif 25 <= bmi <= 30:
        phan_loai = "Tiền béo phì"
    elif 30 <= bmi<= 35:
        phan_loai = "Béo phì độ 1"
    elif 35 <= bmi <= 40:
        phan_loai = "Béo phì độ 2"
    else:
        phan_loai = "Béo phì độ 3"
    return round(bmi,2),phan_loai


x,u=chi_so_bmi(70,1.71)
print(f"Chỉ số BMI là {x} ")
print(f"Phân loại {u}")