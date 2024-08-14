#
num1=int(input("Please enter a number: "))
if num1<100:
    print("your number smaller than 100")
#örnek 3
grade=int(input("Please enter your grade: "))
if grade<50:
    print("you need to take again lesson")

password=str(input("Please enter password"))
if password=="9874":
    print("You entered the system succesful")
else:
    print("Wrong password Try Again!!")
#Klavyeden bir yıl girmesini isteyin. Bu yıla göre geçmiş mi? 
#Henüz gelmemiş mi yoksa içinde bulunduğun yıl mı olduğunu 
#tespit edip kullanıcıya söylesin.
year=int(input("Please enter year"))
if year==2024:
    print("You are in the correct time")
elif year<2024:
    print("You are in the past time")
elif year>2024:
    print("You are in the future ")