miasta = ("Kraków","Tarnów","Lublin","Gdańsk","Słupsk","Poznań","Kraków","Kraków")

print(miasta.count("Kraków"))

print(miasta[3])
print(miasta[:4])

if "Gdańsk" in miasta:
    print("Witamy w Gdańsku")

if "grabki" in miasta:
    print("to jest błąd!")

print(len(miasta))

stolica = ("Warszawa",)
print(type(stolica))

miasta = miasta + stolica
print(miasta)

mojakrotka = tuple(("CosTam344",344,True,"Kraków",0.99))
print(mojakrotka)

mojalista = list(mojakrotka)
print(mojalista)

mojalista.remove(344)
u = mojalista.index("Kraków")
mojalista[u] = "Toruń"

mojalista.append(100)

mojakrotka = tuple(mojalista)

print(mojakrotka)
