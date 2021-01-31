słowo = 'kajak'
def czy_palindrom(słowo):
    return słowo == słowo[::-1]
if czy_palindrom(słowo):
    print(f"Slowo {słowo} jest palindromem")
else:
    print(f"Slowo {słowo} nie jest palindromem")
