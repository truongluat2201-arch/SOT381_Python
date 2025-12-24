# Kiểm tra số x có trong List không, nếu có thì ở vị trí nà
n = int(input("Nhập vào các phần tử: "))
x = int(input("Nhập  số cần kiểm tra: "))
s = []
for i in range(n):
    a = int(input(f"s[{i}]= "))
    s.append(a)
print(f"Danh sách s = {s}")
if x in s:
    vt = s.index(x)
    print(f"Số {x} có trong danh sách s, tại vị trí {vt}")
else:
    print(f"Số {x} không có trong danh sách s")
