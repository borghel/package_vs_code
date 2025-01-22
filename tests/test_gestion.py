import pytest
import os
from gestion_utilisateurs.gestion import GestionUtilisateurs
from gestion_utilisateurs.exceptions import UtilisateurExistantError, UtilisateurNonTrouveError


@pytest.fixture
def gestion(tmp_path):
    """Fixture pour initialiser GestionUtilisateurs avec un fichier JSON temporaire."""
    fichier_test = tmp_path / "test_utilisateurs.json"
    return GestionUtilisateurs(fichier_test)


def test_ajouter_utilisateur(gestion):
    gestion.ajouter_utilisateur("Alice", "alice@example.com")
    assert len(gestion.afficher_utilisateurs()) == 1
    assert gestion.afficher_utilisateurs()[0]["email"] == "alice@example.com"


def test_ajouter_utilisateur_existant(gestion):
    gestion.ajouter_utilisateur("Alice", "alice@example.com")
    with pytest.raises(UtilisateurExistantError):
        gestion.ajouter_utilisateur("Alice", "alice@example.com")


def test_supprimer_utilisateur(gestion):
    gestion.ajouter_utilisateur("Alice", "alice@example.com")
    gestion.supprimer_utilisateur("alice@example.com")
    assert len(gestion.afficher_utilisateurs()) == 0


def test_supprimer_utilisateur_inexistant(gestion):
    with pytest.raises(UtilisateurNonTrouveError):
        gestion.supprimer_utilisateur("nonexistent@example.com")
