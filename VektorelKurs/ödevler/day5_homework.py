for a in range (10):
    print(f"{a}")
#
for a in range (1,10):
    print(f"{a}")
#12’den 50’ye (50 dahil) kadar saydır.
for a in range (12,51):
    print(f"{a}")
#30’den 100’e (100 dahil) kadar 5’er saydır.
for a in range (30,101,5):
    print(f"{a}")
#Geri sayım sayacı yapınız. 
for zzz in range(10, -1, -1): print(zzz)
#100’den 40’a kadar (40 dahil) 5’er geri saydır
for a in range(100,40,-5):
    print(f"{a}")
#Kaça kadar sayayım diye sor ve saydır.
num=int(input("Kaça kadar sayayım"))
for a in range(num):
    print(f"{a}")
#Kaça kadar sayayım diye sor ve saydır.
num1=int(input("Kaçtan sayayım"))
num2=int(input("Kaça kadar sayayım"))
for a in range(num2,num1):
    print(f"{a}")
#Kaçtan kaça kadar kaçar kaçar sayacağını sor ve saydır. 
num1=int(input("Kaçtan sayayım: "))
num2=int(input("Kaça kadar sayayım: "))
num3=int(input("Kaçar sayayım: "))
for a in range(num2,num1,num3):
    print(f"{a}")
#Programı kullanan kişinin adını, yaşı sayısınca yazdırın.
ad=str(input("Adınız nedir: "))
yas=str(input("yasınız nedir: "))
for a in range(yas):
    print(f"{ad}")
#Çarpım tablosunu ekrana yazdırın.
for a in range(10):
    for b in range (10):
        print(f"{a}x{b}={a*b}")