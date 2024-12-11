#Podejście procedualne

def harmonogramowanie(zadanie):
    zadanie.sort(key=lambda x: x[1])
    maks_nagroda = 0
    ostatni_koniec = 0
    wybrane_zadania = []

    for start, koniec, nagroda in zadanie:
        if start >= ostatni_koniec:
            wybrane_zadania.append((start, koniec, nagroda))
            maks_nagroda += nagroda
            ostatni_koniec = koniec
    return maks_nagroda, wybrane_zadania

zadanie = [(1, 3, 10), (2, 5, 20), (3, 6, 15), (4, 7, 30)]
maks_nagroda, harmonogram = harmonogramowanie(zadanie)
print("Maksymalna nagroda:", maks_nagroda)
print("Wybrane zadania:", harmonogram)
