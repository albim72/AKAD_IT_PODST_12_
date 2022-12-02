#przykład nr 1
def witaj():
    print("witaj użytkowniku")
    print("opłać abonament")
    print("zaloguj się")

witaj()
witaj()

# for _ in range(21):
#     witaj()

#przykład nr 2
def obywatel(nrtelefonu,kraj="Polska"):
    print("pochodzę z kraju:",kraj,", numer telefonu: ",nrtelefonu)

obywatel(345435343,"Turcja")
obywatel(345434665,"Armenia")
obywatel(556456456546,"Włochy")
obywatel(54546546456,"Hiszpania")
obywatel(78678578768)
#przykład nr 3
f= 9

def oblicz(a,b,x):
    f = (a+b)*x
    print("za chwilę będzie return")
    return f
    print("po returnie")

print(oblicz(6,12,36))
print(f)

#przykład nr 4

def miasta(miasto3, miasto2="Katowice", miasto1="Kraków"):
    print("miasto tygodnia:",miasto1,", drugie miejsce:", miasto2, ",trzecie miejsce:",miasto3)


miasta("Toruń","Poznań","Białystok")
miasta("Toruń","Poznań")
miasta("Toruń")
miasta("Rzeszów",None,"Lublin")
miasta("Rzeszów",miasto1="Lublin")

#przykład nr 5

def zamki(nr_tygodnia,*zamki,kupon):
    print("zamek tygodnia:", zamki[0]," - kupon do biletu:",kupon,"zł, drugie miejsce:", zamki[1], ",trzecie miejsce:", zamki[2])

zamki(12,"Malbork","Ogrodzieniec","Warszawa","Czersk",kupon=20)
zamki(13,"Janowiec","Malbork","Ogrodzieniec","Będzin","Warszawa","Czersk",kupon=6)


#przykład nr 6
ef=100
def fx(x):
    global ef
    ef = ef*x**2
    return ef

print(fx(9))
print(ef)
