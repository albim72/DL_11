from abc import ABC, abstractmethod


class STransportu(ABC):
    def __init__(self, nazwa, rodzaj):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.info()

    def info(self):
        print("utworzenie nowego środka transportu....")

    @abstractmethod
    def danest(self):
        pass

    @abstractmethod
    def kosztyprzejazdu(self, koszty_stale):
        return koszty_stale
