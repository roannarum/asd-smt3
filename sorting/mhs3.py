class Mahasiswa:
    def __init__(self, npm, nama, jk):
        self.npm = npm
        self.nama = nama
        self.jk = jk
    def __repr__(self):
        return f'Mahasiswa dgn NPM {self.npm} dan nama {self.nama} jenis kelamin {self.jk}'
    def __lt__(self, other):
        if self.jk != other.jk:
            return self.jk < other.jk
        return self.nama < other.nama

mhs = [
  Mahasiswa('21031', 'Barry Allen', 'L'),
  Mahasiswa('21020', 'Mary Jane', 'P'),
  Mahasiswa('21030', 'Bill Gates', 'L'),
  Mahasiswa('21032', 'Astuti', 'P'),
]

mhs.sort()

for m in mhs:
  print(m)
