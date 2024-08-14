#operaorler 2**3 2 üzeri üç
#'and' 'or' 'not'
# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3
# camelCase
# 	adiSoyadi
# 	ogrenciNo

# snake_case
# 	adi_soyadi
# 	ogrenci_no

# kebap-case
# 	adi-soyadi

# ogrenci-no

# PascalCase
# 	AdiSoyadi
# 	OgrenciNo

# y=int(input("sayi test"))
# if 3<20 and y<10:
#     print("True")

#fonksiyon tanımlama
def selam():
    print("merhaba")
    print("nasılsın")
def topla(x,y):
    #print(x+y)
    return(x+y)

a=int(input("sayi1: "))
b=int(input("sayi2: "))
print(topla(a,b))
##
def selamla(isim):
    return "Merhaba " + isim
print(selamla(input("Adın ne? ")))
##
def selam(isim="isim yok"):
    return "Merhaba "+ isim
ad="Yasin"
print(selam(ad))
