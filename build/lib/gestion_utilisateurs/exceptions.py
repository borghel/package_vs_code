class GestionUtilisateursError(Exception):
    """Classe de base pour les exceptions du package."""

class UtilisateurExistantError(GestionUtilisateursError):
    """Erreur levée lorsqu'un utilisateur existe déjà."""

class UtilisateurNonTrouveError(GestionUtilisateursError):
    """Erreur levée lorsqu'un utilisateur n'est pas trouvé."""
