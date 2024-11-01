#Tugas Nomor 1 DDP

kendaraan = ["Honda", "Mobil", 1500, "Hitam", 4]
kendaraan.append(["150 juta", "Sedan"])
kendaraan.insert(2, "Honda")

print(kendaraan)

#tugas Nomor 2 DDP

pilihan = int(input("Masukkan pilihan (1: persegi, 2: lingkaran, 3: segitiga): "))

match pilihan:
    case 1:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        luas = sisi * sisi
        print("Luas persegi:", luas)
    case 2:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = 3.14 * jari_jari * jari_jari
        print("Luas lingkaran:", luas)
    case 3:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print("Luas segitiga:", luas)
    case _:
        print("Pilihan tidak valid")
