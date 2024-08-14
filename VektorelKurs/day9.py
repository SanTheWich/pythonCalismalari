"""SINIF OBJE
"""
a = 12
b = "Vektörel"
print(b)
print(type(b))
print(a)
print(type(a))
# #! SINIFLAR ÖRNEK 1
# class Ogrenci: #Referans Model
#     adi = "Yasin"
#     soyadi = "KARABUDAK"
#     numarasi = "22243510069"
# ogrenci1= Ogrenci
# print("Öğrenci Bilgisi: ",Ogrenci.adi, Ogrenci.soyadi,  Ogrenci.numarasi)
# #! SINIFLAR ÖRNEK2
# class Ogrenci: #Referans Model
#     adi = "Yasin"
#     soyadi = "KARABUDAK"
#     no = "22243510069"
#     def __init__(self,xx="-",yy="*"):
#         self.ad=xx
#         self.no=yy

# print("Öğrenci Bilgisi: ",Ogrenci.adi, Ogrenci.soyadi,  Ogrenci.numarasi)
# ogrenci1=Ogrenci()
# print("o1: ",ogrenci1.adi)
# ogrenci2=Ogrenci()
# print("o2:",ogrenci2.no)



# ogrenci1.adi="Ahmet"
# print(ogrenci1.adi)
# ogrenci2.adi="Başak"
# print(ogrenci2.adi)
# ogrenci3=Ogrenci("ÖMER",66)
# ogrenci4=Ogrenci
# print(ogrenci1.no)
# print(ogrenci2.no)
# print(ogrenci3.no)
# print(ogrenci4.no)
#! day 10 tekrar
# class Ogrenci:
#     AdSoyad = "Tanımsız"
#     NotOrtalamasi= ""
#     disiplinCezasi=0
#     Ogrenciler=["Ogrenci listesi bos"]

#     def __init__(ddd,ad,no):
#         ddd.AdSoyad=ad
#         ddd.Numara= no
#         ddd.Ogrenciler.append(ad)
#     def bilgi(yyy):
#         print("Metod ile adı soyadı:",yyy.AdSoyad,", Numarasi:",yyy.Numara)
    
#     def ogrenci_Ekle(self,ww):
#         self.Ogrenciler.append(ww)

#     def ogrenci_listesi(self):
#         print("Öğgenciler listeleniyor")
#         print(*self.Ogrenciler,sep="\n")

# print("Sınıftaki adSoyad değeri: ",Ogrenci.AdSoyad)
# Ogrenci1=Ogrenci("AHMET KAYABAŞI",10)
# Ogrenci2=Ogrenci("YASİN KARABUDAK",66)
# Ogrenci1.bilgi()
# Ogrenci2.bilgi()
# Ogrenci1.ogrenci_listesi()
# Ogrenci1.ogrenci_Ekle("Başak")

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age 
# p1 = Person("John", 36)

# print(p1.name) 
# print(p1.age)  


class kisi:
  def __init__(self, ad, yas):#ilki self olmak zorunda değil
    self.adi = ad#parametreyi sona koy 
    self.yasi = yas 
    #def kisiEkleme():
        

p1 = kisi("yasin", 36)
        

print(p1.adi) 
print(p1.yasi)  