from abc import ABC, abstractmethod


class Pojazd(ABC):
    def __init__(self, model: str, rok: int):
        self._model = model
        self._rok = rok
        self._predkosc = 0
        if not FabrykaPojazdow.sprawdz_rok(rok=rok):
            raise ValueError("Nieprawidłowy rok produkcji!")   


    @property
    def predkosc(self) -> float:
        return self._predkosc

    @predkosc.setter
    def predkosc(self, predkosc: float):
        if predkosc < 0:
            raise ValueError("Prędkość nie może być ujemna!")  
        self._predkosc = predkosc
    
    @predkosc.deleter
    def predkosc(self):
        self._predkosc = 0


    # Dokoncz definicje, rowniez setter i deleter
    # @property
    # def predkosc(self) -> float:


class Samochod(Pojazd):
    liczba_drzwi: int
    def __init__(self, model: str, rok: int, liczba_drzwi: int, ):
        super().__init__(model=model, rok=rok)
        self.liczba_drzwi=liczba_drzwi
# w __init__ dodaj skladowa liczba_drzwi

class Autobus(Pojazd):
    liczba_miejsc: int
    def __init__(self, model: str, rok: int, liczba_miejsc: int, ):
        super().__init__(model=model, rok=rok)
        self.liczba_miejsc = liczba_miejsc
        print("dupsko")
# w __init__ dodaj skladowa liczba_miejsc


class FabrykaPojazdow(ABC):

    _liczba_wyprodukowanych: int 
    _nazwa: str
    def __init__(self, nazwa: str):
        self._nazwa = nazwa
        self._liczba_wyprodukowanych = 0
    

    @property
    def nazwa(self):
        return self._nazwa
    
    def _zwieksz_licznik(self):
       self._liczba_wyprodukowanych += 1
    

    def ile_wyprodukowano(self) -> int:
        return self._liczba_wyprodukowanych

    @abstractmethod
    def stworz_pojazd() -> Pojazd:
        print("swtorzono pojazd")

    @classmethod
    def utworz_fabryke(cls, typ_fabryki: str, nazwa: str) -> 'FabrykaPojazdow':
        if typ_fabryki == "samochod":
            print("stworzono auto")
            return FabrykaSamochodow(nazwa=nazwa)
        
        elif typ_fabryki == "autobus":
            return FabrykaAutobusow(nazwa=nazwa)
        
        print("stworzono fabryke pojazdow")

    @staticmethod
    def sprawdz_rok(rok: int) -> bool:
        return (rok >=1900 and rok <= 2024)
    




# do uzupelnienia rozne metody jak na diagramie i w opisie

class FabrykaSamochodow(FabrykaPojazdow):

    def __init__(self, nazwa: str):
        super().__init__(nazwa=nazwa)  

    def stworz_pojazd(self, model: str, rok: int, liczba_drzwi: int = 4) -> Samochod:
        pojazd = Samochod(model=model, rok=rok, liczba_drzwi=liczba_drzwi)
        self._zwieksz_licznik()
        return pojazd

class FabrykaAutobusow(FabrykaPojazdow):

    def __init__(self, nazwa: str):
        super().__init__(nazwa=nazwa)

    def stworz_pojazd(self, model: str, rok: int, liczba_miejsc: int = 50) -> Autobus:
        pojazd = Autobus(model=model, rok=rok, liczba_miejsc=liczba_miejsc)
        self._zwieksz_licznik()
        return pojazd
    


def main():
    # Utworz fabryki pojazdow (samochodow i autobusow)
    fabryka_samochodow = FabrykaPojazdow.utworz_fabryke("samochod", "Fabryka Samochodów Warszawa")
    fabryka_autobusow = FabrykaPojazdow.utworz_fabryke('autobus', "Fabryka Autobusów Kraków")
    

    # Utworzone fabryki - demonstracja @property nazwa
    print(f"Nazwa fabryki: {fabryka_samochodow.nazwa}")  
    print(f"Nazwa fabryki: {fabryka_autobusow.nazwa}")  

    # Utworz pojazdy
    samochod = fabryka_samochodow.stworz_pojazd("Fiat", 2023, liczba_drzwi=5)
    autobus = fabryka_autobusow.stworz_pojazd("Solaris", 2023, liczba_miejsc=60)

    # Demonstracja dzialania gettera, settera i deletera
    samochod.predkosc = 50  # uzycie setter
    print(f"Prędkość samochodu: {samochod.predkosc}")  # uzycie getter
    del samochod.predkosc  # uzycie deleter
    print(f"Prędkość po reset: {samochod.predkosc}")

    # Pokazanie ile pojazdow wyprodukowano
    print(f"Wyprodukowano samochodów: {fabryka_samochodow.ile_wyprodukowano()}")
    print(f"Wyprodukowano autobusów: {fabryka_autobusow.ile_wyprodukowano()}")

if __name__ == "__main__":
    main()