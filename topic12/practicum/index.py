from burung import Burung
from ikan import Ikan
from ular import Ular

# Membuat objek dari setiap class
elang = Burung('Elang', 2, 'Cokelat', 'Tajam')
merpati = Burung('Merpati', 2, 'Abu-abu', 'Tumpul')

hiu = Ikan('Hiu', 'Insang Pipih', 15, 'Abu-perak')
salmon = Ikan('Salmon', 'Insang Panjang', 8, 'Oranye')

kobra = Ular('Kobra', 1.5, 'Mematikan', 'Hitam Kuning')
boa = Ular('Boa', 2.3, 'Tidak Berbisa', 'Cokelat Loreng')

# Menampilkan informasi dan method untuk Burung
print("--- Burung Elang ---")
elang.display_info()
elang.terbang()
elang.display_ciri_khusus()
elang.bersuara()

print("\n--- Burung Merpati ---")
merpati.display_info()
merpati.terbang()
merpati.display_ciri_khusus()
merpati.bersuara()

# Menampilkan informasi dan method untuk Ikan
print("\n--- Ikan Hiu ---")
hiu.display_info()
hiu.berenang()
hiu.display_karakteristik()
hiu.berkembang()

print("\n--- Ikan Salmon ---")
salmon.display_info()
salmon.berenang()
salmon.display_karakteristik()
salmon.berkembang()

# Menampilkan informasi dan method untuk Ular
print("\n--- Ular Kobra ---")
kobra.display_info()
kobra.melata()
kobra.display_bahaya()
kobra.menyerang()

print("\n--- Ular Boa ---")
boa.display_info()
boa.melata()
boa.display_bahaya()
boa.menyerang()