import numpy as np
import matplotlib.pyplot as plt


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
    uncertainty = 0.005 * np.abs(tension_values)

    # Création du graphique
    plt.figure(figsize=(10, 6))

    plt.errorbar(
        num_mesure,
        tension_values,
        yerr=uncertainty,
        fmt='o',
        color='red',
        ecolor='blue',
        elinewidth=0.8,
        capsize=2,
        label=None,
        markersize=4
    )

    plt.scatter(num_mesure, tension_values, color='red', label=None, s=10)

    # Ajout des annotations
    plt.xlabel('Numéro de mesure', fontsize=12)
    plt.ylabel('Tension (V)', fontsize=12)
    plt.title(Titre, fontsize=14, fontweight='bold')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.minorticks_on()

    #Légende
    a = évaluer_signal_stationnaire(tension_values)
    valeurs_uniques = (
        f"$\\bar{{v}}$= {a[0]:.2f} V\n"
        f"$\\sigma^2$= {a[1]:.2e} V²\n"
        f"SNR= {a[2]:.2f}"
    )
    plt.legend([f"Valeurs uniques:\n\n{valeurs_uniques}"], fontsize=10, loc='center left', bbox_to_anchor=(1, 0.5))

    # Affichage
    plt.tight_layout()
    plt.show()