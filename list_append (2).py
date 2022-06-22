from time import time

awal = time()
daftar = []
for i in range(10_000_000):
    daftar.append(i + 1)
daftar.reverse()
akhir = time()
waktu = akhir - awal
print(waktu)
