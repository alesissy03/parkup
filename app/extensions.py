"""
Extensii globale Flask (DB, LoginManager, etc.)

TODO (Task 2, Task 5):
- Creează instanța SQLAlchemy pentru acces la baza de date.
- Creează instanța LoginManager pentru autentificare.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# TODO (Task 2): instanța SQLAlchemy pentru modele și conexiune la DB
db = SQLAlchemy()

# TODO (Task 5): instanța LoginManager pentru gestionarea sesiunilor de utilizator
login_manager = LoginManager()

# TODO (Task 5): configurează login_manager.login_view și alte mesaje implicite
