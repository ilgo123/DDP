from animal import Animal

class Ular(Animal):
    def __init__(self, name, panjang, jenis_bisa, warna_kulit):
        super().__init__(name, 'Tikus & Katak', 'Darat & Semak', 'Bertelur')
        self.panjang = panjang
        self.jenis_bisa = jenis_bisa
        self.warna_kulit = warna_kulit
    
    def melata(self):
        print(f"{self.name} melata sepanjang {self.panjang} meter")
    
    def display_bahaya(self):
        print(f"Jenis Bisa: {self.jenis_bisa}")
        print(f"Warna Kulit: {self.warna_kulit}")
    
    def menyerang(self):
        if self.jenis_bisa == 'Mematikan':
            print(f"{self.name} siap menyerang dengan racun mematikan!")
        else:
            print(f"{self.name} bersifat defensif")