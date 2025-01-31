import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches


def évaluer_signal_stationnaire(tension_values):
    tension_values = np.array(tension_values)

    # Calcul moyenne
    mean_tension = np.mean(tension_values)

    # Calcul variance
    variance_tension = np.var(tension_values)

    #Calcul SNR
    SNR = mean_tension**2 / variance_tension

    return mean_tension, variance_tension, SNR


def Constructeur_de_Graphique(file_path, Titre):
    with open(file_path, 'r') as file:
        données = [ligne.replace(",", ".") for ligne in file]
        données = [ligne.split("\t")[1] for ligne in données]

    num_mesure = np.arange(len(données))
    tension_values = np.array(données, dtype=float)

    # Création du graphique
    plt.figure(figsize=(10, 6))

    plt.scatter(num_mesure, tension_values, color='red', label=None, s=4)

    # Ajout des annotations
    plt.xlabel('Index de la mesure', fontsize=12)
    plt.ylabel('Tension (V)', fontsize=12)
    plt.title(Titre, fontsize=14, fontweight='bold')
    plt.minorticks_on()
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.4f"))
    plt.ylim(min(tension_values) - min(tension_values) * 0.0003 , max(tension_values) + max(tension_values) * 0.0003)

    #Légende
    a = évaluer_signal_stationnaire(tension_values)
    valeurs_uniques = (
        f"$\\bar{{v}}$= {a[0]:.2f} V\n"
        f"$\\sigma^2$= {a[1]:.2e} V²\n"
        f"SNR= {a[2]:.2f}\n"
        f"Nombre de mesures prises = 1000"
    )
    text_proxy = mpatches.Patch(color='none', label=f"Valeurs uniques:\n\n{valeurs_uniques}")
    plt.legend([f"Valeurs uniques:\n\n{valeurs_uniques}"], fontsize=10, loc='upper center', bbox_to_anchor=(0.1, -0.15), handles=[text_proxy])

    # Affichage
    plt.tight_layout()
    plt.show()