a = 10
b = 20

# örnek-1
print("a küçük" if a < b else "b küçük")

import day5_2 #o dosyadaki fonksiyonu buraya getirdi
print(day5_2.ikiKati(5))
from day5_2 import ikiKati# direkt fonksiyonu aktarmayı sağlar
##FOR LOOP
for a in range(5):
    print(f"{a}")
# For ile sayı saydırma (range)
# Ör-1 Say
for x in range(6): print(x,"vektorel")

# Ör-2 Belirli aralık say
for x in range(5, 10): print(x)

# Ör-3 Atlayarak say
for x in range(5, 30, 2): print(x)

# Ör-4 x adet bir şey yaz
for _ in range(5): print("Erdinç")
for x in range(1, 10): print('Erdinç')

# Ör-5 Geri saydır
for x in range(100, 10, -5): print(x)
for x in 'Erdinç': print(x) # doğru kullanımı

for a in range(1,11):
    if a==2: continue
    for b in range(1,11):
        print(a,"x",b,"=",a*b)
print("\n")
#if a == 7: break !! a döngüsünü kırıyor