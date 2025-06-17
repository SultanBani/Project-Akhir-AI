import heapq

class Node:
    def __init__(self, name, g, h, parent=None):
        self.name = name
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def a_star_search(graph, heuristics, start, goal):
    open_list = []
    closed_list = set()

    start_node = Node(start, 0, heuristics.get(start, 0))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.name == goal:
            path = []
            total_cost = current_node.g
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1], total_cost

        closed_list.add(current_node.name)

        for neighbor, cost in graph.get(current_node.name, []):
            if neighbor in closed_list:
                continue

            g = current_node.g + cost
            h = heuristics.get(neighbor, 0)
            neighbor_node = Node(neighbor, g, h, current_node)
            heapq.heappush(open_list, neighbor_node)

    return None, float('inf')


# data graf kota
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

# Estimasi heuristik jarak ke semua titik
heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 0
}

# input kita
print("Daftar kota yang tersedia:", list(graph.keys()))
start = input("Masukkan kota asal: ").strip().upper()
goal = input("Masukkan kota tujuan: ").strip().upper()

# ALGORITMA A* 
if start not in graph or goal not in graph:
    print("Kota yang dimasukkan tidak tersedia dalam peta!")
else:
    path, cost = a_star_search(graph, heuristics, start, goal)
    if path:
        print("\nRute terbaik dari", start, "ke", goal, "adalah:", " → ".join(path))
        print("Total jarak/tempuh biaya:", cost)
    else:
        print("Tidak ditemukan rute dari", start, "ke", goal)
