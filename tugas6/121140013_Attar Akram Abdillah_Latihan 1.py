from abc import ABC
from abc import abstractmethod

class AkunBank(ABC):
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo

    def lihat_saldo(self):
        if self.saldo > 0:
            print(self.saldo)
        else:
            print(self.nama + " Miskin")

    @abstractmethod
    def transfer_saldo(self, jumlah):
        pass

    @abstractmethod
    def lihat_sukubunga(self):
        pass


class AkunGold(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)

    def transfer_saldo(self, jumlah):
        if jumlah > 100000:
            if 2023 - self.tahun_daftar >= 3:
                self.saldo -= jumlah
            else:
                self.saldo -= (jumlah + 2000)
        else:
            self.saldo -= jumlah

    def lihat_sukubunga(self):
        if self.saldo >= 1000000000:
            if 2023 - self.tahun_daftar >= 3:
                print("Bunga bulanan sebesar 1%")
            else:
                print("Bunga bulanan sebesar 2%")
        else:
            print("Bunga bulanan sebesar 3%")


class AkunSilver(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)

    def transfer_saldo(self, jumlah):
        if jumlah > 100000:
            if 2023 - self.tahun_daftar >= 3:
                self.saldo -= (jumlah + 2000)
            else:
                self.saldo -= (jumlah + 5000)
        else:
            self.saldo -= jumlah

    def lihat_sukubunga(self):
        if self.saldo >= 10000000:
            if 2023 - self.tahun_daftar >= 3:
                print("Bunga bulanan sebesar 1%")
            else:
                print("Bunga bulanan sebesar 2%")
        else:
            print("Bunga bulanan sebesar 3%")

Budi = AkunGold("Budi", 2020, 10000000000)
Andi = AkunSilver("Andi", 2021, 10000000)
John = AkunSilver("John", 2023, 0)


Budi.lihat_saldo()
Budi.transfer_saldo(200000)
Budi.lihat_sukubunga()
Budi.lihat_saldo()

Andi.lihat_saldo()
Andi.transfer_saldo(200000)
Andi.lihat_sukubunga()
Andi.lihat_saldo()

John.lihat_saldo()
