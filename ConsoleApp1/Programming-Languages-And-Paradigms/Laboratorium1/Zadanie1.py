def podzielPaczki(wagi, max_waga):
    for waga in wagi:
        if waga > max_waga:
            raise ValueError(f"Paczka i wafze {waga} przekracza max dozwoloną wagę kursu ({max_waga} kg).")

    wagi_sorted = sorted(wagi, reverse = True)
    kursy = []

    for waga in wagi_sorted:
        dodano = False
        for kurs in kursy:
            if sum(kurs) + waga <= max_waga:
                kurs.append(waga)
                dodano = True
                break

        if not dodano:
            kursy.append([waga])

    return len(kursy), kursy
wagi = [20, 5, 8, 15, 10, 10, 7]
max_waga = 25;

#print(podzielPaczki(wagi, max_waga))
liczba_kursow, kursy = podzielPaczki(wagi, max_waga)
for i, kurs in enumerate (kursy, 1):
    print(f"Kurs {i}: {kurs} \t suma wagi: {sum(kurs)} kg")