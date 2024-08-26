# class Ogrenci:
#     ad = "---"
#     soyad = ""
#     numara = ""
#     notOrtalamasi = ""
#     disiplinCezasi = 0

# print("Sınıftaki ad değeri:",Ogrenci.ad)
# ogrenci1 = Ogrenci()
# ogrenci2 = Ogrenci()

# ogrenci1.ad = "Ali"
# ogrenci2.ad = "Veli"

# print("ogrenci1 nesnesinin ad değeri:",ogrenci1.ad)
# print("ogrenci1 nesnesinin ad değeri:",ogrenci2.ad)

# print("Sınıftaki ad değeri:",Ogrenci.ad)

class Ogrenci:
    AdSoyad = "Tanımsız"
    NotOrtalamasi = ""
    DisiplinCezasi = 0

    def __init__(self,ad="Tanımsız",no=0):
        self.AdSoyad = ad
        self.Numara = no 
        
    def Bilgi(self):
        print ("Metod ile: Adı Soyadı:",self.AdSoyad,", Numarası:",self.Numara)

print("Sınıftaki adSoyad değeri:",Ogrenci.AdSoyad)

ogrenci1 = Ogrenci("Ahmet BAL",10)
ogrenci2 = Ogrenci("Mehmet GÜL")
ogrenci3 = Ogrenci()
ogrenci4 = Ogrenci(no=42)

ogrenci1.Bilgi()
ogrenci2.Bilgi()
ogrenci3.Bilgi()
ogrenci4.Bilgi()

