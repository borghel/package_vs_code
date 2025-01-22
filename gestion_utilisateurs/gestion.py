from .exceptions import UtilisateurExistantError, UtilisateurNonTrouveError
from .utils import charger_donnees, sauvegarder_donnees


class GestionUtilisateurs:
    def __init__(self, fichier_donnees=None):
        """
        Initialise la gestion des utilisateurs avec une option de fichier JSON.
        
        :param fichier_donnees: Chemin vers le fichier JSON pour persister les données.
        """
        self.fichier_donnees = fichier_donnees
        self.utilisateurs = charger_donnees(fichier_donnees) if fichier_donnees else []

    def ajouter_utilisateur(self, nom, email):
        """Ajoute un utilisateur s'il n'existe pas déjà."""
        if any(u["email"] == email for u in self.utilisateurs):
            raise UtilisateurExistantError(f"L'utilisateur avec l'email {email} existe déjà.")
        self.utilisateurs.append({"nom": nom, "email": email})
        if self.fichier_donnees:
            sauvegarder_donnees(self.fichier_donnees, self.utilisateurs)

    def supprimer_utilisateur(self, email):
        """Supprime un utilisateur à partir de son email."""
        utilisateur = next((u for u in self.utilisateurs if u["email"] == email), None)
        if not utilisateur:
            raise UtilisateurNonTrouveError(f"Aucun utilisateur trouvé avec l'email {email}.")
        self.utilisateurs.remove(utilisateur)
        if self.fichier_donnees:
            sauvegarder_donnees(self.fichier_donnees, self.utilisateurs)

    def afficher_utilisateurs(self):
        """Affiche tous les utilisateurs."""
        return self.utilisateurs
