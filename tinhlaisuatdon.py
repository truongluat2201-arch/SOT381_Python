so_tien_gui=float(input("Nhập số tiền gửi: "))
lai_suat=float(input("Nhập lãi suất: "))
so_thang=int(input("Nhập số tháng: "))
lai= (so_tien_gui*lai_suat/100*so_thang)/12
print(f"Số tiền lãi nhận được là: {lai}")