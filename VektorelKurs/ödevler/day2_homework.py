### 1-
name=str(input("Please write your name: "))
print(f"Hello {name}")
### 2-square 
a=int(input("Please enter a side size of your square: "))
print ("Your square size is equal {}".format(a*4))
### 3- square area
a=int(input("\nPlease enter your square length size: "))
print ("Your square size is equal {}".format(a*a))
### 4- sum 
num1=int(input("\nPlease enter your number 1:  "))
num2=int(input("\nPlease enter your second number: "))
print ("{} + {} equal {}".format(num1,num2,num1+num2))
## 5- all of calc. 
a=int(input("\nPlease enter your first number:  "))
b=int(input("\nPlease enter your second number: "))
print("{} + {} = {}".format(a,b,a+b))
print("{} - {} = {}".format(a,b,a-b))
print("{} / {} = {}".format(a,b,a/b))
print("{} * {} = {}".format(a,b,a*b))
## 6-age
a=int(input("\nPlease enter your birth year:"))
print("Your age is {} ".format(2024-a))
## 7-Türkçe’den 1., 2. yazılı ve performans notunu sorup, ortalamalarını hesaplayarak kullanıcıya veren bir program yap.

## 8-Boyunuza göre ideal kilonuzu hesaplayan program yapınız.

## 9-Üçgenin alan ve çevre hesabını yapan bir program yap.

## 10-Dairenin alanını (π r²) ve çevresini (2 π r) hesaplayan bir program yap.
a=int(input("\nPlease enter your circle radius: "))
print("Your circle area is {} and perimeter is {} ".format(a*a*3.14,2*3.14*a))