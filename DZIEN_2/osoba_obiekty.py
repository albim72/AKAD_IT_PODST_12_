class Osoba:
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczu = "brązowe"
        self.pracownik = False
        self.info()

    def info(self):
        print("utworzono nową osobę...")

    def print_osoba(self):
        print(f"Osoba -> imię: {self.imie}, wiek: {self.wiek}, waga: {self.waga} kg, "
              f"wzrost: {self.wzrost} cm, kolor oczu: {self.kolor_oczu}")

    def wiekza_x_lat(self,x):
        return self.wiek + x

    def czypracownik(self):
        return self.pracownik


za = 7
print("____________osoba 1_____________")
os1 = Osoba("Jan",56,99,176)
os1.kolor_oczu = "niebieskie"
os1.print_osoba()
print(f"wiek osoby za {za} lat: {os1.wiekza_x_lat(za)} ")
print(f"czy osoba jest pracownikiem? ({os1.czypracownik()})")


print("____________osoba 2_____________")
os2 = Osoba("Olga",29,53,166)
os2.print_osoba()
print(f"wiek osoby za {za} lat: {os2.wiekza_x_lat(za)} ")
print(f"czy osoba jest pracownikiem? ({os2.czypracownik()})")
