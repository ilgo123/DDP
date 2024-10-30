# SOAL NO 1
kendaraan = ["Vario", "Matic", 150, "Putih", 2]
print(kendaraan, '\n\n')

kendaraan.append(30000000)
kendaraan.append("Motor Matic/Scooter")
print(kendaraan, '\n\n')

kendaraan.insert(2, "Honda")
print(kendaraan, '\n\n')


# SOAL NO 2
i = int(input("Ketik 1 jika menghitung Luas Persegi\nKetik 2 jika menghitung Luas Lingkaran\nKetik 3 jika menghitung Luas Segitiga\n"))

match i:
    case 1:
        s = int(input("Masukkan sisi yang dihitung : ")) 
        
        print(f"Luas Persegimu adalah {s**2}")
    case 2: 
        r = int(input("Masukkan jari jari dari lingkaran : "))
        checkR = r/7
        phi = None
        if r % 7 == 0:
            phi = 22/7
        else:
            phi = 3.14

        print(f"Luas Lingkarannya adalah {phi * r ** 2}")
    case 3:
        a = int(input("Masukkan alas dari segitiga : "))
        t = int(input("Masukkan tinggi dari segitiga : "))

        print(f"Luas Segitiganya adalah {a * t / 2}")
    case _:
        print("PILIHLAH SESUAI INSTRUKSI")
