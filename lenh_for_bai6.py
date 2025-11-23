# in ra các số chẵn từ 1 đến n
n= int(input("Nhập số n: "))
for i in range(1,n+1):
    if i%2==0 :
        print(i, end=" ")