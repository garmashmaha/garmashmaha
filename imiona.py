# 1. Przechowywanie danych
osoby = {
    "Kamil": {"znajomi": ["Magda", "Piotr", "Daniel"], "rzeczy": []},
    "Magda": {"znajomi": ["Kamil", "Ewa", "Liliana"], "rzeczy": ["kamera"]},
    "Ewa": {"znajomi": ["Magda", "Liliana", "Daniel"], "rzeczy": []},
    "Piotr": {"znajomi": ["Kamil"], "rzeczy": ["kamera", "statyw"]},
    "Nikodem": {"znajomi": ["Mikołaj"], "rzeczy": []},
    "Mikołaj": {"znajomi": ["Nikodem", "Daniel"], "rzeczy": ["kamera"]},
    "Liliana": {"znajomi": ["Magda", "Ewa"], "rzeczy": ["kamera"]},
    "Daniel": {"znajomi": ["Kamil", "Ewa", "Mikołaj"], "rzeczy": []}
}

# 3. API sprawdzające czy osoby się znają
def czy_znaja_sie(osoba1, osoba2):
    return osoba2 in osoby[osoba1]["znajomi"]

# API zwracające przyjaciół po podaniu imienia
def znajomi(osoba):
    return osoby[osoba]["znajomi"]

# 4. API pokazujące ścieżkę - kogo najszybciej zapytać o pożyczenie przedmiotu
def kogo_zapytac(osoba, rzecz):
    kolejka = [(osoba, [osoba])]
    odwiedzone = set()
    while kolejka:
        (osoba, sciezka) = kolejka.pop(0)
        if rzecz in osoby[osoba]["rzeczy"]:
            return sciezka
        elif osoba not in odwiedzone:
            odwiedzone.add(osoba)
            for znajomy in osoby[osoba]["znajomi"]:
                kolejka.append((znajomy, sciezka + [znajomy]))
    return None