# Đếm từ 1 đến n số có bao nhiêu số chẳn, bao nhiêu số lẻ
n = int(input("Nhập số n: "))
chan = 0
le = 0
for i in range(1,n+1):
    if i%2==0:
        chan = chan + 1
    else:
        le = le + 1
print(f"Có {chan} số Chẵn và {le} số lẻ")
