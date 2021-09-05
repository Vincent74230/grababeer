# GRABABEER APP

## Comment l'installer sur votre machine:

I - Cloner le projet depuis le repo github:
- `git clone git@github.com:Vincent74230/grababeer.git`

II - Installer un environnement de développement à la racine du projet avec virtualenv
- Dans la console, taper la commande `virtualenv -p python3 env`
- Activer l'environnement `source env/bin/activate`
- Installer les dépendances : `pip3 install -r requirements.txt`

III - Créer une base de données PostgreSQL:
- Entrer dans l'invite de commande Postgres : `sudo su postgres`
- Une fois dans l'invite taper : `psql`
- Créer l'utilisateur : `CREATE USER beer_user WITH PASSWORD 'password';`
- Créer la base de données : `CREATE DATABASE grababeer WITH OWNER beer_user ENCODING 'UTF-8;`
- Donner toutes les autorisation à beer_user sur grababeer : `GRANT ALL PRIVILEGES ON DATABASE grababeer to beer_user;`
- Permettre à beer_user de créer des bases de données (pour les tests automatisés):`ALTER USER beer_user CREATEDB`

IV - Lancer l'application:
- Se placer à la racine du projet (au niveau du 'manage.py')
- Lancer la commande `python manage.py runserver`
- Ctrl-click sur le lien qui s'affiche dans la console.