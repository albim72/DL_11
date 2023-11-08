from pojazd import Pojazd

p = Pojazd("Bus Mercedes Sprinter","pojazd kołowy",5,356,45,13)
print(p)
print(p.danest())
print(f'koszty przejazdu: {p.kosztyprzejazdu(15)} zł')
print("działanie na zmiennych konstrukcyjnych")
p._inne_koszty = 17
print(f'nowe koszty inne: {p._inne_koszty} zł')
print(f'koszty przejazdu po zmianie: {p.kosztyprzejazdu(15)} zł')
print("działanie na properties")
p.inne_koszty = 21
print(f'nowe koszty inne: {p.inne_koszty} zł')
print(f'koszty przejazdu po zmianie: {p.kosztyprzejazdu(15)} zł')
