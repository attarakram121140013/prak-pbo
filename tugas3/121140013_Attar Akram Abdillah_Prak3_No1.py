class AkunBank:
    #Declaring list data pelanggan
    list_pelanggan = []

    #Inialisasi data pelanggan
    def __init__(self, no_pelanggan, nama_pelanggan, __jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = __jumlah_saldo
        #Penambahan data pelanggan ke list
        AkunBank.list_pelanggan.append([no_pelanggan, nama_pelanggan, __jumlah_saldo])

    #Method untuk menampilkan menu
    def lihat_menu(self):
        print()
        print("Selamat datang di Bank Jago")
        print("Halo " + self.__nama_pelanggan + ", ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")

    #Method untuk menampilkan nilai saldo
    def lihat_saldo(self):
        print()
        print(self.__nama_pelanggan + " memiliki saldo Rp " + str(self.__jumlah_saldo))

    #Method unutuk melakukan penarikan saldo    
    def tarik_tunai(self):
        done = False
        while done == False:
            print()
            jumlah = input("Masukkan jumlah nominal yang ingin ditarik: ")
            jumlah = int(jumlah)
            
            if(jumlah > self.__jumlah_saldo):
                print()
                print("Nominal saldo yang Anda punya tidak cukup!")
            else:
                print()
                self.__jumlah_saldo -= jumlah
                print("Saldo berhasil ditarik!")
                done = True
                
    #Method untuk melakukan pemindahan saldo ke rekening lain
    def transfer(self, rek_tujuan, jumlah):
        check = False
        
        for i in range (0, len(AkunBank.list_pelanggan), 1):
            if rek_tujuan == AkunBank.list_pelanggan[i][0]:
                nama = AkunBank.list_pelanggan[i][1]
                x = i
                check = True
            else:
                pass
        
        if jumlah > self.__jumlah_saldo:
            print()
            print("Nominal saldo yang Anda punya tidak cukup! Kembali ke menu utama...")
        elif check == True:
            AkunBank.list_pelanggan[x][2] += jumlah
            self.__jumlah_saldo -= jumlah
            print()
            print("Transfer Rp " + str(jumlah) + " ke " + nama + " sukses!")

            if Akun2.__no_pelanggan == rek_tujuan:
                Akun2.__jumlah_saldo += jumlah
            elif Akun3.__no_pelanggan == rek_tujuan:
                Akun3.__jumlah_saldo += jumlah
        else:
            print()
            print("No rekening tujuan tidak dikenal! Kembali ke menu utama...")

#Pembuatan objek
Akun1 = AkunBank(1234, "Attar Akram Abdillah", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

#Constrain main program
progressing = True

#Main program
while progressing == True:
    Akun1.lihat_menu()
    comm = input("Masukkan nomor input: ")
    comm = int(comm)

    if comm == 1:
        Akun1.lihat_saldo()
    elif comm == 2:
        Akun1.tarik_tunai()
    elif comm == 3:
        print()
        jumlah = input("Masukkan nominal yang ingin ditransfer: ")
        jumlah = int(jumlah)
        rek_tujuan = input("Masukkan no rekening tujuan: ")
        rek_tujuan = int(rek_tujuan)
        Akun1.transfer(rek_tujuan, jumlah)
    elif comm == 4:
        progressing = False
    else:
        print("Invalid input!")

print()
print("Bank Jago, transaksi aman, nyaman, terpercaya")





    
