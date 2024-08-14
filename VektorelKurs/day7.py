# -- KISAYOLLAR 
# # -- CTRL D = AYNI OLAN HEPSİNİ SEÇİYOR 
#      dene
#      dene
# -- HOME BAŞA 
# -- END SONA
# alt shift aşağı ok
# alt shift aşağı ok olduğun satırı altına kopyalıyor
#ctrl+enter yan sekmede açma
""""
#! Arrayler
List ler sırasız ve değiştirilebilirdir. Aynı değerden iki tane barındırabilir. [ ]
Tuple lar sıralı ve değiştirilemezdir. Aynı değerden iki tane barındırabilir. ()
Set ler sıralı ve indexlenmiş değillerdir. Aynı değerden iki tane içeremez.
Dictionary ler sıralı ve değiştirilebilirdir. Aynı değerden iki tane içeremez.
String ifadeler de bir tür dizidir.
meyveler = ["elma", "muz", "kiraz"]
print (meyveler)
+ ile ekleme
meyveler += ["muz","karpuz"]
print (meyveler)
yeniMeyveler = ["muz","nar"]
meyveler += yeniMeyveler 
print(meyveler)
Append ile istede sona eleman ekleme
meyveler.append("karpuz")
meyveler.append("erik")
print (meyveler)
Insert ile istede araya eleman ekleme
meyveler.insert(2,"muz")
print (meyveler)
extend ile tek tek ekleme
yeniMeyveler = ["nar","muz"]
meyveler.extend(yeniMeyveler)
print(meyveler)
meyveler.extend("erik")
print(meyveler) 
!!!!!!!!!!!!!!
#!Listelerden eleman çıkarma(silme)
Elaman silmek için pop ve remove metodlarını kullanabilirsiniz
dizi=[“elma”,”muz”,”kiraz”,”kavun”]
dizi.pop() # Listeden eleman silme son elemanı sil
dizi.remove(“muz”) # ilk muzu sil
dizi.pop[2:4]
dizi.remove()
meyveler = ["elma", "muz", "kiraz"]
meyveler.pop()
print (meyveler)
meyveler.remove("muz")
print (meyveler)
#!
Listeyi sıralama
dizi=[“elma”,”armut”,”kiraz”,”kavun”]
dizi.sort() 
print (dizi)
Tersten sıralama
dizi.sort(reverse=true)
print (dizi)
dizi.reverse()
print(dizi)
İçindeki bazı değerleri sayma
say = dizi.count(“ankara”)
print (say)
#!
dizi = list("erdinc donmez")
print (len(dizi)) # Listenin uzunluğu 

print(dizi)
dizi = [1,2,3,4,5,6]
dizi*2

print(dizi[::-1]) # terse çevir

liste içinde eleman var mı bakma
thislist = ["elma", "muz", "kiraz"]
if "elma" in thislist:
  print("Evet, 'elma' listede var.")
"""
ogrenciler = ["Ali","Can","Han","Ece"]
print(f"{ogrenciler}")
a=1
for a in range(len(ogrenciler)):
    print(f"{ogrenciler[a]}")
    a+=1
ogrenciler.append("Yasin")#liste sonuna ekler
ogrenciler.append("Ahmet")#
ogrenciler.insert(1,"Başak")#belirtilen yere ekleme yapar
print(ogrenciler[1:3])#1. ve3. idexksekadar yazar
print(ogrenciler.index("Can"))
ogrenciler.pop(4)#4. elemanı siler
print(ogrenciler)
#!Çekiliş yap
for a in range():
    a=1
    print("DÖngü")
    