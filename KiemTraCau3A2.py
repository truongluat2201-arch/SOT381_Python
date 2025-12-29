n = int(input("Nhập số lượng phần tử: "))
ds_so = []
tong_chan = 0
for i in range(n):
    a = int(input(f"Nhập số thứ {i}: "))
    ds_so.append(a)
print("Danh sách các số nguyên vừa nhập",ds_so)
for j in range(0,len(ds_so),2):
    tong_chan = tong_chan + ds_so[j]
print(f"Tổng các số tại vị trí chẵn trong danh sách là {tong_chan}")