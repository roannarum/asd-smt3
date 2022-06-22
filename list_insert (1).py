from time import time

awal = time()
daftar = []
for i in range(100_000):
    daftar.insert(0, i + 1)
akhir = time()
waktu = akhir - awal
print(waktu)
