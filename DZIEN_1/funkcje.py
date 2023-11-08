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



