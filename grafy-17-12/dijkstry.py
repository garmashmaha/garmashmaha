import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def create_graph():
    num_vertices = int(input("Podaj liczbę wierzchołków: "))
    graph = {}
    for i in range(num_vertices):
        name = input(f"Podaj nazwę wierzchołka {i+1}: ")
        graph[name] = {}
        num_edges = int(input(f"Podaj liczbę krawędzi z wierzchołka {name}: "))
        for j in range(num_edges):
            edge_name = input(f"Podaj nazwę wierzchołka docelowego dla krawędzi {j+1} z {name}: ")
            edge_weight = int(input(f"Podaj wagę dla krawędzi {j+1} z {name} do {edge_name}: "))
            graph[name][edge_name] = edge_weight
    return graph

graph = create_graph()
start_vertex = input("Podaj wierzchołek startowy: ")
print(dijkstra(graph, start_vertex))
