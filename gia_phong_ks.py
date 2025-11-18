loai_phong = input("Nhập loại phòng: ") #"Standard","Deluxe","Suite"
so_dem = int(input("Nhập số đêm: "))
if so_dem > 3 :
    if loai_phong == "Standard" :
        gia_phong = (1000000 - (1000000 * 10/100)) * so_dem
    elif loai_phong == "Deluxe" :
        gia_phong = (1500000 - (1500000* 10/100)) * so_dem
    else :
        gia_phong = (2500000 - (2500000 * 10/100)) * so_dem
else :
    if loai_phong == "Standard" :
        gia_phong = 1000000 * so_dem
    elif loai_phong == "Deluxe" :
        gia_phong = 1500000 * so_dem
    else :
        gia_phong = 2500000 * so_dem
print(f"Giá phòng ở {so_dem} đêm là {gia_phong:,.0f} đồng ")
