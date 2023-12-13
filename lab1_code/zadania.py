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

# ZADANIE6: Generowanie tablicy 100 pseudo-randomowych liczb
tablica_liczb = [random.randint(1, 1000) for _ in range(100)]

# ZADANIE7: Implementacja sortowania bąbelkowego
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Sortowanie tablicy z ZADANIA6
bubble_sort(tablica_liczb)

# ZADANIE8: Sortowanie setu z ZADANIA4 za pomocą sortowania bąbelkowego
set_do_posortowania = {elem['name'] for elem in lista_imion if elem['type'] == typ_imienia_do_wyszukania}
set_posortowany = list(set_do_posortowania)
bubble_sort(set_posortowany)

# ZADANIE9: Wyszukiwanie imienia 'JULIAN' w posortowanej tablicy z ZADANIA7
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return f"Imię {item} zostało znalezione na pozycji {mid}."
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return f"Imię {item} nie zostało znalezione."

# Wyszukiwanie imienia 'JULIAN' w posortowanej tablicy
wynik_wyszukiwania = binary_search(tablica_liczb, 500)  # Wyszukiwanie przykładowej liczby 500

# ZADANIE10: Pomiar czasu sortowania i wyszukiwania
start_time_sortowania = time.time()
bubble_sort(tablica_liczb)
end_time_sortowania = time.time()
czas_sortowania = end_time_sortowania - start_time_sortowania

start_time_wyszukiwania = time.time()
wynik_wyszukiwania = binary_search(tablica_liczb, 500)  # Wyszukiwanie przykładowej liczby 500
end_time_wyszukiwania = time.time()
czas_wyszukiwania = end_time_wyszukiwania - start_time_wyszukiwania

# Wyświetlenie czasu sortowania i wyszukiwania
print("Czas sortowania:", czas_sortowania, "sekundy")
print("Czas wyszukiwania:", czas_wyszukiwania, "sekundy")
