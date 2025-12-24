# tìm các số chia hết cho 3 và 5
n = int(input("Nhập số n: "))
for i in range(1,n+1):
    if (i%3==0) and (i%5==0) :
        print(i, end=" ")