#podejście funkcyjne

def funkcyjna(zadanie):
    sortowane = sorted(zadanie, key=lambda x: x['czas'])
    kolejnosc = [x['id'] for x in sortowane]
    calkowity_czas = 0
    aktualny_czas = 0
    for zadanie in sortowane:
        aktualny_czas += zadanie['czas']
        calkowity_czas += aktualny_czas
    return kolejnosc, calkowity_czas

zadanie = [
    {'id': 1, 'czas': 4, 'nagroda': 20},
    {'id': 2, 'czas': 2, 'nagroda': 10},
    {'id': 3, 'czas': 3, 'nagroda': 15},
    {'id': 4, 'czas': 1, 'nagroda': 5}
]

kolejnosc, calkowity_czas =funkcyjna(zadanie)
print("Optymalna kolejność zadań:", kolejnosc)
print("Całkowity czas oczekiwania:", calkowity_czas)

