mat_khau = input("Nhập mật khẩu: ")
do_dai = len(mat_khau)
if do_dai < 8 :
    ket_qua = "Mật khẩu yếu"
elif 8 < do_dai < 12 :
    ket_qua = "Mật khẩu trung bình"
else :
    ket_qua = "Mật khẩu mạnh"
print(f"Mật khẩu của bạn là loại {ket_qua}")