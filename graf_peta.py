import networkx as nx
import matplotlib.pyplot as plt

# Data graf kota 
edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'D', 2),
    ('B', 'E', 5),
    ('C', 'F', 3),
    ('E', 'F', 1)
]

# Graf kosong
G = nx.Graph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Posisi node pada peta (disusun manual agar rapi)
pos = {
    'A': (0, 2),
    'B': (1, 3),
    'C': (1, 1),
    'D': (2, 4),
    'E': (2, 2),
    'F': (3, 1)
}

# Ukuran dan warna node
node_colors = 'skyblue'
node_size = 1500

# Gambar node dan edge
plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=node_colors)
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Label bobot (jarak)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)

# Judul dan tampilkan
plt.title("Peta Kota Pengiriman Barang (Graf untuk A* Search)", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()
