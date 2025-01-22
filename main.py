from gestion_utilisateurs.gestion import GestionUtilisateurs

def menu():
    print("\n--- Menu ---")
    print("1. Ajouter un utilisateur")
    print("2. Supprimer un utilisateur")
    print("3. Modifier un utilisateur")
    print("4. Afficher les utilisateurs")
    print("5. Quitter")
    choix = input("Choisissez une option : ")
    return choix

def main():
    gestion = GestionUtilisateurs("data/utilisateurs.json")

    while True:
        choix = menu()
        if choix == "1":
            nom = input("Nom : ")
            email = input("Email : ")
            gestion.ajouter_utilisateur(nom, email)
        elif choix == "2":
            email = input("Email à supprimer : ")
            gestion.supprimer_utilisateur(email)
        elif choix == "3":
            email = input("Email de l'utilisateur à modifier : ")
            nouveau_nom = input("Nouveau nom : ")
            gestion.modifier_utilisateur(email, nouveau_nom)
        elif choix == "4":
            gestion.afficher_utilisateurs()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
