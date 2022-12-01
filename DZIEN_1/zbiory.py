drzewa = {"buk","dąb","jesion","sosna","dąb","baobab","jabłoń","dąb","dąb"}
print(drzewa)
print(drzewa)
print(drzewa)

for d in drzewa:
    print(d)


print("jesion" in drzewa)
print("osika" in drzewa)

drzewa.add("osika")
print(drzewa)

las = ["jodła","grab","świerk","brzoza"]
drzewa.update(las)
print(drzewa)

drzewa.remove("osika")
print(drzewa)

drzewa.discard("jojoba")
print(drzewa)

drzewa.discard("dąb")
print(drzewa)

drzewa.add("brzoza")
print(drzewa)

nb = [3,4,5,2,3,4,5,3,4,52,3,4,5,6,2,3,4,5,2,3,4,5]
nb = list(set(nb))
print(nb)
