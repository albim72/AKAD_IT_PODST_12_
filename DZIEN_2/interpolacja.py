marka = "Jeep"
model = "Cherokee"
rocznik = 2020


opis_auta = "samochód -> marka: {}, model: {}, rocznik: {}."
print(opis_auta.format(marka,model,rocznik))

opis_auta = "samochód -> rocznik: {2}, marka: {0}, model: {1}."
print(opis_auta.format(marka,model,rocznik))

#f-string
fopis = f"autokomis ABC -> samochód marka {marka},model {model}, rok produkcji: {rocznik}."
print(fopis)

nazwa = "wpółczynnik"
wartosc = 1.5674356

ft = '%-30s = %.2f' %(nazwa,wartosc)
print(ft)

owoce = [
    ('awokado',8.77),
    ('jabłko',2.99),
    ('winogrono',12.56),
    ('mandarynka',8.90),
    ('malina',16),
    ('banan',4.99)
]


enumeracja = list(enumerate(owoce))
print(enumeracja)
print("__________warzywniak JÓZEK - cennik owoców______________________")
for i,(owoc,cena) in enumerate(owoce):
    print('#%d: %-10s = %.2f zł' %(i,owoc,cena))

print("______warzywniak JÓZEK - cennik owoców - wersja rozszerzona_________")
for i,(owoc,cena) in enumerate(owoce):
    print('#%d: %-10s = %6.2f zł' %(
        i+1,
        owoc.title(),
        round(cena,1)
    ))
