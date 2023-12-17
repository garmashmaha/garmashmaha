def floyd_warshall(graph):
    # Inicjalizujemy macierz odległości jako macierz wag krawędzi w grafie.
    distance = graph.copy()

    num_vertices = len(graph)

    # Przechodzimy przez wszystkie wierzchołki i aktualizujemy macierz odległości.
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Jeśli odległość do wierzchołka j przez wierzchołek k jest mniejsza niż dotychczas znana
                # najkrótsza odległość do j, aktualizujemy najkrótszą odległość.
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

def create_graph():
    num_vertices = int(input("Podaj liczbę wierzchołków: "))
    graph = [[float('infinity') for _ in range(num_vertices)] for _ in range(num_vertices)]

    # Ustawiamy wartości na przekątnej na 0, ponieważ odległość od wierzchołka do samego siebie wynosi 0.
    for i in range(num_vertices):
        graph[i][i] = 0

    for i in range(num_vertices):
        num_edges = int(input(f"Podaj liczbę krawędzi z wierzchołka {i+1}: "))

        for j in range(num_edges):
            edge_index = int(input(f"Podaj indeks wierzchołka docelowego dla krawędzi {j+1} z wierzchołka {i+1}: ")) - 1
            edge_weight = int(input(f"Podaj wagę dla krawędzi {j+1} z wierzchołka {i+1} do wierzchołka {edge_index+2}: "))

            # Dodajemy krawędź do grafu.
            graph[i][edge_index] = edge_weight

    # Zwracamy utworzony graf.
    return graph

# Tworzymy graf na podstawie danych wprowadzonych przez użytkownika.
graph = create_graph()

# Wywołujemy funkcję floyd_warshall i wyświetlamy wynik.
print(floyd_warshall(graph))