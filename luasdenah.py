# from functools import reduce
 
class Ruangan:
	def __init__(self, panjang, lebar):
		self.panjang = panjang
		self.lebar = lebar
	@property
	def luas(self):
		return self.panjang * self.lebar
        # menghasilkan sebuah fungsi
 
bangunan = [
	Ruangan(3, 4),
	Ruangan(4, 3),
	Ruangan(4, 3),
	Ruangan(8, 5),
	Ruangan(3, 4),
	Ruangan(4, 3),
	Ruangan(4, 4),
	Ruangan(4, 4),
	Ruangan(4, 4),
]

# luas = reduce(lambda a, b: a + b.luas, bangunan, 0)
luas = 0
for ruangan in bangunan:
    luas += ruangan.luas()
print(luas)