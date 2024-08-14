def ornekler():
    print("Selam")
    import time,datetime,os
    time.sleep(2)### 2 saniye bekleyip yazıyo
    print("Adım Yasin")
    time.sleep(4)
    os.system("cls")##terminali temizler
import time,datetime,os
def anlikSaat():
    for i in range(10000):
        time.sleep(1)
        os.system("cls")
        print("Saat:", datetime.datetime.now().strftime("%H:%M:%S"))
def saat():
    import datetime
    print ("Bugün: ",datetime.date.today())
    tarih=datetime.date.today()
    print("Bu yıl: ",str(tarih)[0:4])
    print(f"Formatlanmis tarih: {str(tarih)[0:4]} {str(tarih)[5:7]}")
def mathLib():
    import math
    print(math.sqrt(9))
#!Help
def string():
    a=(input("Adın ne?"))
    print(a.upper())#büyültür
    print(a.lower())
    print(a.capitalize())
    print(a.title())
#! WHİLE
def meyve():
    a=1
    while a<10:
        print(a)
        a+=1
    meyveler=[]
    meyve=" "
    while meyve!="":
        meyve=input("Meyve giriniz: ")
        if meyve !="": meyveler.append(meyve)
    print("Girdiğiniz meyveler: ",*meyveler,sep="\n")
    import random
    print(random.choice(meyveler))#ne yiycez
#! İKİ BOYUTLU DİZİLER
a=[1,2,3]#tek boyutlu
_11a =["Başak","YASİN","AHMET"]
_11b =["keko","burak"]
arkadasGrubu=[_11a,_11b]
print(arkadasGrubu[0][1])#0. satırın 1. elemanı
arkadasGrubu[1].append("ÖMER")
print(arkadasGrubu[1])
