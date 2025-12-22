ds_baihat = []
n =int(input("Nhập số lượng bài hát: "))
for i in range (1,n+1):
    ten_bh = input(f"Nhập tên bài hát thứ {i}: ")
    a = ds_baihat.append(ten_bh)
for bai in ds_baihat:
    print(bai)
# in hoa bài hát
for k in range(n):
    print(ds_baihat[k].upper())
# tìm tên bài hát có chữ yêu
for h in range(n):
    ten = ds_baihat[h]
    if (ten.find("yêu") != -1):
        print(ten)

# Tìm bài hát dài nhất
ten_bai_dai_nhat = ds_baihat[0]
so_tu_dai_nhat = len(ten_bai_dai_nhat.split())
vi_tri_cua_bai = 0
for t in range(n):
    ten_bai = ds_baihat[t]
    so_tu = len(ten_bai.split())
    if so_tu > so_tu_dai_nhat :
        ten_bai_dai_nhat = ten_bai
        so_tu_dai_nhat = so_tu
        vi_tri_cua_bai = i
print(ten_bai_dai_nhat, so_tu_dai_nhat)