from stransportu import STransportu

class Pojazd(STransportu):

    def __init__(self, nazwa, rodzaj, nrtrasy, czas_przejazdu, koszt_paliwa, inne_koszty):
        super().__init__(nazwa, rodzaj)
        self.nrtrasy = nrtrasy
        self.czas_przejazdu = czas_przejazdu
        self.koszt_paliwa = koszt_paliwa
        self._inne_koszty = inne_koszty

    def __repr__(self):
        return (f'nowy obiekt klasy {self.__class__.__name__}: środek transportu -> {self.nazwa}'
                f', numer trasy: {self.nrtrasy} , czas przejazdu: {self.czas_przejazdu} min')

    #funkcja getter
    @property
    def inne_koszty(self):
        return self._inne_koszty

    #funkcja setter
    @inne_koszty.setter
    def inne_koszty(self,nowekoszty):
        self._inne_koszty = nowekoszty

    def danest(self):
        return f'Pojazd -> {self.rodzaj}, nazwa pojazdu: {self.nazwa}.'

    def kosztyprzejazdu(self, koszty_stale):
        return super().kosztyprzejazdu(koszty_stale) + self.koszt_paliwa + self.inne_koszty
