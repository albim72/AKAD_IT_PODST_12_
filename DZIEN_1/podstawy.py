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


