jumlah = 0
n = int(input("Masukan angka : "))

for i in range (1, n+1) :
    print (i, end = "")
    if i == n :
        print("=", end = "")
    else :
        print("+", end="")
    jumlah = jumlah + i

print(jumlah)

# atau
while n>0:
    jumlah = 0
    