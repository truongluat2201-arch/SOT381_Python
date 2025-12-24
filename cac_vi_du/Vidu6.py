full_name=input("Họ và tên: ")
birth_year=int(input("Nhập năm sinh: "))
height=float(input("Nhập chiều cao (m): "))
weight=float(input("Nhập cân nặng (kg): "))
bmi= weight / (height**2)
current_year= 2025
age= current_year - birth_year
print("\n" + "="*40)
print(f"Họ tên: {full_name:>20}")
print(f"Tuổi: {age:>23}")
print(f"Chiều cao: {height:>18.2f} m ")
print(f"Cân nặng: {weight:>18.1f} kg ")
print(f"BMI: {bmi:>17.2f}")
print("="*40)