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


class Pracownik(Osoba):
    #konstruktor z dziedziczeniem
    def __init__(self,imie,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie):
        super().__init__(imie,wiek,waga,wzrost)
        self.firma = firma
        self.stanowisko = stanowisko
        self.latapracy = latapracy
        self.wynagrodzenie = wynagrodzenie
        self.pracownik = True

    def print_pracownik(self):
        print(f"dane pracownika -> firma: {self.firma}, stanowisko pracy: {self.stanowisko}, "
              f"lata pracy: {self.latapracy}, wynagrodzenie: {self.wynagrodzenie} zł.")


print("____________pracownik 1_____________")
pr1 = Pracownik("Karol",55,101,174,"ABC","dyrektor",12,11900)
pr1.print_osoba()
pr1.print_pracownik()
print(f"wiek osoby za {za} lat: {pr1.wiekza_x_lat(za)} ")
print(f"czy osoba jest pracownikiem? ({pr1.czypracownik()})")

class Sport:
    def __init__(self,dyscyplina,lataupr,zyciowka):
        self.dyscyplina = dyscyplina
        self.lataupr = lataupr
        self.zyciowka = zyciowka

    def info_sport(self):
        print(f"{self.dyscyplina}, lata uprawiania: {self.lataupr}, życiówka: {self.zyciowka}.")


class Ekstra:
    pass


class Student(Pracownik,Sport,Ekstra):
    def __init__(self,imie,wiek,waga,wzrost,nr_studenta,wydzial,kierunek,rokstud,
                 firma="",stanowisko="",latapracy="",wynagrodzenie="",dyscyplina="",lataupr="",zyciowka=""):
        Pracownik.__init__(self,imie,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie)
        Sport.__init__(self,dyscyplina,lataupr,zyciowka)
        self.nr_studenta = nr_studenta
        self.wydzial = wydzial
        self.kierunek = kierunek
        self.rokstud = rokstud

    def print_student(self):
        print(f"Student {self.nr_studenta}, wydział: {self.wydzial}, kierunek: {self.kierunek}, "
              f"rok studiów: {self.rokstud}.")

    def czypracownik(self):
        return self.firma != ""


print("____________student 1_____________")
st1 = Student("Olaf",22,80,176,456556,"budowlany","budowa mostów",3)
st1.print_osoba()
st1.print_student()
print(f"wiek osoby za {za} lat: {st1.wiekza_x_lat(za)} ")
print(f"czy osoba jest pracownikiem? ({st1.czypracownik()})")

print("____________student 2_____________")
st2 = Student("Karolina",23,60,178,976766,"ekonomii","ekonomika",4,"XYZ","sekretarka",1,2700)
st2.print_osoba()
st2.print_student()
st2.print_pracownik()
print(f"wiek osoby za {za} lat: {st2.wiekza_x_lat(za)} ")
print(f"czy osoba jest pracownikiem? ({st2.czypracownik()})")

#utwórz trzecią instancję klasy Student - st3, który to student nie będzie pracownikiem, ale będzie sportowcem

print("____________student 3_____________")
st3 = Student("Paweł",22,77,177,4545545,"Automatyka i Informatyka","informatyka",3,dyscyplina="biegi ultra",lataupr=4,
              zyciowka="50km 7h 34min 4s")
st3.print_osoba()
st3.print_student()
st3.info_sport()
print(f"wiek osoby za {za} lat: {st3.wiekza_x_lat(za)} ")
print(f"czy osoba jest pracownikiem? ({st3.czypracownik()})")


