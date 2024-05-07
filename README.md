
# Test technique

Ce projet est le test technique demandé.

Tout d'abord, il faut clôner le projet : 

```
git clone https://github.com/SurenaHawk/test_axa.git
```
Une fois ouvert, il faut créer un environnement virtuel dans le projet.
Lancer la commande pour installer virtualenv avec pip.

```
pip3 install virtualenv 
```
Une fois installé, il faut créer l'environnement : 
```
virtualenv venv
```
Enfin, une fois la création terminé, on peut utiliser l'environnement virtuel : 
```
source venv/bin/activate
```
Aller dans le dossier axa et executer la commande suivante pour installer les packages nécesasires pour faire fonctionner le projet : 
```
pip3 install -r requirements.txt
```
Il y a dans la base de données déjà une donnée. Vous pouvez lancer le projet directement avec la commande :
```
python3 manage.py runserver
```
Si vous ne souhaitez pas utiliser la base de données initiale, supprimez le fichier db.sqlite3 et faites les commandes suivantes : 

Il faut faire une migrations pour récupérer les tables pour la base de données : 
```
python3 manage.py migrate
```

Enfin, il suffit de lancer le projet : 
```
python3 manage.py runserver
```
