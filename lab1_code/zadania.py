import json

# Wczytaj dane z pliku JSON
with open("imiona.json", "r") as file:
    lista_imion = json.load(file)

# Wyświetl listę najpopularniejszych imion dzieci
print(lista_imion)

import time

def suma_od_1_do_n(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

# Odczytaj wartość n z klawiatury
n = int(input("Podaj wartość n: "))

start_time = time.time()
wynik = suma_od_1_do_n(n)
end_time = time.time()

print("Wynik:", wynik)
print("Czas wykonania:", end_time - start_time, "sekundy")

def znajdz_imie(imie, lista_imion):
    if imie in lista_imion:
        return f"Imię {imie} jest na liście."
    else:
        return f"Imię {imie} nie występuje na liście."

imie_do_wyszukania = "Julian"

start_time = time.time()
wynik = znajdz_imie(imie_do_wyszukania, lista_imion)
end_time = time.time()

print(wynik)
print("Czas wykonania:", end_time - start_time, "sekundy")

def znajdz_imie_w_typie(imie, lista_imion, typ_imienia):
    if imie in [elem['name'] for elem in lista_imion if elem['type'] == typ_imienia]:
        return f"Imię {imie} jest na liście typu {typ_imienia}."
    else:
        return f"Imię {imie} nie występuje na liście typu {typ_imienia}."

imie_do_wyszukania = "Julian"
typ_imienia_do_wyszukania = "HISPANIC"

start_time = time.time()
wynik = znajdz_imie_w_typie(imie_do_wyszukania, lista_imion, typ_imienia_do_wyszukania)
end_time = time.time()

print(wynik)
print("Czas wykonania:", end_time - start_time, "sekundy")