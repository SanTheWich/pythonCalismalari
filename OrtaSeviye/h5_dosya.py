# #ASDA
# #!  "w" write üzerine yazar 
# abc = open("c:\\Users\\yasin\\Desktop\\Python\\OrtaSeviye\\rehber.txt", "w")
# abc.write("Dosyaya kayded-2.\nİkinci satır!!\n")
# abc.write("Üçüncü satır") 
# # abc.write("Üçüncü satır") 
# # abc.close() # oluşturulan her dosya kapatılmalıdır.
# #! "a" üzerine yazar iki kere çalıştırsan aynı şeylerden 2 tane olur
# abc = open("rehber.txt", "a")
# abc.write("Dosyaya kayded-2.\nİkinci satır!!\n")
# abc.write("Üçüncü satır") 
# abc.write("Üçüncü satır") 
# abc.close() # oluşturulan her dosya kapatılmalıdır.
#! "r" dosya içindekileri okur
# f = open("c:\\Users\\yasin\\Desktop\\Python\\OrtaSeviye\\demofile2.txt", "a")
# f.write("Dosyaya ekleme yapma!")
# f.close()

# f = open("c:\\Users\\yasin\\Desktop\\Python\\OrtaSeviye\\demofile2.txt", "r")
# print(f.read())

# f = open("c:\\Users\\yasin\\Desktop\\Python\\OrtaSeviye\\demofile3.txt", "w")
# f.write("İçindekileri silerek yazma!")
# f.close()
# # ekleme sonrası dosya içeriğine bak:
# f = open("c:\\Users\\yasin\\Desktop\\Python\\OrtaSeviye\\demofile3.txt", "r")
# print(f.read()) 

# dosyalar=["c:\\Users\\yasin\\Desktop\\Python\\OrtaSeviye\\demofile2.txt","c:\\Users\\yasin\\Desktop\\Python\\OrtaSeviye\\demofile3.txt"]
# for a in dosyalar:
#     f= open (a,"r")
#     print(f.read()) das
#! try:
# try:
#     dosya = open("c:\\Users\\yasin\\Desktop\\Python\\OrtaSeviye\\rehber.txt","r")
#     print("   Rehber Kayıt Listesi ")        
#     print("═════════════════════════════")
#     a = 1        
#     for kayit in dosya.readlines():
#         print(a, kayit)
#         a += 1
# except:
#     print("Dosya bulunamadı.")
#     print("Devam etmek için Enter'a basın.")
#     input()

# d=open("c:\\Users\\yasin\\Desktop\\Python\\OrtaSeviye\\rehber.txt")
# okunan=d.readline()#sadece bir satır
# print(okunan)
# okunan=d.readline()#sadece bir satır
# print(okunan)
# okunan=d.readlines()#sadece bir satır
# print(okunan)
import os 
print(*os.listdir(),sep="\n")
dosyaListesi=os.listdir()
for a in dosyaListesi:
    # print(a)
    if a.endswith(".py"):
        print(a)
# mevcut konumdaki dosya/dizinlerin dizi olarak listesi.