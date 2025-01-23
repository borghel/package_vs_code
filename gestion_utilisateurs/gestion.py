# filepath: /c:/Users/medihsen/Desktop/package vs code/gestion_utilisateurs/gestion.py
from .exceptions import UtilisateurExistantError, UtilisateurNonTrouveError
from .utils import charger_donnees, sauvegarder_donnees

class GestionUtilisateurs:
    def __init__(self, fichier_donnees=None):
        self.fichier_donnees = fichier_donnees
        self.utilisateurs = charger_donnees(fichier_donnees) if fichier_donnees else []

    def ajouter_utilisateur(self, nom, email):
        if any(u["email"] == email for u in self.utilisateurs):
            raise UtilisateurExistantError(f"L'utilisateur avec l'email {email} existe déjà.")
        self.utilisateurs.append({"nom": nom, "email": email})
        if self.fichier_donnees:
            sauvegarder_donnees(self.fichier_donnees, self.utilisateurs)

    def supprimer_utilisateur(self, email):
        utilisateur = next((u for u in self.utilisateurs if u["email"] == email), None)
        if not utilisateur:
            raise UtilisateurNonTrouveError(f"Aucun utilisateur trouvé avec l'email {email}.")
        self.utilisateurs.remove(utilisateur)
        if self.fichier_donnees:
            sauvegarder_donnees(self.fichier_donnees, self.utilisateurs)

    def afficher_utilisateurs(self):
        return self.utilisateurs

    def rechercher_utilisateur(self, critere, valeur):
        if critere not in ['nom', 'email']:
            raise ValueError("Critère invalide. Utilisez 'nom' ou 'email'.")
        return [u for u in self.utilisateurs if u.get(critere) == valeur]

    def mettre_a_jour_utilisateur(self, email, nouveau_nom):
        utilisateur = next((u for u in self.utilisateurs if u["email"] == email), None)
        if not utilisateur:
            raise UtilisateurNonTrouveError(f"Aucun utilisateur trouvé avec l'email {email}.")
        utilisateur["nom"] = nouveau_nom
        if self.fichier_donnees:
            sauvegarder_donnees(self.fichier_donnees, self.utilisateurs)