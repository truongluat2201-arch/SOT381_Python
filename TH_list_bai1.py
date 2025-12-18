# Nhập 5 số từ bàn phím vào list và tính tổng
n = int(input("Nhập số lượng phần tử: "))
s = []
for i in range(n):
    a = int(input(f"s[{i}]= "))
    s.append(a)
print(s)
t = sum(s)
print(f"Tổng các số trong s là {t}")