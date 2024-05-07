
# Test technique

Ce projet est le test technique demandé.

Tout d'abord, il faut clôner le projet : 

```
git clone https://github.com/SurenaHawk/test_axa.git
```

Une fois clôner, allez dans le dossier test_axa : 

```
cd test_axa
```
Ensuite, il faut créer un environnement virtuel dans le projet.
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
Allez dans le dossier axa :

```
cd axa
```

Exécuter la commande suivante pour installer les packages nécesasires pour faire fonctionner le projet : 

```
pip3 install -r requirements.txt
```
Vérifiez que vous êtes au même emplacement que le fichier manage.py et lancer la commande migrate qui permettra de récupérer les tables de la base de données et créera le fichier db.sqlite3 :
```
python3 manage.py migrate
```

Enfin, il suffit de lancer le projet : 
```
python3 manage.py runserver
```
