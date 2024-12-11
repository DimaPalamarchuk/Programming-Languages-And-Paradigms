#podejście funkcyjne

def funkcyjny(wagi, wartosci, pojemnosc):
    def rekurencyjne(n, pozostala_pojemnosc):
        if n == 0 or pozostala_pojemnosc == 0:
            return 0, []
        if wagi[n - 1] > pozostala_pojemnosc:
            return rekurencyjne(n - 1, pozostala_pojemnosc)
        wartosc_bez, przedmioty_bez = rekurencyjne(n - 1, pozostala_pojemnosc)
        wartosc_z, przedmioty_z = rekurencyjne(n - 1, pozostala_pojemnosc - wagi[n - 1])
        wartosc_z += wartosci[n - 1]
        przedmioty_z = przedmioty_z + [n - 1]
        if wartosc_z > wartosc_bez:
            return wartosc_z, przedmioty_z
        else:
            return wartosc_bez, przedmioty_bez
    maks_wartosc, wybrane_przedmioty = rekurencyjne(len(wagi), pojemnosc)
    return maks_wartosc, wybrane_przedmioty

wagi = [2, 3, 4, 5]
wartosci = [3, 4, 5, 6]
pojemnosc = 5

maks_wartosc, przedmioty = funkcyjny(wagi, wartosci, pojemnosc)
print("Maksymalna wartość:", maks_wartosc)
print("Wybrane przedmioty:", przedmioty)
