import matplotlib.pyplot as plt
import networkx as nx

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

G = nx.DiGraph()
edges=([("inside","boulder"), ("outside","boulder"), ("artifical","outside"), ("natural","outside"),
                ("boulder","climable Object"),("climbing Route","climable Object"),("start","climbing Route"),("end","climbing Route"),
                ("mountain","climable Object"),("sattlepoint","mountain"),("summit","mountain"),("foot","sattlepoint"), ("secondary Summit","summit"),
                ("mountain","mountain Range"), ("Alpen","mountain Range"), ("Mt. Blanc","Alpen"), ("Mt. Blanc","mountain"), ("Kletter Ei","artifical"),
                ("end", "summit"), ("start", "foot")])
G.add_edges_from(edges)

# group nodes by column
level_5_nodes = ["mountain Range"]
level_4_nodes = ["boulder", "climable Object", "mountain", "Alpen"]
level_3_nodes = ["inside", "outside","summit","sattlepoint", "Mt. Blanc"]
level_2_nodes = ["natural", "artifical","climbing Route","secondary Summit", "foot"]
level_1_nodes = ["Kletter Ei", "end", "start"]

# set the position according to column (x-coord)
pos = {n: (i+1.5, 2) for i, n in enumerate(level_4_nodes)}
pos.update({n: ( i + 5, 3) for i, n in enumerate(level_5_nodes)})
pos.update({n: ( i + 1, 1) for i, n in enumerate(level_3_nodes)})
pos.update({n: ( i + 0.5,0) for i, n in enumerate(level_2_nodes)})
pos.update({n: ( i + 2,-1) for i, n in enumerate(level_1_nodes)})

#mapping = {0: "climable object"}
#nx.relabel_nodes(G, mapping, copy=False)

# set the edge labels
p = "part of"
s = "specialisation"
i = "instance of"
edge_labels = {("inside","boulder"):s, ("outside","boulder"):s, ("artifical","outside"):s, ("natural","outside"):s,
                ("climable Object", "boulder"):s,("climable Object", "climbing Route"):p,("climbing Route","start"):p,("climbing Route","end"):p,
                ("climable Object", "mountain"):s,("mountain","sattlepoint"):p,("mountain", "summit"):p,("sattlepoint", "foot"):p, ("summit", "secondary Summit"):s,
                ("mountain Range","mountain"):p, ("Alpen","mountain Range"):i, ("Alpen","Mt. Blanc"):p, ("mountain","Mt. Blanc"):i, ("artifical","Kletter Ei"):i}


# draw the graph
nx.draw_networkx_nodes(G, pos, nodelist=["climbing Route", "climable Object"], **options2)
nx.draw_networkx_nodes(G, pos, nodelist=["boulder", "mountain"], **options3)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color="grey")



# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
plt.axis("off")
plt.show()

