# singly linked-list

class LLNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # metode untuk menambah nilai baru di belakang list
    def append(self, value):
        # buat node baru untuk menampung nilai
        node = LLNode(value)
        # kalo sudah ada isinya
        if self.tail is not None:
            # node terakhir disambung ke node baru
            self.tail.next = node
            # tandai node baru sebagai node terakhir
            self.tail = node
        # kalo masih kosong
        else:
            # jadikan node baru sebagai elemen pertama
            self.head = node
            # jadikan node baru sebagai elemen terakhir
            self.tail = node
    # metode untuk menyisipkan nilai baru di posisi sembarang
    def insert(self, pos, value):
        # buat node baru untuk menampung nilai
        node = LLNode(value)
        # cek apakah mau menyisipkan di bagian depan
        if pos == 0:
            # letakkan node baru di posisi sebelum node awal
            node.next = self.head
            # tandai node baru itu sebagai node awal
            self.head = node
        # kalo posisinya bukan bagian depan
        else:
            # telusuri posisi node sebelumnya
            prev = self.head
            for i in range(pos - 1):
                # jika sudah mencapai bagian akhir
                if prev.next is None:
                    # tambahkan saja node baru di bagian akhir
                    prev.next = node
                    self.tail = node
                    # selesai
                    return
                prev = prev.next
            # node baru disambung dengan node pada posisi yang ditentukan
            node.next = prev.next
            # letakkan node sebelumnya di depan node baru
            prev.next = node
    # metode untuk menghapus node pada posisi tertentu
    def delete(self, pos):
        # jika list kosong, jangan melakukan apa-apa
        if self.head is None: return
        # jika yang dihapus yg paling depan
        if pos == 0:
            # geser posisi head maju satu langkah
            self.head = self.head.next
        # jika yg dihapus posisi setelah node paling depan
        else:
            # telusuri node sebelum data yang dihapus
            prev = self.head
            for i in range(pos - 1):
                # jika mencapai bagian akhir, selesai
                if prev.next is None:
                    return
                prev = prev.next
            # arahkan node sebelum yang mau dihapus, agar
            # menunjuk ke node setelah yg mau dihapus
            prev.next = prev.next.next
    def values(self):
        result = []
        node = self.head
        while node is not None:
            result.append(node.value)
            node = node.next
        return result

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(5)
linked_list.insert(0, 7)
linked_list.insert(2, 6)
linked_list.insert(100, 8)
linked_list.delete(0)
linked_list.delete(2)
linked_list.delete(200)

print(linked_list.values())