print("=== MÁY TÍNH ĐƠN GIẢN ===")
num1=float(input("Nhập số thứ nhất: "))
num2=float(input("Nhập số thứ hai: "))
operation=input("Nhập phép toán (+,-,*,/): ")
if operation == "+" :
    result = num1 + num2
    print(f"{num1}+{num2}={result}")
elif operation =="-" :
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation =="*" :
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/" :
    if num2 !=0 :
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else :
        print("Lỗi: Không thể chia cho 0 !")
else:
    print("Phép tính không hợp lệ")