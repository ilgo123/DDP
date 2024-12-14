from animal import Animal

class Ikan(Animal):
    def __init__(self, name, jenis_insang, panjang_sirip, warna_sisik):
        super().__init__(name, 'Plankton & Kecil-kecil', 'Air', 'Bertelur')
        self.jenis_insang = jenis_insang
        self.panjang_sirip = panjang_sirip
        self.warna_sisik = warna_sisik
    
    def berenang(self):
        print(f"{self.name} sedang berenang dengan insang {self.jenis_insang}")
    
    def display_karakteristik(self):
        print(f"Panjang Sirip: {self.panjang_sirip} cm")
        print(f"Warna Sisik: {self.warna_sisik}")
    
    def berkembang(self):
        if self.panjang_sirip > 10:
            print(f"{self.name} sudah dewasa dan siap berkembang biak")
        else:
            print(f"{self.name} masih dalam tahap pertumbuhan")