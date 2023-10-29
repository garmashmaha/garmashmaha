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
