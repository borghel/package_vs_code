import pytest
from gestion_utilisateurs.gestion import GestionUtilisateurs
from gestion_utilisateurs.exceptions import UtilisateurExistantError, UtilisateurNonTrouveError

@pytest.fixture
def gestion(tmp_path):
    fichier_test = tmp_path / "test_utilisateurs.json"
    return GestionUtilisateurs(fichier_test)

def test_ajouter_utilisateur(gestion):
    print("hello")
    gestion.ajouter_utilisateur("Alice", "alice@example.com")
    assert len(gestion.afficher_utilisateurs()) == 1
    assert gestion.afficher_utilisateurs()[0]["email"] == "alice@example.com"

def test_ajouter_utilisateur_existant(gestion):
    print("hello")
    gestion.ajouter_utilisateur("Alice", "alice@example.com")
    with pytest.raises(UtilisateurExistantError):
        gestion.ajouter_utilisateur("Alice", "alice@example.com")

def test_supprimer_utilisateur(gestion):
    print("hello")
    gestion.ajouter_utilisateur("Alice", "alice@example.com")
    gestion.supprimer_utilisateur("alice@example.com")
    assert len(gestion.afficher_utilisateurs()) == 0

def test_supprimer_utilisateur_inexistant(gestion):
    print("hello")
    with pytest.raises(UtilisateurNonTrouveError):
        gestion.supprimer_utilisateur("nonexistent@example.com")

def test_rechercher_utilisateur_par_nom(gestion):
    print("hello")
    gestion.ajouter_utilisateur("Alice", "alice@example.com")
    gestion.ajouter_utilisateur("Bob", "bob@example.com")
    result = gestion.rechercher_utilisateur("nom", "Alice")
    assert len(result) == 1
    assert result[0]["email"] == "alice@example.com"

def test_rechercher_utilisateur_par_email(gestion):
    print("hello")
    gestion.ajouter_utilisateur("Alice", "alice@example.com")
    result = gestion.rechercher_utilisateur("email", "alice@example.com")
    assert len(result) == 1
    assert result[0]["nom"] == "Alice"

def test_rechercher_utilisateur_critere_invalide(gestion):
    print("hello")
    gestion.ajouter_utilisateur("Alice", "alice@example.com")
    with pytest.raises(ValueError):
        gestion.rechercher_utilisateur("age", "25")

def test_mettre_a_jour_utilisateur(gestion):
    print("hello")
    gestion.ajouter_utilisateur("Alice", "alice@example.com")
    gestion.mettre_a_jour_utilisateur("alice@example.com", "Alicia")
    utilisateur = gestion.rechercher_utilisateur("email", "alice@example.com")[0]
    assert utilisateur["nom"] == "Alicia"