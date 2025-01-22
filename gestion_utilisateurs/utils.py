import json


def sauvegarder_donnees(chemin, donnees):
    """Sauvegarde les données dans un fichier JSON."""
    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, indent=4)
    print(f"Données sauvegardées dans {chemin}.")


def charger_donnees(chemin):
    """Charge les données depuis un fichier JSON."""
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []
