#podejście funkcyjne

def plecak(wagi, wartosci, pojemnosc, n):
    if n == 0 or pojemnosc == 0:
        return 0, []
    if wagi[n - 1] > pojemnosc:
        return plecak(wagi, wartosci, pojemnosc, n - 1)
    wartosc_bez = plecak(wagi, wartosci, pojemnosc, n - 1)
    wartosc_z = plecak(wagi, wartosci, pojemnosc - wagi[n - 1], n - 1)
    wartosc_z = (wartosc_z[0] + wartosci[n - 1], wartosc_z[1] + [n - 1])

    if wartosc_z[0] > wartosc_bez[0]:
        return wartosc_z
    else:
        return wartosc_bez

wagi = [2, 3, 4, 5]
wartosci = [3, 4, 5, 6]
pojemnosc = 5
maks_wartosc, przedmioty = plecak(wagi, wartosci, pojemnosc, len(wartosci))
print("Maksymalna wartość:", maks_wartosc)
print("Wybrane przedmioty:", przedmioty)
