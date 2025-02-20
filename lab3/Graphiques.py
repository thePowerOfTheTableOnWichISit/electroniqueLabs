import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

import Graph


titres = [
          "valeur de courant traversant une diode standard en polarité direct",
          "valeur de courant traversant une diode standard en polarité inverse"
          ]

emps = [
        "lab3/diodPopodirect.lvm",
        "lab3/diodPopoInverse.lvm",
        ]

graphiques = []
for i, j in zip(titres, emps):
    graphiques.append(Graph.Constructeur_de_Graphique_XY(j, i))
