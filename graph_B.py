import matplotlib.pyplot as plt
import networkx as nx

# Define options for drawing nodes
options_boulder = {
    "node_size": 1000,
    "node_shape": "o",
    "alpha": 0.7,
    "node_color": "lightgreen",
    "linewidths": 2
}
options_grip = {
    "node_size": 700,
    "node_shape": "o",
    "alpha": 0.7,
    "node_color": "lightblue",
    "linewidths": 2
}

# Create a new directed graph for the boulder and its grips
G_boulder = nx.DiGraph()

# Define grips with coordinates
grips = {
    "grip1": {"coordinates": (1, 2)},
    "grip2": {"coordinates": (2, 3)},
    "grip3": {"coordinates": (3, 4)},
    "grip4": {"coordinates": (4, 5)},
    "grip5": {"coordinates": (5, 6)},
}

# Add the boulder node
G_boulder.add_node("boulder", type="object", difficulty="medium")

# Add grip nodes and connect them to the boulder
for grip, attrs in grips.items():
    G_boulder.add_node(grip, **attrs)
    G_boulder.add_edge("boulder", grip, relationship="has_grip")

# Set positions for visualization
pos_boulder = {"boulder": (0.5, 0.5)}
pos_grips = {grip: (i, i+1) for i, grip in enumerate(grips)}
pos_boulder.update(pos_grips)

# Combine node labels and attributes for annotation
node_attr_labels_boulder = {node: f"{node}\n{attrs['coordinates']}" if 'coordinates' in attrs else node for node, attrs in G_boulder.nodes(data=True)}

# Draw the boulder graph
plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(G_boulder, pos_boulder, nodelist=["boulder"], **options_boulder)
nx.draw_networkx_nodes(G_boulder, pos_boulder, nodelist=grips.keys(), **options_grip)
nx.draw_networkx_edges(G_boulder, pos_boulder, width=1.0, alpha=0.5)
nx.draw_networkx_labels(G_boulder, pos_boulder, labels=node_attr_labels_boulder, font_size=9)
nx.draw_networkx_edge_labels(G_boulder, pos_boulder, edge_labels={("boulder", grip): "has_grip" for grip in grips}, font_size=9, font_color="grey")

# Set margins for the axes so that nodes aren't clipped
plt.axis("off")
plt.title("Boulder and Grips")
plt.show()

# Display the grips in an array format
grip_coordinates = {grip: attrs['coordinates'] for grip, attrs in grips.items()}
print("Grip Coordinates:", grip_coordinates)
