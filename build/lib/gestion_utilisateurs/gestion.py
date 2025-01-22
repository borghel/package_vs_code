from gestion_utilisateurs.exceptions import UtilisateurExistantError, UtilisateurNonTrouveError

class GestionUtilisateurs:
    # Méthodes existantes...

    def ajouter_utilisateur(self, nom, email):
        if any(u["email"] == email for u in self.utilisateurs):
            raise UtilisateurExistantError(f"L'utilisateur avec l'email {email} existe déjà.")
        self.utilisateurs.append({"nom": nom, "email": email})

    def supprimer_utilisateur(self, email):
        utilisateur = next((u for u in self.utilisateurs if u["email"] == email), None)
        if not utilisateur:
            raise UtilisateurNonTrouveError(f"Aucun utilisateur trouvé avec l'email {email}.")
        self.utilisateurs.remove(utilisateur)
