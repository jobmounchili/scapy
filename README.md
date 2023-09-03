# Installation et Procédure de déploiement

## Prérequis
Pour installer notre application, il vous faudra :
1. Installer python3
```
$ sudo apt-get install python3
```
2. Un serveur web nginx
```
$ sudo apt-get install nginx
```
3. Un système de gestion de base de données SQLite
```
$ sudo apt-get install sqlite3
```
4. Un gestionnaire de processus Gunicorn pour exécuter l'application Django
```
$ pip3 install gunicorn
```

## Déploiement de l'application
Pour déployer notre application, vous allez :
1. Transférez vos fichiers de code source Django sur le serveur, par exemple, en utilisant SCP, FTP ou Git.
2. Installer les dépendances requises avec la commande:
```
$ sudo pip3 install -r requirements.txt
```
3. Exécuter les migrations de base de données pour configurer la base de données :
```
$ sudo python3 manage.py migrate
```
4. Et collecter les fichiers statiques avec la commande:
```
$ sudo python3 manage.py collectstatic
```

## Exécution de l'application
Utiliser un gestionnaire de processus pour exécuter votre application Django avec Gunicorn : 
```
$ sudo gunicorn mysite.wsgi:application
```
***
### Important
Toujours exécuter l'application en sudo

### Connexion à l'application
Il existe deux types d'utilisateur l'analyste et l'expert
* Utilisateur (expert) paul, Mot de passe : azerty123
* Utilisateur (analyste) jean, Mot de passe : azerty456
