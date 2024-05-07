
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

Par la suite, il faut faire une migrations pour créer la base de données : 
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Enfin, il suffit de lancer le projet : 
```
python3 manage.py runserver
```
