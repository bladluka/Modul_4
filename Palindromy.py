tekst = 'A to kiwi zdziwi kota'
import string


def czy_palindrom(tekst):
    nowy_tekst = ''
    for znak in tekst:
        if znak in string.ascii_letters:
            nowy_tekst += znak
        nowy_tekst = nowy_tekst.lower()
    return nowy_tekst == nowy_tekst[::-1]


if czy_palindrom(tekst):
    print(f"Tekst {tekst} jest palindromem")
else:
    print(f"Tekst {tekst} nie jest palindromem")
