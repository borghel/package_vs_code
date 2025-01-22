import os
import json
from gestion_utilisateurs.utils import sauvegarder_donnees, charger_donnees


def test_sauvegarder_et_charger_donnees(tmp_path):
    chemin = tmp_path / "utilisateurs.json"
    donnees = [{"nom": "Alice", "email": "alice@example.com"}]

    # Test sauvegarde
    sauvegarder_donnees(chemin, donnees)
    assert os.path.exists(chemin)

    # Test chargement
    donnees_chargees = charger_donnees(chemin)
    assert donnees_chargees == donnees
