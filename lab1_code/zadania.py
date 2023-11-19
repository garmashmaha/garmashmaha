import json
import time

def suma_od_1_do_n(n):
    return sum(range(1, n + 1))

def zmierz_czas(funkcja, *args):
    start_time = time.time()
    wynik = funkcja(*args)
    end_time = time.time()
    return wynik, end_time - start_time

def wczytaj_dane_z_json(sciezka):
    with open(sciezka, "r") as file:
        return json.load(file)

def znajdz_imie(imie, lista_imion):
    return f"Imię {imie} {'jest' if imie in lista_imion else 'nie występuje'} na liście."

def znajdz_imie_w_typie(imie, lista_imion, typ_imienia):
    is_imie = any(elem['name'] == imie and elem['type'] == typ_imienia for elem in lista_imion)
    return f"Imię {imie} {'jest' if is_imie else 'nie występuje'} na liście typu {typ_imienia}."

# ZADANIE 2: Wczytaj dane z pliku JSON
sciezka_do_pliku = "/home/codespace/.python/garmashmaha/lab1_code/imiona.json"
lista_imion = wczytaj_dane_z_json(sciezka_do_pliku)

# ZADANIE 3: Wyszukiwanie imienia "Julian" w liście imion
imie_do_wyszukania = "Julian"
wynik, czas_wyszukania = zmierz_czas(znajdz_imie, imie_do_wyszukania, [elem['name'] for elem in lista_imion])

print(wynik)
print("Czas wykonania:", czas_wyszukania, "sekundy")

# ZADANIE 4: Wyszukiwanie imienia "Julian" w liście imion typu "HISPANIC"
typ_imienia_do_wyszukania = "HISPANIC"
wynik, czas_wyszukania_typ = zmierz_czas(znajdz_imie_w_typie, imie_do_wyszukania, lista_imion, typ_imienia_do_wyszukania)

print(wynik)
print("Czas wykonania:", czas_wyszukania_typ, "sekundy")

# ZADANIE 5: Tworzenie unikalnej listy imion bez powtórzeń
unikalne_imiona = list({elem['name'] for elem in lista_imion})

# Wypisz unikalne imiona
print(unikalne_imiona)
