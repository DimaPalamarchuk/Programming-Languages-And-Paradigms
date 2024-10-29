#podejscie proceduralne

def proceduralne(zadanie):
    sortowane = sorted(zadanie, key=lambda x: x['czas'])
    calkowity_czas = 0
    aktualny_czas = 0
    kolejnosc = []

    for zadanie in sortowane:
        aktualny_czas += zadanie['czas']
        calkowity_czas += aktualny_czas
        kolejnosc.append(zadanie['id'])
    return kolejnosc, calkowity_czas

zadanie = [
    {'id': 1, 'czas': 4, 'nagroda': 20},
    {'id': 2, 'czas': 2, 'nagroda': 10},
    {'id': 3, 'czas': 3, 'nagroda': 15},
    {'id': 4, 'czas': 1, 'nagroda': 5}
]

kolejnosc, calkowity_czas = proceduralne(zadanie)
print("Optymalna kolejność zadań:", kolejnosc)
print("Całkowity czas oczekiwania:", calkowity_czas)
