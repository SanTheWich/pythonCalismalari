name="Yasin Talha"
surname="karabudak"
array = ["number1","number2","number3"]
print(name[-3:])
print(name[-3])
print(len(name[-3:]))
print(name[2:6])
print(name[::-1])
#### !!!!
print(name,end="+")
print(surname)
print(*"PYTHON")#" * HER KARAKTERİN ARASINA BOŞLUK BIRAKIR" 
print(*array,sep="\n")#listenin her elemanın arasına ne koyacağını "sep" ile belirliyoruz
print("Adı: ",name,"\n Soyadı: ",surname)
print(f"Adı: {name}, Soyadı: {surname}" )
