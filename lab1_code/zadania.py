import json
import time

def suma_od_1_do_n(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

def znajdz_imie(imie, lista_imion):
    if imie in lista_imion:
        return f"Imię {imie} jest na liście."
    else:
        return f"Imię {imie} nie występuje na liście."

def znajdz_imie_w_typie(imie, lista_imion, typ_imienia):
    if any(elem['name'] == imie and elem['type'] == typ_imienia for elem in lista_imion):
        return f"Imię {imie} jest na liście typu {typ_imienia}."
    else:
        return f"Imię {imie} nie występuje na liście typu {typ_imienia}."

# ZADANIE 2: Wczytaj dane z pliku JSON
with open("/home/codespace/.python/garmashmaha/lab1_code/imiona.json", "r") as file:
    lista_imion = json.load(file)

# ZADANIE 3: Wyszukiwanie imienia "Julian" w liście imion
imie_do_wyszukania = "Julian"

start_time = time.time()
wynik = znajdz_imie(imie_do_wyszukania, [elem['name'] for elem in lista_imion])
end_time = time.time()

print(wynik)
print("Czas wykonania:", end_time - start_time, "sekundy")

# ZADANIE 4: Wyszukiwanie imienia "Julian" w liście imion typu "HISPANIC"
imie_do_wyszukania = "Julian"
typ_imienia_do_wyszukania = "HISPANIC"

start_time = time.time()
wynik = znajdz_imie_w_typie(imie_do_wyszukania, lista_imion, typ_imienia_do_wyszukania)
end_time = time.time()

print(wynik)
print("Czas wykonania:", end_time - start_time, "sekundy")

# ZADANIE 5: Tworzenie unikalnej listy imion bez powtórzeń
unikalne_imiona = list(set(elem['name'] for elem in lista_imion))

# Wypisz unikalne imiona
print(unikalne_imiona)
