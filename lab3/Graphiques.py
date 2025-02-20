import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

import Graph


titres = [
          "Figure 1 - Valeur de courant traversant une diode standard en polarité direct. \nDonnées mesurées en rouge, Données obtenue avec l'équation de Shockley en bleu",
          "Figure 2 - valeur de courant traversant une diode standard en polarité inverse"
          ]

emps = [
        "lab3/diodPopodirect.lvm",
        "lab3/diodPopoInverse.lvm",
        ]


Graph.Constructeur_de_Graphique_XY(emps[0], titres[0])
Graph.Constructeur_de_Graphique_XY(emps[1], titres[1], range_graph=(-0.1, 0.1))
