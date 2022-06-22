class Titik: 
    def _init_ (self, x, y):
        self.x = x
        self.y = y

class Segitiga:
    def _init_ (self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    @property
    def luas(self) :
        return 0.5*abs(
            (self.a.x - self.c.x)*
            (self.b.y - self.a.y) -
            (self.a.x - self.b.x)*
            (self.c.y - self.a.y)
        )

#input
A = Titik (1,14) 
B = Titik (13,12)
C = Titik (4,9)
D = Titik (1,6)
E = Titik (12,8)
F = Titik (14,1)
G = Titik (5,4)
H = Titik (2,2)

poligon = [
    Segitiga (A, B, D),
    Segitiga (B, D, E),
    Segitiga (B, C, E),
    Segitiga (D, E, F),
]

#proses
luas = 0
for segitiga in poligon :
    luas += segitiga.luas

#output
print(luas)