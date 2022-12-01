samochod = {
    "marka":"Ford",
    "model":"Mustang",
    "rocznik":1975,
    "poj":3.6
}

print(samochod)
print(type(samochod))

print(samochod["marka"])
samochod["poj"] = 3.8
print(samochod)

samochod["przebieg"] = 367800
print(samochod)

print(samochod.items())
print(samochod.keys())
print(samochod.values())

print("_________________ klucze _______________________")
for x in samochod:
    print(x)

print("_________________ wartości v1 _______________________")
for y in samochod.values():
    print(y)

print("_________________ wartości v2 _______________________")

for y in samochod:
    print(samochod[y])


print("_________________ items _______________________")

for x,y in samochod.items():
    print(x,":",y)
