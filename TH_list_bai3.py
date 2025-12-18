# Nhập list số nguyên, đếm số chẳn và số lẻ
n = int(input("Nhập số lượng phần tử: "))
chan = 0
le = 0
s = []
for i in range(n):
    a = int(input(f"s[{i}]= "))
    s.append(a)
print(f"Danh sách s = {s}")
for j in s:
    if j % 2 == 0:
        chan += 1
    else:
        le += 1
print(f"Số lượng số chẵn trong danh sách là {chan}")
print(f"Số lượng số lẻ trong danh sách là {le}")