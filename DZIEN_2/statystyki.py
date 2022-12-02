liczby = [56,78,244,0,-777,1099,23,567,899,2,3,4,1,5,19,4,-55]

def statystyki(dane):
    minimum = min(dane)
    maksimum = max(dane)
    rozstep = maksimum-minimum
    n = len(dane)
    return minimum,maksimum,rozstep,n

wynik = statystyki(liczby)
print(wynik)
print(type(wynik))

mini,maxi,roz,n = statystyki(liczby)
print(f"wartość maksymalna: {maxi}, wartość minimalna: {mini}, liczba elementów: {n}, "
      f"rozstęp danych: {roz}")
