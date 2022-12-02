liczby = [56,78,244,0,-777,1099,23,567,899,2,3,4,1,5,19,4,-55]

def statystyki(dane):
    minimum = min(dane)
    maksimum = max(dane)
    rozstep = maksimum-minimum
    n = len(dane)
    suma = sum(dane)
    avg = suma/n
    return minimum,maksimum,rozstep,n,suma,avg

wynik = statystyki(liczby)
print(wynik)
print(type(wynik))

mini,maxi,roz,n,s,a = statystyki(liczby)
print(f"wartość maksymalna: {maxi}, wartość minimalna: {mini}, liczba elementów: {n}, "
      f"rozstęp danych: {roz}, suma elementów: {s}, średnia arytmetyczna: {a:.2f}")
