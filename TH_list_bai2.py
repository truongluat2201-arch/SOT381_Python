# NHập list 10 số, tìm số lớn nhất và nhỏ nhất
n = int(input("Nhập số phần từ: "))
s = []
for i in range(n):
    a = int(input(f"s[{i}]= "))
    s.append(a)
print(f"Danh sách s = {s}")
mx = max(s)
mn = min(s)
print(f"Số lớn nhất trong s là {mx}")
print(f"Số nhỏ nhất trong s là {mn}")