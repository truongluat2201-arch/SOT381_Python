while True:
    print("\n=== MENU ===")
    print("1. Xem lời chào")
    print("2. Tính bình phương")
    print("3. Xem bảng cửu chương")
    print("0. Exit")
    
    lua_chon= int(input("Chọn chức năng: ")) # chọn số
    if lua_chon == 1 :
        print("Xin chào python!")
    elif lua_chon == 2 :
        x = int(input("Nhập số cần tính bình phương: "))
        print(f"Bình phương của {x} là {x*x}")
    elif lua_chon == 3 :
        for i in range(1,11):
            print(f"\n=== Bảng cửu chương {i} ===")
            for j in range(1,11):
                k = i*j
                print(f"{i}*{j}={k}")
    else :
        print("Chào tạm biệt")
        break