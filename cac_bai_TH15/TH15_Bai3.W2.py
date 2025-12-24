n = int(input("Nhập vào n: "))
if (n < 0) and (n > 10):
    print("Giai thừa không xác định")
else:
    tich = 1
    i = 1
    while i <= n:
        tich = tich * i
        i = i + 1
    print(f"{n}! là {tich}")
        
    
  
            