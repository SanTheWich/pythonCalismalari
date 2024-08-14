import turtle
# # print(dir(turtle))#hangi fonksiyonları kullanabileceğini listeler
# # help(turtle.pen)
# renkler=["cyan","red","yellow","olive","blue","green"]
# turtle.speed(10)
# for x in range (20,26):
#     turtle.color(renkler[x%6])
#     turtle.forward(60)
#     turtle.right(144)
# input()
import random
# print(random.randint(1,100))
# print(random.random())
# yaziTura = ["Tura","Yazı"]
# print(random.choice(yaziTura)) 
# renk=["cyan","blue","green","black"]
# for b in range(10):
#     turtle.up()#kalemi kaldır
#     turtle.goto(random.randint(-200,200),random.randint(-200,200))#turtlerın konumu değiştirmek için yapılır.
#     turtle.down()
#     buyukluk=random.randint(10,100)
#     turtle.color(renk[random.randint(0,3)])
#     for a in range (4):
#         turtle.forward(buyukluk)
#         turtle.right(90)
# input()
# not1=35
# print(type("sehir"))
# print(type(not1))
# #atamalar
# a=b=1
# ad,soyad,yas ="Yasin","Karabudak",21
# #veriler
# a=1#global variable
# def aDeger():
#     a=2#local variable
#     print(f"{a}")
# print (f"global variable {a}") 
# !!!!!!  
# def aDeger2():
#     global a
#     a=2#global a yazdık artık global a da 2 oldu
#     print(f"{a}")
# yaziTura = ["Tura","Yazı"]
# print(random.choice(yaziTura)) 
# aDeger2()
sayi=(random.randint(1,10))
hak=3
puan=100
for a in range (3):
    tahmin=int(input("Tahminin: "))
    if sayi==tahmin:
        print(f"Doğru bildiniz \n Puanınız {puan}")
        break
    elif hak>1:
        hak=hak-1
        puan=puan-10
        print(f"Bilemediniz {hak} hakkiniz kaldi")
    else:
        print("Hakkin kalmadi kaybettin.")