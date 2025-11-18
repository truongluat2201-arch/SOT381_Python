chieu_cao = float(input("Nhập chiều cao (m): "))
can_nang = float(input("Nhập cân nặng (kg): "))
bmi = can_nang / (chieu_cao**2)
if bmi < 18.5 :
    danh_gia = "Gầy"
elif bmi < 25 :
    danh_gia = "Bình thường"
elif bmi <30 :
    danh_gia = "Tiền béo phì"
else:
    danh_gia = "Béo phì"
print(f"BMI là: {bmi:.1f} - {danh_gia}")