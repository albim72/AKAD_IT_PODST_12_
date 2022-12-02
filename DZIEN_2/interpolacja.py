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
