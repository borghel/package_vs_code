## Fonctionnalités

### Rechercher un utilisateur
La méthode `rechercher_utilisateur` permet de chercher un utilisateur par son **nom** ou son **email** :

#### Exemple :
```python
from gestion_utilisateurs.gestion import GestionUtilisateurs

gestion = GestionUtilisateurs()
gestion.ajouter_utilisateur("Alice", "alice@example.com")
gestion.ajouter_utilisateur("Bob", "bob@example.com")

# Rechercher par nom
resultat_nom = gestion.rechercher_utilisateur("nom", "Alice")
print(resultat_nom)  # [{'nom': 'Alice', 'email': 'alice@example.com'}]

# Rechercher par email
resultat_email = gestion.rechercher_utilisateur("email", "bob@example.com")
print(resultat_email)  # [{'nom': 'Bob', 'email': 'bob@example.com'}]
