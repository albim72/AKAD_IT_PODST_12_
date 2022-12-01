print("pierwsza linia programu....")
a = 67
print(a)
print(type(a))

a = "czerwony"
print(a)
print(type(a))

liczba:float
liczba = 8.89
print(liczba)
print(type(liczba))

liczba = True
print(liczba)
print(type(liczba))

pora = "pora roku: "
pora1 = "jesień"
pora2 = "zima"
rok = 2022

#komentarz -> łączenie ciąg string (tekstu) -> operator +
print(pora+pora1+", "+pora+pora2+", rok: "+ str(rok))

"""
komentarz dokumentacyjny, wieloliniowy
tylko pierwszy komentarz w pliku pythona jest dokumentacyjny
linia3
linia4
.....

"""
'''
ten komentarz nie jest dokumentacyjny
'''

#wyświetlanie tekstu za poocą kolekcji
print(pora,pora1,",",pora,pora2,"rok:",rok,sep=" -- ")

abc= 56,89
print(abc)

y = 77.895
print(y)
print(8*y)

x = "8.15"
print(12*x)
print(12*float(x))
#CTRL+D -> powielenie linii/bloku
print(12*eval(x))

g1 = 10
g2 = 11

print(g1+g2,g1-g2,g1*g2,g1/g2,g1%g2,g1**g2,sep="  --  ")
print(round(6.77))
print(round(6.77,1))
print(pow(7,4))

import math

print(math.sqrt(17))

i = 4
i+=1 # i = i+1
print(i)



