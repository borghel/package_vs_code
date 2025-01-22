import pytest
from gestion_utilisateurs.gestion import GestionUtilisateurs
from gestion_utilisateurs.exceptions import UtilisateurExistantError, UtilisateurNonTrouveError

@pytest.fixture
def gestion():
    return GestionUtilisateurs("test_utilisateurs.json")

def test_ajouter_utilisateur(gestion):
    gestion.ajouter_utilisateur("Alice", "alice@example.com")
    assert len(gestion.utilisateurs) == 1

def test_ajouter_utilisateur_existant(gestion):
    gestion.ajouter_utilisateur("Alice", "alice@example.com")
    with pytest.raises(UtilisateurExistantError):
        gestion.ajouter_utilisateur("Alice", "alice@example.com")

def test_supprimer_utilisateur(gestion):
    gestion.ajouter_utilisateur("Alice", "alice@example.com")
    gestion.supprimer_utilisateur("alice@example.com")
    assert len(gestion.utilisateurs) == 0

def test_supprimer_utilisateur_inexistant(gestion):
    with pytest.raises(UtilisateurNonTrouveError):
        gestion.supprimer_utilisateur("bob@example.com")
