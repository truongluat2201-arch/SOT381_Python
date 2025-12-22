ds_baihat = []
n =int(input("Nhập số lượng bài hát: "))
for i in range (1,n+1):
    ten_bh = input("Nhập tên bài hát: ")
    a = ds_baihat.append(ten_bh)

print(f"Danh sách bài hát gồm những bài sau {ds_baihat}")