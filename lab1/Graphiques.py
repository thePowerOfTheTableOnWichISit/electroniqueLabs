import Graph


titres = [
          "Distribution de plusieurs mesures de tension \n d'un convertisseur AC/CC",
          "Distribution de plusieurs mesures de tension \n d'un convertisseur AC/CC sur une plage de -1V à 1V",
          "Distribution de plusieurs mesures de tension d'une pile"
          ]

emps = [
        "données DC.lvm",
        "Données DC -1,1.lvm",
        "pile.lvm"
        ]

graphiques = []
for i, j in zip(titres, emps):
    graphiques.append(Graph.Constructeur_de_Graphique(j, i))
