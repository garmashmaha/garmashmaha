from flask import Flask, jsonify
import json
import random
import time
from collections import Counter

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
    
def popularne_imiona(sciezka):
    with open(sciezka, "r") as file:
        imiona=json.load(file)
        
    counter_imion = Counter([imie['name'] for imie in imiona])

    # Wybór najpopularniejszych imion (występujących więcej niż raz)
    najpopularniejsze = [imie for imie, count in counter_imion.items() if count > 1]

    return jsonify({"najpopularniejsze_imiona": najpopularniejsze})

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

# Endpointy dla zadań

@app.route('/zadanie0/<int:n>', methods=['GET'])
def zadanie0(n):
    return jsonify({"suma": suma_od_1_do_n(n)})

@app.route('/zadanie1', methods=['GET'])
def zadanie1():
    wynik, czas_wykonania = zmierz_czas(suma_od_1_do_n, 1000)  # Przykładowe wykonanie dla n=1000
    return jsonify({"wynik": wynik, "czas_wykonania": czas_wykonania})

@app.route('/zadanie2', methods=['GET'])
def zadanie2():
    sciezka_do_pliku = "lab1_code/imie.json"  # Ścieżka do pliku JSON z danymi
    najpopularniejsze_imiona = popularne_imiona(sciezka_do_pliku)
    return najpopularniejsze_imiona

@app.route('/zadanie3/<imie>', methods=['GET'])
def zadanie3(imie):
    sciezka_do_pliku = "lab1_code/imie.json"  # Ścieżka do pliku JSON z danymi
    lista_imion = wczytaj_dane_z_json(sciezka_do_pliku)
    wynik = znajdz_imie(imie, [elem['name'] for elem in lista_imion])
    #wynik = znajdz_imie(imie, lista_imion)
    return jsonify({"wynik": wynik})

@app.route('/zadanie4/<imie>/<typ_imienia>', methods=['GET'])
def zadanie4(imie, typ_imienia):
    sciezka_do_pliku = "lab1_code/imie.json"  # Ścieżka do pliku JSON z danymi
    lista_imion = wczytaj_dane_z_json(sciezka_do_pliku)
    wynik = znajdz_imie_w_typie(imie, lista_imion, typ_imienia)
    return jsonify({"wynik": wynik})

@app.route('/zadanie5', methods=['GET'])
def zadanie5():
    sciezka_do_pliku = "lab1_code/imie.json"  # Ścieżka do pliku JSON z danymi
    lista_imion = wczytaj_dane_z_json(sciezka_do_pliku)
    unikalne = unikalne_imiona(lista_imion)
    return jsonify({"unikalne_imiona": unikalne})

@app.route('/zadanie6', methods=['GET'])
def zadanie6():
    return jsonify({"liczby": generuj_liczby()})

@app.route('/zadanie7', methods=['GET'])
def zadanie7():
    liczby = generuj_liczby()
    posortowane = bubble_sort(liczby)
    return jsonify({"posortowane": posortowane})

@app.route('/zadanie8/<typ_imienia>', methods=['GET'])
def zadanie8(typ_imienia):
    sciezka_do_pliku = "lab1_code/imie.json"  # Ścieżka do pliku JSON z danymi
    lista_imion = wczytaj_dane_z_json(sciezka_do_pliku)
    wynik = [elem['name'] for elem in lista_imion if elem['type'] == typ_imienia]
    posortowany = bubble_sort(wynik)
    return jsonify({"posortowane_imiona_typu": posortowany})


@app.route('/zadanie9', methods=['GET'])
def zadanie9():
    liczby = generuj_liczby()
    posortowane = bubble_sort(liczby)
    wynik_wyszukiwania = binary_search(posortowane, 500)  # Wyszukiwanie przykładowej liczby 500
    return jsonify({"wynik_wyszukiwania": wynik_wyszukiwania})

if __name__ == '__main__':
    app.run(debug=True)
