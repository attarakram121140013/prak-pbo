no_soal = input("Masukkan nomor soal: ")

if no_soal == "1":
    n = input("Masukkan jumlah n = ")
    n = int(n)
    for i in range (0, n, 1):
        for j in range (0, n, 1):
            print('*', end = '')
        print()
elif no_soal == "2":
    for i in range (0, 4, 1):
        if i < 3:
            nama = input("Username anda : ")
            password = input("Password anda : ")

            if nama == "informatika" and password == "12345678":
                print("Berhasil login!")
                break
            else:
                print("Username atau password anda salah, coba lagi")
        else:
            print("Akun anda terblokir")
else:
    print("nomor soal tidak ada")
