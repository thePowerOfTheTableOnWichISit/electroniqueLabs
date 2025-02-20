import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
import scipy.optimize as opt


def évaluer_signal_stationnaire(tension_values):
    tension_values = np.array(tension_values)

    # Calcul moyenne
    mean_tension = np.mean(tension_values)

    # Calcul variance
    variance_tension = np.var(tension_values)

    #Calcul SNR
    SNR = mean_tension**2 / variance_tension

    return mean_tension, variance_tension, SNR


def Constructeur_de_Graphique_index(file_path, Titre):
    with open(file_path, 'r') as file:
        données = [ligne.replace(",", ".") for ligne in file]
        données = [ligne.split("\t")[1] for ligne in données]

    num_mesure = np.arange(len(données))
    tension_values = np.array(données, dtype=float)

    # Création du graphique
    plt.figure(figsize=(10, 6))

    plt.scatter(num_mesure, tension_values, color='red', label=None, s=4)

    # Ajout des annotations
    plt.xlabel('Index de la mesure[-]', fontsize=12)
    plt.ylabel('Tension [V]', fontsize=12)
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
    plt.legend([f"Valeurs uniques:\n\n{valeurs_uniques}"], fontsize=10, loc='upper center', bbox_to_anchor=(0.17, -0.15), handles=[text_proxy])

    # Affichage
    plt.tight_layout()
    plt.show()


def évaluer_signal_stationnaire(tension_values):
    tension_values = np.array(tension_values)

    # Calcul moyenne
    mean_tension = np.mean(tension_values)

    # Calcul variance
    variance_tension = np.var(tension_values)

    #Calcul SNR
    SNR = mean_tension**2 / variance_tension

    return mean_tension, variance_tension, SNR


def Constructeur_de_Graphique_XY(file_path, titre, range_graph=None):
    with open(file_path, 'r') as file:
        strings_brutes = [ligne.replace(",", ".") for ligne in file]
        data_dict = {}
        for i in range(len(strings_brutes[0].strip().split('\t'))):
            data_dict[f'col_{i+1}'] = []
        for string_brute in strings_brutes:
            donnée = string_brute.strip().split('\t')
            for i, value in enumerate(donnée):
                data_dict[f'col_{i+1}'].append(float(value))

    y = np.array(data_dict[f'col_{len(donnée)}'])
    x = np.array(data_dict[f'col_{1}'], dtype=float)
    # Création du graphique
    plt.figure(figsize=(10, 6))

    initial_guess = [1e-9, 0.025]  # Typical values for a diode

    # Fit the data
    params, covariance = opt.curve_fit(diode_equation, y, x, p0=initial_guess)

    # Extract the fitted parameters
    I0_fit, V0_fit = params
    voltage_smooth = np.linspace(min(y), max(y), 100)
    fitted_current = diode_equation(voltage_smooth, I0_fit, V0_fit)

    plt.scatter(y, x, color='red', label=None, s=4)
    plt.plot(voltage_smooth, fitted_current, label="Fitted Curve", linestyle="--", color='blue')

    # Ajout des annotations
    plt.xlabel('Tension [V]', fontsize=12)
    plt.ylabel('Résistance dynamique [ohm]', fontsize=12)
    #plt.title(Titre, fontsize=14, fontweight='bold')
    plt.minorticks_on()
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.4f"))
    if range_graph is not None:
        plt.ylim(range_graph[0], range_graph[1])

    #Légende
    valeurs_uniques = (
        titre
    )
    text_proxy = mpatches.Patch(color='none', label=f"{valeurs_uniques}")
    plt.legend([f"{valeurs_uniques}"], fontsize=15, loc='upper center', bbox_to_anchor=(0.46, -0.15), handles=[text_proxy], frameon=False)

    # Affichage
    plt.tight_layout()
    plt.show()


def calculate_dynamic_resistance(current, voltage):
    n = len(current)
    RD = np.zeros(n-2)
    for i in range(1, n - 2):
        dV = voltage[i + 1] - voltage[i - 1]
        dI = current[i + 1] - current[i - 1]
        RD[i-1] = abs(dV) / abs(dI)
    
    return RD

def diode_equation(V, I0, V0):
    return I0 * (np.exp(V / V0) - 1)