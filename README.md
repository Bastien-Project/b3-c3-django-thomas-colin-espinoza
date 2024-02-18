# Password Manager
Créez une application web de carnet d'adresses. Les utilisateurs pourront s'inscrire, se connecter, et ajouter, éditer et supprimer des contacts.

## Fonctionnalités Attendues
- Liste des sites : Affichez tous les sites. Chaque site doit avoir un nom, une URL, un identifiant et un mot de passe
- Ajout de sites : Permettez aux utilisateurs d'ajouter de nouveau site avec un formulaire.
- Modification de site
suppression de site : Permettez aux utilisateurs de modifier et de supprimer leurs propres sites.
- Interface utilisateur conviviale : Créez une interface utilisateur simple et intuitive à l'aide de templates Django.
- Exporter ses mots de passe au format csv
- Importer des mots de passe au format csv

## Bonus :
- Authentification des utilisateurs : Permettez aux utilisateurs de s'inscrire, de se connecter et de se déconnecter. (Fait)
- Cryptage du mot de passe (Fait)
- Génération de mots de passe aléatoires
- Dark mode (Fait)

## Ressenti du groupe sur le projet
Le projet est bien et il nous a permis d'apprendre un nouveau framework de python. Cependant, ce n'est pas évident en bossant à plusieurs en même temps et de bien répartir le travail quand on ne connaît pas la techno vu que Django est nouveau pour nous. 
Du coup, on a plutôt travailler en faisant du pair programming.
En revanche, par complexité et manque de connaissance, nous n'avons pas réussi à faire la partie avec les CSV.

## Commandes Utiles
Création et application des migrations :
```sh
python manage.py makemigrations
python manage.py migrate
```
Création d'un "super utilisateur" :
 ```sh
python manage.py createsuperuser
```
Lancer le projet :
```sh
python manage.py runserver
```