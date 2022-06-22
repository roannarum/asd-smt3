from math import sqrt
class Titik :
	def __init__ (self, x, y):
		self.x = x
		self.y = y 

class Garis:
	def __init__(self, t1, t2):
		self.t1 = t1
		self.t2 = t2

	@property
	def jarak(self):
		x = self.t2.x - self.t1.x
		y = self.t2.y - self.t1.y
		return sqrt(x**2 + y**2)
		# return sqrt (((self.t2.x - self.t1.x)*2)+((self.t2.y - self.t1.y)*2))
#input
A, B = Titik(1, 14), Titik(13, 12)
C, D = Titik(4, 9), Titik(1, 6)
E, F = Titik(12, 8), Titik(14, 1)
G, H = Titik(5, 4), Titik(2, 2)

Jalan = [ 
	Garis(A, B),
	Garis(B, C),
	Garis(C, D),
	Garis(D, E),
	Garis(E, F),
	Garis(F, G),
	Garis(G, H)
]
#proses
total = 0 
for panjang in Jalan :
	total += panjang.jarak

print("Total panjang dari garis tersebut adalah",total)