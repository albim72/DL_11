#przykład 1

def obliczenie(x,y,z):
    dane = (x,y,z)
    print(dane)

obliczenie(4,7,8)


n=100
def fx(a,b,c=1.1):
    global n
    n = a/(b+c) * n
    return n

print(fx(3.6,7,8.8))
print(n)

print(fx(5,7))


#przykład 2 - funkcja ZIP

numerki = [1,2,3,4]
polskie = ['jedynka','dwójka','trójka','czwórka','piątka']
english = ('one','two','three','four')

wynik = zip(numerki,polskie,english)
print(wynik)

wynik_lista = list(wynik)
print(wynik_lista)

# wynik_set = set(wynik)
# print(wynik_set)



#przykład 3 - enumerate

sklep = ['chleb','masło','mleko','ser','jogurt']

for i,item in enumerate(sklep):
    print(f'{i+1}: {item}')

print("__________________________________")

for i,item in enumerate(sklep,100):
    print(f'{i+1}: {item}')

#funkcja wyższego rzędu
def mapowanie(dane,transformacja):
    mapa = []
    for element in dane:
        mapa.append(transformacja(element))
    return mapa


def mnozenie(wart):
    return wart*3

print(mapowanie([1,5,8,19,25,67,99],mnozenie))
