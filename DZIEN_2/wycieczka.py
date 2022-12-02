#funkcja kwota(transport,nocleg_wyzyw,wycieczki,ubezp,inne,rabat) -> wypisz wynik
#rabatuj tylko transport i nocleg_wyzyw
def kwota(t,nw,w,u,i,rab=0):
    return (nw+t)*(1-rab/100)+w+u+i

print(kwota(100,100,50,50,50),"zł")
print(kwota(100,100,50,50,50,25),"zł")
