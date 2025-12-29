n = int(input("Nhập số lượng phần tử: "))
ds_so = []
sl_chan = 0
for i in range(n):
    a = int(input(f"Nhập số thứ {i}: "))
    ds_so.append(a)
print("Danh sách các số nguyên vừa nhập",ds_so)
for j in ds_so:
    if j % 2 == 0:
        sl_chan = sl_chan + 1
print(f"Số lượng phần tử chẵn trong danh sách của bạn là {sl_chan}")

