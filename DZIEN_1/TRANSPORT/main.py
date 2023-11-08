from pojazd import Pojazd

p = Pojazd("Bus Mercedes Sprinter","pojazd kołowy",5,356,45,13)
print(p)
print(p.danest())
print(f'koszty przejazdu: {p.kosztyprzejazdu(15)} zł')
