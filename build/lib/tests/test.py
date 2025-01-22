from gestion_utilisateurs import GestionUtilisateurs

gestion = GestionUtilisateurs("data/utilisateurs.json")
gestion.ajouter_utilisateur("Bob", "bob@example.com")
gestion.afficher_utilisateurs()
