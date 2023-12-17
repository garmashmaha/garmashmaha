import heapq  # Importujemy moduł heapq, który zawiera implementację kolejki priorytetowej.

def dijkstra(graph, start):
    # Inicjalizujemy odległości od wierzchołka startowego do wszystkich innych wierzchołków jako nieskończoność.
    distances = {vertex: float('infinity') for vertex in graph}
    # Odległość od wierzchołka startowego do samego siebie to oczywiście 0.
    distances[start] = 0

    # Tworzymy kolejkę priorytetową, gdzie każdy element to para (odległość, wierzchołek).
    # Na początku dodajemy do niej tylko wierzchołek startowy z odległością 0.
    priority_queue = [(0, start)]

    while priority_queue:
        # Zdejmujemy wierzchołek o najmniejszej odległości.
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Przechodzimy przez wszystkie wierzchołki sąsiadujące z bieżącym wierzchołkiem.
        for neighbor, weight in graph[current_vertex].items():
            # Obliczamy odległość do sąsiada przez bieżący wierzchołek.
            distance = current_distance + weight

            # Jeśli znaleźliśmy krótszą ścieżkę do sąsiada, aktualizujemy jego odległość
            # i dodajemy go do kolejki priorytetowej.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Zwracamy słownik odległości od wierzchołka startowego do wszystkich innych wierzchołków.
    return distances

def create_graph():
    # Pytamy użytkownika o liczbę wierzchołków.
    num_vertices = int(input("Podaj liczbę wierzchołków: "))
    graph = {}

    for i in range(num_vertices):
        name = input(f"Podaj nazwę wierzchołka {i+1}: ")
        graph[name] = {}
        num_edges = int(input(f"Podaj liczbę krawędzi z wierzchołka {name}: "))

        for j in range(num_edges):
            edge_name = input(f"Podaj nazwę wierzchołka docelowego dla krawędzi {j+1} z {name}: ")
            edge_weight = int(input(f"Podaj wagę dla krawędzi {j+1} z {name} do {edge_name}: "))

            # Dodajemy krawędź do grafu.
            graph[name][edge_name] = edge_weight

    # Zwracamy utworzony graf.
    return graph

# Tworzymy graf na podstawie danych wprowadzonych przez użytkownika.
graph = create_graph()

start_vertex = input("Podaj wierzchołek startowy: ")

# Wywołujemy funkcję dijkstra i wyświetlamy wynik.
print(dijkstra(graph, start_vertex))
