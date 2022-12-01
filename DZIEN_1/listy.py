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
