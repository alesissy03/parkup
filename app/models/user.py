"""
Modelul User.

TODO (Task 2):
- Creează tabela `users` cu câmpurile:
    - id (PK)
    - email (unic)
    - password_hash
    - full_name
    - role (student/staff/admin)
    - created_at (datetime)
TODO (Task 5):
- Adaugă metode pentru setarea/verificarea parolei.
- Integrează cu Flask-Login (UserMixin).
"""

from ..extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"

    # TODO (Task 2): definește coloanele (id, email, password_hash, full_name, role, created_at)

    # TODO (Task 5): metode set_password(self, raw_password) și check_password(self, raw_password)

    def __repr__(self):
        # TODO (Task 2): întoarce un string util pentru debugging
        return "<User>"
