class Data:

    def __init__(self, nama, nim, kelas, jumlah_sks):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.jumlah_sks = jumlah_sks

    def get_id(self):
        print("Berikut data diri mahasiswa:")
        print("Nama: ", self.nama)
        print("NIM: ", self.nim)
        print("Kelas : ", self.kelas)
        print("Jumlah SKS: ", self.jumlah_sks)
        print()

    def set_id(self, new_nama, new_nim, new_kelas, new_jumlah_sks):
        self.nama = new_nama
        self.nim = new_nim
        self.kelas = new_kelas
        self.jumlah_sks = new_jumlah_sks
        print("Data berhasil diubah!")
        print()

    def switch_data(self, orang):
        temp_nama = self.nama
        temp_nim = self.nim
        temp_kelas = self.kelas
        temp_jumlah_sks = self.jumlah_sks

        self.nama = orang.nama
        self.nim = orang.nim
        self.kelas = orang.kelas
        self.jumlah_sks = orang.jumlah_sks

        orang.nama = temp_nama
        orang.nim = temp_nim
        orang.kelas = temp_kelas
        orang.jumlah_sks = temp_jumlah_sks

orang1 = Data("Attar", 121140013, "RB", 4)
orang1.get_id()
orang1.set_id("Budi", 121140413, "RC", 4)
orang1.get_id()

orang2 = Data("Andi", 121140421, "RA", 3)
orang3 = Data("Ricar D. Milos", 121140069, "RZ", 3)

orang1.set_id(orang2.nama, orang2.nim, orang2.kelas, orang2.jumlah_sks)
orang2.set_id("Zhong Lee", 123891011, "RD", 4)

orang4 = Data("Attar", 121140013, "RB", 4)

orang1.switch_data(orang2)

orang1.get_id()
orang2.get_id()
orang3.get_id()
orang4.get_id()
