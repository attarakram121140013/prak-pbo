# Definisi Kelas Parent Robot
class Robot:

    jumlah_turn = 1

    def __init__(self, nama, health, damage):
        self.nama = nama
        self.health = health
        self.damage = damage

    def lakukan_aksi(self, target, status):
        if status == "menang":
            target.health -= self.damage
            print("Robotmu (" + self.nama + ") menyerang sebanyak " + str(self.damage) + " DMG")
            print()
            jumlah_turn += 1
        else:
            target.health -= self.damage
            print("Robot lawan (" + self.nama + ") menyerang sebanyak " + str(self.damage) + " DMG")
            print()
            jumlah_turn += 1

# Definisi Kelas Anak Antares
class Antares(Robot):

    def __init__(self, nama, health, damage):
        super().__init__(nama, health, damage)

    def lakukan_aksi(self, target, status):
        if status == "menang":
            if Robot.jumlah_turn % 3 == 0:
                self.damage = self.damage * 1.5
                target.health -= self.damage
                print("Robotmu (" + self.nama + ") menyerang sebanyak " + str(self.damage) + " DMG")
                print()
                self.damage = self.damage - (self.damage/3)
                Robot.jumlah_turn += 1
            else:
                target.health -= self.damage
                print("Robotmu (" + self.nama + ") menyerang sebanyak " + str(self.damage) + " DMG")
                print()
                Robot.jumlah_turn += 1
        else:
            if Robot.jumlah_turn % 3 == 0:
                self.damage = self.damage * 1.5
                target.health -= self.damage
                print("Robot lawan (" + self.nama + ") menyerang sebanyak " + str(self.damage) + " DMG")
                print()
                self.damage = self.damage - (self.damage/3)
                Robot.jumlah_turn += 1
            else:
                target.health -= self.damage
                print("Robot lawan (" + self.nama + ") menyerang sebanyak " + str(self.damage) + " DMG")
                print()
                Robot.jumlah_turn += 1

# Definisi Kelas Anak Alphasetia
class Alphasetia(Robot):
    
    def __init__(self, nama, health, damage):
        super().__init__(nama, health, damage)

    def lakukan_aksi(self, target, status):
        if status == "menang":
            if Robot.jumlah_turn % 2 == 0:
                self.health += 4000
                target.health -= self.damage
                print("Robotmu (" + self.nama + ") menambah darah sebanyak 4000 HP")
                print("Robotmu (" + self.nama + ") menyerang sebanyak " + str(self.damage) + " DMG")
                print()
                Robot.jumlah_turn += 1
            else:
                target.health -= self.damage
                print("Robotmu (" + self.nama + ") menyerang sebanyak " + str(self.damage) + " DMG")
                print()
                Robot.jumlah_turn += 1
        else:
            if Robot.jumlah_turn % 2 == 0:
                self.health += 4000
                target.health -= self.damage
                print("Robot lawan (" + self.nama + ") menambah darah sebanyak 4000 HP")
                print("Robot lawan (" + self.nama + ") menyerang sebanyak " + str(self.damage) + " DMG")
                print()
                Robot.jumlah_turn += 1
            else:
                target.health -= self.damage
                print("Robot lawan (" + self.nama + ") menyerang sebanyak " + str(self.damage) + " DMG")
                print()
                Robot.jumlah_turn += 1
       

# Definisi Kelas Anak Lecalicus
class Lecalicus(Robot):

    def __init__(self, nama, health, damage):
        super().__init__(nama, health, damage)

    def lakukan_aksi(self, target, status):
        if status == "menang":
            if Robot.jumlah_turn % 4 == 0:
                self.health += 7000
                self.damage = self.damage * 2;
                target.health -= self.damage
                print("Robotmu (" + self.nama + ") menambah darah sebanyak 7000 HP")
                print("Robotmu (" + self.nama + ") menyerang sebanyak " + str(self.damage) + " DMG")
                print()
                self.damage = self.damage - (self.damage/2)
                Robot.jumlah_turn += 1
            else:
                target.health -= self.damage
                print("Robotmu (" + self.nama + ") menyerang sebanyak " + str(self.damage) + " DMG")
                print()
                Robot.jumlah_turn += 1
        else:
            if Robot.jumlah_turn % 4 == 0:
                self.health += 7000
                self.damage = self.damage * 2;
                target.health -= self.damage
                print("Robot lawan (" + self.nama + ") menambah darah sebanyak 7000 HP")
                print("Robot lawan (" + self.nama + ") menyerang sebanyak " + str(self.damage) + " DMG")
                print()
                self.damage = self.damage - (self.damage/2)
                Robot.jumlah_turn += 1
            else:
                target.health -= self.damage
                print("Robot lawan (" + self.nama + ") menyerang sebanyak " + str(self.damage) + " DMG")
                print()
                Robot.jumlah_turn += 1
        
#Inisiasi Objek
robot1 = Antares("Antares", 50000, 5000)
robot2 = Alphasetia("Alphasetia", 40000, 6000)
robot3 = Lecalicus("Lecalicus", 45000, 5500)

#Pemilihan Robot
choice = input("Pilih robotmu! (1 = Antares, 2 = Alphasetia, 3 = Lecalicus):")
if choice == "1":
    p1 = robot1
elif choice == "2":
    p1 = robot2
elif choice == "3":
    p1 = robot3

choice = input("Pilih robot lawan! (1 = Antares, 2 = Alphasetia, 3 = Lecalicus):")
if choice == "1":
    p2 = robot1
elif choice == "2":
    p2 = robot2
elif choice == "3":
    p2 = robot3

print()
print("Pertarungan Dimulai!")
print()

#Pendefinisian variabel pembantu
end = False
i = 1

#Pertandingan
while end != True:
    print("Turn saat ini: " + str(p1.jumlah_turn))
    print("Robotmu (" + p1.nama + ") - " + str(p1.health) + " HP, robot lawan (" + p2.nama + ") - " + str(p2.health) + " HP)")

    #Input Aksi dan Penentuan Pilihan Aksi Bot
    a = input("Pilih seranganmu! (1 = gunting, 2 = batu, 3 = kertas):")
    a = int(a)
    if i == 1:
        if p2.nama == "Antares":
            b = 1
        elif p2.nama == "Alphasetia":
            b = 2
        elif p2.nama == "Lecalicus":
            b = 3
    elif i > 1:
        if Robot.jumlah_turn % 2:
            b += 1
        else:
            b += 2

        if b == 6:
            b -= 5
        elif b == 5:
            b -= 4
        elif b == 4:
            b -= 2
    i += 1

    #Pemutusan Pemenang Ronde dan Pelaksanaan Aksi
    if a == b:
        print("Draw!")
        Robot.jumlah_turn += 1
    elif a == 1 and b == 3:
        status = "menang"
        p1.lakukan_aksi(p2, status)
    elif a == 2 and b == 1:
        status = "menang"
        p1.lakukan_aksi(p2, status)
    elif a == 3 and b == 2:
        status = "menang"
        p1.lakukan_aksi(p2, status)
    else:
        status = "kalah"
        p2.lakukan_aksi(p1, status)

    #Pengecekan Berakhir Tidaknya Pertandingan
    if p1.health <= 0:
        print("Robotmu kalah!")
        end = True
    elif p2.health <= 0:
        print("Robotmu menang!")
        end = True
