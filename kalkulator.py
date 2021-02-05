import logging
logging.basicConfig(level=logging.DEBUG)

dzialanie = int(input("Podaj działanie posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie,"
                  " 4 Dzielenie: "))

while dzialanie not in (1, 2, 3, 4):
    dzialanie = int(input("Podaj działanie posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie,"
                          " 4 Dzielenie: "))


def odejmowanie(skladnik_1, skladnik_2):
    return skladnik_1 - skladnik_2

def dzielenie(skladnik_1, skladnik_2):
    return skladnik_1 / skladnik_2

if dzialanie == 1:
    skladniki = input("Podaj składniki oddzielone przecinkami: ")
    wynik = sum([int(item) for item in skladniki.split(',')])
    info = f'Dodaje do siebie {skladniki}'
elif dzialanie == 2:
    skladnik_1 = int(input("Podaj składnik 1: "))
    skladnik_2 = int(input("Podaj składnik 2: "))
    wynik = odejmowanie(skladnik_1, skladnik_2)
    info = f'Odejmuje {skladnik_1} - {skladnik_2}'
elif dzialanie == 3:
    skladniki = input("Podaj składniki oddzielone przecinkami: ")
    skladniki = [int(item) for item in skladniki.split(',')]
    wynik = 1
    for item in skladniki:
        wynik *= item
    info = f'Mnoze przez siebie {skladniki}'
elif dzialanie == 4:
    skladnik_1 = int(input("Podaj składnik 1: "))
    skladnik_2 = int(input("Podaj składnik 2: "))
    while skladnik_2 == 0:
        skladnik_2 = int(input("Nie dzieli sie przez zero. Podaj liczbe wieksza od zera: "))
    wynik = dzielenie(skladnik_1, skladnik_2)
    info = f'Dziele {skladnik_1} przez {skladnik_2}'


print(f"Wynik to {wynik}")
logging.info(info)




