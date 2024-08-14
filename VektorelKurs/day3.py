not1=int(input("Ilk sınav notunuz kaçtır"))
not2=int(input("ikinci sınav notunuz kaçtır"))
ortalama=(not1+not2)/2
if ortalama<0 or ortalama>100:
    print("Yanlış veri girdiniz")
else:
    if ortalama<85:
        print("tebrikler burs kazandınız")
    elif 85>ortalama>=70:
        print("en azından kalmadınız")
    elif 50<ortalama<70:
        print("balon patladı")