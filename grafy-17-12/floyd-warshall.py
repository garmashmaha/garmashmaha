def floyd_warshall(graph):
    # Inicjalizujemy macierz odległości jako macierz wag krawędzi w grafie.
    distance = {v: dict(graph[v]) for v in graph}

    vertices = list(graph.keys())

    # Przechodzimy przez wszystkie wierzchołki i aktualizujemy macierz odległości.
    for k in vertices:
        for i in vertices:
            for j in vertices:
                # Jeśli odległość do wierzchołka j przez wierzchołek k jest mniejsza niż dotychczas znana
                # najkrótsza odległość do j, aktualizujemy najkrótszą odległość.
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

def create_graph():
    num_vertices = int(input("Podaj liczbę wierzchołków: "))
    graph = {}

    for _ in range(num_vertices):
        vertex_name = input("Podaj nazwę wierzchołka: ")
        graph[vertex_name] = {}

        num_edges = int(input(f"Podaj liczbę krawędzi z wierzchołka {vertex_name}: "))

        for _ in range(num_edges):
            edge_name = input(f"Podaj nazwę wierzchołka docelowego dla krawędzi z wierzchołka {vertex_name}: ")
            edge_weight = int(input(f"Podaj wagę dla krawędzi z wierzchołka {vertex_name} do wierzchołka {edge_name}: "))

            # Dodajemy krawędź do grafu.
            graph[vertex_name][edge_name] = edge_weight

    # Zwracamy utworzony graf.
    return graph

# Tworzymy graf na podstawie danych wprowadzonych przez użytkownika.
graph = create_graph()

# Wywołujemy funkcję floyd_warshall i wyświetlamy wynik.
print(floyd_warshall(graph))
