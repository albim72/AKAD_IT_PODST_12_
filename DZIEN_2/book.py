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
