import matplotlib.pyplot as plt
import networkx as nx

# Define options for drawing nodes
options1 = {
    "font_size": 11,
    "node_size": 1500,
    "node_shape": "s",
    "alpha": 0.5,
    "node_color": "white",
    "linewidths": 40,
    "width": 3
}
options2 = {
    "node_size": 1500,
    "node_shape": "s",
    "alpha": 0.5,
    "node_color": "orange",
    "linewidths": 40
}
options3 = {
    "node_size": 1500,
    "node_shape": "s",
    "alpha": 0.5,
    "node_color": "skyblue",
    "linewidths": 40
}

# Create directed graph
G = nx.DiGraph()

# Define edges
edges = [
    ("inside", "boulder"), ("outside", "boulder"), ("artifical", "outside"), ("natural", "outside"),
    ("boulder", "climable Object"), ("climbing Route", "climable Object"), ("start", "climbing Route"), ("end", "climbing Route"),
    ("mountain", "climable Object"), ("sattlepoint", "mountain"), ("summit", "mountain"), ("foot", "sattlepoint"), ("secondary Summit", "summit"),
    ("mountain", "mountain Range"), ("Alpen", "mountain Range"), ("Mt. Blanc", "Alpen"), ("Mt. Blanc", "mountain"), ("Kletter Ei", "artifical"),
    ("end", "summit"), ("start", "foot")
]
G.add_edges_from(edges)

# Add attributes to nodes
node_attributes = {
    "inside": {"type": "location", "altitude": 500},
    "outside": {"type": "location", "altitude": 1000},
    "boulder": {"type": "object", "difficulty": "medium"},
    "climable Object": {"type": "category", "description": "Objects that can be climbed"},
    "climbing Route": {"type": "route", "length_km": 2},
    "start": {"type": "point", "altitude": 1500},
    "end": {"type": "point", "altitude": 2000},
    "mountain": {"type": "object", "height_m": 3000},
    "sattlepoint": {"type": "point", "altitude": 2800},
    "summit": {"type": "point", "altitude": 3200},
    "foot": {"type": "point", "altitude": 1500},
    "secondary Summit": {"type": "point", "altitude": 3100},
    "mountain Range": {"type": "category", "description": "Ranges of mountains"},
    "Alpen": {"type": "range", "location": "Europe"},
    "Mt. Blanc": {"type": "mountain", "height_m": 4808},
    "Kletter Ei": {"type": "object", "difficulty": "high"},
    "artifical": {"type": "object", "man_made": True},
    "natural": {"type": "object", "man_made": False},
}

for node, attrs in node_attributes.items():
    G.add_node(node, **attrs)
    
# Add attributes to edges
edge_attributes = {
    ("inside", "boulder"): {"relationship": "specialisation"},
    ("outside", "boulder"): {"relationship": "specialisation"},
    ("artifical", "outside"): {"relationship": "specialisation"},
    ("natural", "outside"): {"relationship": "specialisation"},
    ("climable Object", "boulder"): {"relationship": "specialisation"},
    ("climable Object", "climbing Route"): {"relationship": "part of"},
    ("climbing Route", "start"): {"relationship": "part of"},
    ("climbing Route", "end"): {"relationship": "part of"},
    ("climable Object", "mountain"): {"relationship": "specialisation"},
    ("mountain", "sattlepoint"): {"relationship": "part of"},
    ("mountain", "summit"): {"relationship": "part of"},
    ("sattlepoint", "foot"): {"relationship": "part of"},
    ("summit", "secondary Summit"): {"relationship": "specialisation"},
    ("mountain Range", "mountain"): {"relationship": "part of"},
    ("Alpen", "mountain Range"): {"relationship": "instance of"},
    ("Alpen", "Mt. Blanc"): {"relationship": "part of"},
    ("mountain", "Mt. Blanc"): {"relationship": "instance of"},
    ("artifical", "Kletter Ei"): {"relationship": "instance of"},
}

for (u, v), attrs in edge_attributes.items():
    G.add_edge(u, v, **attrs)
    
# Group nodes by column
level_5_nodes = ["mountain Range"]
level_4_nodes = ["boulder", "climable Object", "mountain", "Alpen"]
level_3_nodes = ["inside", "outside", "summit", "sattlepoint", "Mt. Blanc"]
level_2_nodes = ["natural", "artifical", "climbing Route", "secondary Summit", "foot"]
level_1_nodes = ["Kletter Ei", "end", "start"]

# Set the position according to column (x-coord)
pos = {n: (i + 1.5, 2) for i, n in enumerate(level_4_nodes)}
pos.update({n: (i + 5, 3) for i, n in enumerate(level_5_nodes)})
pos.update({n: (i + 1, 1) for i, n in enumerate(level_3_nodes)})
pos.update({n: (i + 0.5, 0) for i, n in enumerate(level_2_nodes)})
pos.update({n: (i + 2, -1) for i, n in enumerate(level_1_nodes)})

# Set the edge labels
p = "part of"
s = "specialisation"
i = "instance of"
edge_labels = {("inside", "boulder"): s, ("outside", "boulder"): s, ("artifical", "outside"): s, ("natural", "outside"): s,
               ("climable Object", "boulder"): s, ("climable Object", "climbing Route"): p, ("climbing Route", "start"): p, ("climbing Route", "end"): p,
               ("climable Object", "mountain"): s, ("mountain", "sattlepoint"): p, ("mountain", "summit"): p, ("sattlepoint", "foot"): p, ("summit", "secondary Summit"): s,
               ("mountain Range", "mountain"): p, ("Alpen", "mountain Range"): i, ("Alpen", "Mt. Blanc"): p, ("mountain", "Mt. Blanc"): i, ("artifical", "Kletter Ei"): i}

# Combine node labels and attributes for annotation
node_attr_labels = {node: f"{node}" for node, attrs in G.nodes(data=True)}

# Draw the graph
nx.draw_networkx_nodes(G, pos, nodelist=["climbing Route", "climable Object"], **options2)
nx.draw_networkx_nodes(G, pos, nodelist=["boulder", "mountain"], **options3)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_labels(G, pos, labels=node_attr_labels, font_size=8) # Adjust font size to 8 to match the annotation
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color="grey")

# Set margins for the axes so that nodes aren't clipped
plt.axis("off")
plt.show()
