def bellman_ford(graph, start_vertex):
    # Inicjalizujemy odległości od wierzchołka startowego do wszystkich innych wierzchołków jako nieskończoność.
    distance = {vertex: float('infinity') for vertex in graph}
    # Odległość od wierzchołka startowego do samego siebie to oczywiście 0.
    distance[start_vertex] = 0

    # Przechodzimy przez wszystkie wierzchołki, V-1 razy, gdzie V to liczba wierzchołków w grafie.
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbour in graph[vertex]:
                # Jeśli odległość do sąsiada przez bieżący wierzchołek jest mniejsza niż dotychczas znana
                # najkrótsza odległość do sąsiada, aktualizujemy najkrótszą odległość.
                if distance[vertex] + graph[vertex][neighbour] < distance[neighbour]:
                    distance[neighbour] = distance[vertex] + graph[vertex][neighbour]

    # Sprawdzamy cykle o ujemnej wadze.
    for vertex in graph:
        for neighbour in graph[vertex]:
            assert distance[vertex] + graph[vertex][neighbour] >= distance[neighbour], "Graf zawiera cykl o ujemnej wadze"

    return distance

# Tworzymy graf na podstawie danych wprowadzonych przez użytkownika.
graph = create_graph()

start_vertex = input("Podaj wierzchołek startowy: ")

# Wywołujemy funkcję bellman_ford i wyświetlamy wynik.
print(bellman_ford(graph, start_vertex))
