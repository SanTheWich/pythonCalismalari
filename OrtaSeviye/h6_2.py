# class ilan():
#     aktiflik = True
#     def __init__(self, no, bas):
#         self.ilanNo=no
#         self.baslik=bas
    
#     def ilanBilgisi(self):
#         print("No: ",self.ilanNo, "Baslik :",self.baslik)

# ilan1148975819 = ilan(1148975819,"Pıtır Pıtır Şahin")    
# ilan1587458956 = ilan(1587458956,"TOROS")  

# ilan1148975819.ilanBilgisi()
# ilan1587458956.ilanBilgisi()
#! Miras alma
class Calisan():
    Odulleri=""
    Rutbesi=""
    def __init__(self,tc="---",adSoyad="***"):
        self.TCKN=tc
        self.AdiSoyadi=adSoyad
    def CalisanBilgisi(self):
        print("Çalışan bilgileri: Adı Soyadı:",self.AdiSoyadi,"")
calisan1= Calisan("ERDİNÇ DÖNMEZ","123456")
calisan1.CalisanBilgisi()

class Idareci(Calisan):
    ekUcret=0

calisan2=Idareci("Ozan Can","98869412")
