class Uji:

    publik = None
    _terjaga = None
    __privat = None

    def __init__(self, publik, terjaga, privat):
        self.publik = publik
        self._terjaga = terjaga
        self.__privat = privat

    def tampilkan_public(self):
        print(self.publik)
        
    def _tampilkan_protected(self):
        print(self._terjaga)
        
    def __tampilkan_private(self):
        print(self.__privat)

    def tampilkan_private_2(self):
        self.__tampilkan_private()

class Uji2(Uji):

    def __init__(self, publik, terjaga, privat):
        Uji.__init__(self, publik, terjaga, privat)

    def tampilkan_protected_2(self):
        print(self._terjaga)

objek = Uji2("ini publik", "ini protected", "ini private")
objek1 = Uji("ini publik", "ini protected", "ini private")

#publik
print("cara 1:")
print(objek.publik)
print("cara 2:")
objek.tampilkan_public()
print()
#public bisa diakses dengan mudah secara global

#protected
print("cara 1:")
objek._tampilkan_protected()
print("cara 2:")
objek.tampilkan_protected_2()
print()
#protected tidak bisa dengan mudah diakses lewat global
#namun masih bisa diakses dari kelas lainnya, seperti pada cara 2

#private
print("cara 1:")
objek.tampilkan_private_2()
#private harus membuat sebuah fungsi akses untuk melakukan akses dari global
#itu dikarenakan private aksesnya terbatas pada kelas ia dideklarasikan saja
