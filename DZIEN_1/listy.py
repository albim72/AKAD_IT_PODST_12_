kraje = ["Polska","Kanada","Turcja","Hiszpania","Laos","Japonia"]
print(kraje)
print(type(kraje))
print(kraje[3])
print(kraje[2:5])
kraje.append("Urugwaj")
print(kraje)
kraje.insert(2,"Egipt")
print(kraje)

kraje.sort()
print(kraje)
kraje.reverse()
print(kraje)
kraje.sort(reverse=True)
print(kraje)

liczby = [2,56,78,90,-32,0,1112,0,12,9,-3,134,67,-8,0,12,12]

liczby.sort(reverse=True)
print(liczby)

print(liczby[1:6])
liczby.remove(1112)
print(liczby)

del liczby[2]
print(liczby)

print(liczby.count(0))

inc = liczby.index(-3)
del liczby[inc]
print(liczby)

rasa = ["buldog angelski","rotwalier","labrador"]
rasa_cena = [7500,6500,4500]
sklepzoo = [[rasa,"kot","papuga","złota rybka","mysz"],[rasa_cena,2000,8000,40,45]]
print(sklepzoo[0])
print(sklepzoo[0][0])
print(sklepzoo[0][0][0],"-",sklepzoo[1][0][0],"zł")
print(sklepzoo[0][1],"-",sklepzoo[1][1],"zł")

rasa_owczarki = ["owczarek szkocki","owczarek niemiecki","owczarek podhalański"]
rasa = rasa + rasa_owczarki
print(rasa)

litery = ['a','b','c','d','e','f','g','h']
print("przed zmianą:",litery)
litery[2:7] = [99,12,33]
print("po zmianie:",litery)

litery_m = litery
print(type(litery_m))

litery_p = list(litery) #stworzenie nowej listy
litery_q = litery[:]#stworzenie nowej listy

print("przed zmianą:",litery)
print("przed zmianą:",litery_m)
print("przed zmianą:",litery_p)
print("przed zmianą:",litery_q)

litery[:] = ['abc','xyz',1001,1002,1134,2002]

print("po zmianie:",litery)
print("po zmianie:",litery_m)
print("po zmianie:",litery_p)
print("po zmianie:",litery_q)

marki = ["audi","toyota","opel","peugeot","kia","bmw","landrover"]
parz = marki[::2]
nieparz = marki[1::2]

takietam = marki[1:5:2] #[od:do:krok]

print(takietam)

print(parz)
print(nieparz)

imie= "Hieronim" #odwróć listy w szyku

print(imie,"-",imie[::-1])

