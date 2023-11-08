from stransportu import STransportu

class Pojazd(STransportu):
    
    def __init__(self, nazwa, rodzaj, nrtrasy, czas_przejazdu, koszt_paliwa, inne_koszty):
        super().__init__(nazwa, rodzaj)
        self.nrtrasy = nrtrasy
        self.czas_przejazdu = czas_przejazdu
        self.koszt_paliwa = koszt_paliwa
        self.inne_koszty = inne_koszty
 
    def danest(self):
        return f'Pojazd -> {self.rodzaj}, nazwa pojazdu: {self.nazwa}.'

    def kosztyprzejazdu(self, koszty_stale):
        return super().kosztyprzejazdu() + self.koszt_paliwa + self.inne_koszty
