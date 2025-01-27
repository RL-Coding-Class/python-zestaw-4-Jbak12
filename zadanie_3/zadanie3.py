from functools import singledispatch, singledispatchmethod

# Singledispatch: globalna funkcja do logowania zdarzeń
@singledispatch
def log_event(event):
    raise NotImplementedError(f"Brak implementacji dla typu: {type(event)}")

# Napisz obsluge zdarzen str
@log_event.register(str)
def log_event_str(event: str):
    print("obsluga string")

#Napisz obsluge zdarzen int
@log_event.register(int)
def log_event_int(event: int):
    print("obsluga int")

# Napisz obsluge zdarzen typu dict
@log_event.register(dict)
def log_event_dict(event: dict):
    print("obsluga slownik")

# Klasa z metodą używającą singledispatchmethod
class EventHandler:
    def __init__(self):
        self.event_count = 0 

    @singledispatchmethod
    def handle_event(self, event):
        raise NotImplementedError(f"Nieobsługiwany typ zdarzenia: {type(event)}")
    
    # Napisz obsluge zdarzen str, pamietaj: self.event_count += 1
    @handle_event.register(str)
    def handle_event_str(self, event: str):
        self.event_count += 1
        print("obsluga string z klasy")

    # Napisz obsluge zdarzen int
    @handle_event.register(int)
    def handle_event_int(self, event: int):
        self.event_count += 1
        print("obsluga int z klasy")

    # Napisz obsluge zdarzen list
    @handle_event.register(list)
    def handle_event_list(self, event: list):
        self.event_count += 1
        print("obsluga list z klasy")
        
# Klasa pochodna z nowymi rejestracjami typów
class DerivedHandler(EventHandler):
    @singledispatchmethod
    def handle_event(self, event):
        super().handle_event(event)


    @handle_event.register(int)
    def handle_event_float(self, event: int):
        self.event_count += 1
        print("obsluga float z klasy pochodnej")

    @handle_event.register(float)
    def handle_event_float(self, event: float):
        self.event_count += 1
        print("obsluga float z klasy pochodnej")


# Demonstracja użycia
if __name__ == "__main__":
    # Globalna funkcja logowania zdarzeń
    print("=== Globalne logowanie zdarzeń ===")
    log_event("Uruchomienie systemu")
    log_event(404)
    log_event({"typ": "error", "opis": "Nieznany błąd"})

    # Klasa obsługująca zdarzenia
    print("\n=== Klasa EventHandler ===")
    handler = EventHandler()
    handler.handle_event("Zdarzenie logowania")
    handler.handle_event(123)
    handler.handle_event(["zdarzenie1", "zdarzenie2", "zdarzenie3"])

    # Obsługa nieobsługiwanego typu
    print("\n=== Obsługa nieobsługiwanego typu ===")
    try:
        log_event(3.14)  # Nieobsługiwany typ w log_event
    except NotImplementedError as e:
        print(e)

    try:
        handler.handle_event(set([1, 2, 3]))  # Nieobsługiwany typ w handle_event
    except NotImplementedError as e:
        print(e)

    # Klasa DerivedHandler
    print("\n=== Klasa DerivedHandler ===")
    derived_handler = DerivedHandler()
    derived_handler.handle_event("Inne zdarzenie tekstowe")
    derived_handler.handle_event(789)  # Obsługa zmieniona dla int
    derived_handler.handle_event(3.14)  # Obsługa float zarejestrowana w DerivedHandler

    # Niespodzianka: prosze sprawdzic co zobaczymy?
    handler.handle_event(12356789)