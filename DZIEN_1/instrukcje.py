a=112
b=10
print("_________________if-elif______________________")
if a>b and b>=10000:
    print("a i b to duże liczby")
elif (a==1 and b==1):
    print("a=1 i b=1")
elif a==b:
    print("a jest równe b")
elif a>b:
    print("a jest większe od b")
else:
    print("a jest mniejsze od b")

print("_________________match case /od wersji 3.10______________________")
nr_dnia = int(input("podaj numer dnia tygodnia (1-7): "))

match nr_dnia:
    case 1:
        print("Poniedziałek")
    case 2:
        print("Wtorek")
    case 3:
        print("Środa")
    case 4:
        print("Czwartek")
    case 5:
        print("Piątek")
    case 6:
        print("Sobota")
    case 7:
        print("Niedziela")
    case _:
        print("Nie ma takiego dnia")

print("________wyjście________")
quit_flag = True
match quit_flag:
    case True:
        print("Wyjście...")
        exit()
    case False:
        print("system pracuje")

