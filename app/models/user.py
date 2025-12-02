"""
Modelul User.

TODO (Task 2):
- Creează tabela `users` cu câmpurile:
    - id: INTEGER, PK, auto-increment
    - email: VARCHAR, unic, not null
    - password_hash: VARCHAR, not null (parola hash-uită, nu în clar)
    - full_name: VARCHAR
    - role: VARCHAR (ex: 'student', 'staff', 'admin')
    - created_at: DATETIME (data creării contului)

TODO (Task 5):
- Integrare cu Flask-Login (UserMixin).
- Metode:
    - set_password(self, raw_password): setează password_hash
    - check_password(self, raw_password): verifică parola primită.
"""

from ..extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"

    # TODO (Task 2): definește coloanele (id, email, password_hash, full_name, role, created_at)

    # TODO (Task 5): metode set_password(self, raw_password) și check_password(self, raw_password)

    def __repr__(self):
        # TODO (Task 2): întoarce un string util pentru debugging
        return "<User id=? email=?>"
