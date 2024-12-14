from animal import Animal

class Burung(Animal):
    def __init__(self, name, sayap, warna_bulu, jenis_paruh):
        super().__init__(name, 'Biji-bijian & Serangga', 'Darat & Udara', 'Bertelur')
        self.sayap = sayap
        self.warna_bulu = warna_bulu
        self.jenis_paruh = jenis_paruh
    
    def terbang(self):
        print(f"{self.name} sedang terbang dengan {self.sayap} sayap")
    
    def display_ciri_khusus(self):
        print(f"Warna Bulu: {self.warna_bulu}")
        print(f"Jenis Paruh: {self.jenis_paruh}")
    
    def bersuara(self):
        if self.jenis_paruh == 'Tajam':
            print(f"{self.name} bersuara: KICAU KERAS!")
        else:
            print(f"{self.name} bersuara: kicau pelan")