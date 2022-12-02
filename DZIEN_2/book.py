class Book:
    #deklaracja stanu -> konstruktor klasy
    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    #zachowanie -> metody -> funkcje klasy
    def create_book(self):
        print("tworzenie nowej książki")

    def print_book(self):
        print(f"książka {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, "
              f"oprawa: {self.oprawa}.")

    def rabat(self):
        return 0.1*self.cena

    def setcena(self,nowacena):
        self.cena = nowacena


print("________książka nr 1__________")
b1 = Book(456,"Wiedźmin","Andrzej Sapkowski",39)
b1.oprawa = "twarda"
b1.setcena(45)
b1.print_book()
print(f"cena po rabacie {b1.cena - b1.rabat()} zł")

print("________książka nr 2__________")
b2 = Book(566,"Hobbit","J.R.R. Tolkien",36)
b2.print_book()
print(f"cena po rabacie {b2.cena - b2.rabat()} zł")
