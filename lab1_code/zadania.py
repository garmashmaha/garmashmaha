import time

def suma_od_1_do_n(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

n = 1000000  # Przykład: obliczenie sumy od 1 do 1 000 000

start_time = time.time()
wynik = suma_od_1_do_n(n)
end_time = time.time()

print("Wynik:", wynik)
print("Czas wykonania:", end_time - start_time, "sekundy")
