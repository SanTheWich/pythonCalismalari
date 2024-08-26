def soyle(xxx="Değer gönderilmedi"): # Değer alan fonksiyon
    print(xxx)

soyle()
soyle("Napıyon?")#gönderilen parametre


# örnek-5 default parametre sonda olur
def topla(a=10,b=0,c=0):
    return sum((a,b,c))
print(topla(b=5))
#!GLOBAL VARİABLE
x = 50
def fonksiyon1(a):
    print("1.Durum=",a)
    # print("2.Durum=",x) # x=.. dan önce kullanılamaz
    x=100
    print("3.Durum=",x)
fonksiyon1(20)
print("4.Durum=",x)

#! *args
def topla(*sayilar):
    print("Gelenler:",sayilar)
    toplamı=0
    for a in sayilar:
        toplamı+=a
    print(toplamı)
topla(10,20,30,60)

#! dictionary türünde kwargs !!iki tana kwargs kullanamıyoruz
def yaz(**xx):
    print(xx)
    print("Soyadı :" + xx["soyad"])#önemli
yaz(ad = "Eren", soyad = "AKIN")
#!LAMBDA λ
# ör-1 temel kullanım
print((lambda x:x**2)(5))

# ör-2
karesi = lambda n:n**2
print (karesi(4))
# ör-3 Uzun şekli
sayilar = [11,22,3]
def carp(xx): 
    return xx*2
yeniDizi = list(map(carp,sayilar))
print(yeniDizi)

# ör-2 lambda ile kısa şekli
sayilar = [11,22,3]
print(list(map(lambda a:a*2,sayilar))) 
#! MAP 
# map siz şekli
sayilar = [11,22,3]

def carp(xx): return xx*2

yeniDizi = []
for a in sayilar:    yeniDizi.append(carp(a))
   
print(yeniDizi)
###mapsiz dene
sayilar = [11,22,3]
def carp(xx):
    return xx*2

yeniDizi = list(map(carp,sayilar))
   
print(yeniDizi)
###
sayilar = [11,22,3,6,7]

# yeniDizi = list(filter(lambda x:True,sayilar))
yeniDizi = list(filter(lambda x: x%2==0,sayilar))
   
print(yeniDizi)

OgrenciNotları=[[10,30,40],[60,10],[70,80,90]]
def sinavKacirmayanlar(x):
    if len(x)>2: durum=True
    else: durum=False
    return durum
yeniDizi=list(filter(sinavKacirmayanlar,OgrenciNotları))
print(yeniDizi)
#! yield
def myFunc():
  yield "Hello"
  yield 51
  yield "Good Bye"

x = myFunc()

for z in x:
  print(z)