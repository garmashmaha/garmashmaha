from flask import Flask, jsonify
import json
import random
import time

app = Flask(__name__)

# ZADANIE0: Funkcja, która zlicza sumę od 1 do n
def suma_od_1_do_n(n):
    return sum(range(1, n + 1))

# ZADANIE1: Zmierz czas wykonania podanej funkcji
def zmierz_czas(funkcja, *args):
    start_time = time.time()
    wynik = funkcja(*args)
    end_time = time.time()
    return wynik, end_time - start_time

# ZADANIE2: Wczytaj dane z pliku JSON
def wczytaj_dane_z_json(sciezka):
    with open(sciezka, "r") as file:
        return json.load(file)

# ZADANIE3: Wyszukaj imię w liście imion
def znajdz_imie(imie, lista_imion):
    return imie in lista_imion

# ZADANIE4: Wyszukaj imię w liście imion typu "HISPANIC"
def znajdz_imie_w_typie(imie, lista_imion, typ_imienia):
    is_imie = any(elem['name'] == imie and elem['type'] == typ_imienia for elem in lista_imion)
    return is_imie

# ZADANIE5: Tworzenie unikalnej listy imion bez powtórzeń
def unikalne_imiona(lista_imion):
    return list({elem['name'] for elem in lista_imion})

# ZADANIE6: Generowanie tablicy 100 pseudo-randomowych liczb
def generuj_liczby():
    return [random.randint(1, 1000) for _ in range(100)]

# ZADANIE7: Implementacja sortowania bąbelkowego
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# ZADANIE8: Sortowanie setu z ZADANIA4 za pomocą sortowania bąbelkowego
def sortuj_set(set_do_posortowania):
    posortowany_set = list(set_do_posortowania)
    return bubble_sort(posortowany_set)

# ZADANIE9: Wyszukiwanie imienia 'JULIAN' w zbiorze/liście z ZADANIA7
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return True
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return False
