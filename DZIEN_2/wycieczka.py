#funkcja kwota(transport,nocleg_wyzyw,wycieczki,ubezp,inne,rabat) -> wypisz wynik
#rabatuj tylko transport i nocleg_wyzyw
def kwota(t,nw,w,u,i,rab=0):
    return (nw+t)*(1-rab/100)+w+u+i

print(kwota(100,100,50,50,50),"zł")
print(kwota(100,100,50,50,50,25),"zł")

#dla rabatu 0 wypisz -> kwota bazowa wynosi: kwota
#dla rabatów pozostałych -> dla rabatu x% kwota do zapłaty wynosi: kwota

rabs = [0,8,10,12,15,20,25]

#dodatkowo: zapisz kwoty które policzyliśmy dla każdego rabatu do listy wynik =[]
