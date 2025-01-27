from multipledispatch import dispatch
import math

class Figura(object):
    def __init__(self):
        print("Figura init")

class Prostokat(Figura):
    x: int
    y: int
    def __init__(self, x: int, y: int):
        print("Prostokat")
        self.x = x
        self.y = y

class Kwadrat(Prostokat):
    x: int
    def __init__(self, x: int):
        # print("Kwadrat")
        self.x = x

class Kolo(Figura):
    r: float
    def __init__(self, r: float):
        print("Kolo")
        self.r = r


@dispatch(Figura)
def pole(instance: Figura):
    print("Pole: Figura")
    return 0

@dispatch(Prostokat)
def pole(instance: Prostokat):
    return instance.x * instance.y

@dispatch(Prostokat, int, int)
def pole(instance: Prostokat, x: int, y: int):
    return x * y

@dispatch(Kwadrat)
def pole(instance: Kwadrat):
    return instance.x ** 2

@dispatch(Kwadrat, int)
def pole(instance: Kwadrat, x: int):
    return x ** 2

@dispatch(Kolo)
def pole(instance: Kolo):
    print("Pole: Kolo (bez podania promienia)")
    return math.pi * (instance.r ** 2)

@dispatch(Kolo, float)
def pole(instance: Kolo, r: float):
    print(f"Pole: Kolo (z podaniem promienia {r})")
    return math.pi * (r ** 2)

def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(f"Pole obiektu: {pole(i)}")

if __name__ == "__main__":
    print("=== Tworzenie obiektów ===")
    a, b, c, d = Figura(), Prostokat(2, 4), Kwadrat(2), Kolo(3)

    # Wywołania funkcji pole
    print("\n=== Wywołania funkcji pole ===")
    print(f"Pole prostokąta (2x4): {pole(b)}")
    print(f"Pole kwadratu (bok=2): {pole(c)}")
    print(f"Pole koła (r=3): {pole(d)}")

    # Zmiana wymiarów za pomocą funkcji pole
    print("\n=== Zmiana wymiarów ===")
    print(f"Pole prostokąta po zmianie na 5x6: {pole(b, 5, 6)}")
    print(f"Pole kwadratu po zmianie boku na 7: {pole(c, 7)}")
    print(f"Pole koła po zmianie promienia na 4: {pole(d, 4.0)}")

    # Polimorfizm
    print("\n=== Polimorfizm w czasie wykonywania ===")
    polaPowierzchni([a, b, c, d])
