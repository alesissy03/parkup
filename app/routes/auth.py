"""
Endpoint-uri de autentificare și înregistrare.

TODO (Task 5):
- Implementare POST /register
- Implementare POST /login
- (opțional) POST /logout
"""

from flask import Blueprint

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    """
    TODO (Task 5): Înregistrare utilizator nou.

    Request JSON:
    {
      "email": "user@example.com",
      "password": "plaintext-password",
      "full_name": "Nume Prenume",
      "role": "student" | "staff" | "admin" (opțional, default 'student')
    }

    Răspuns 201 (exemplu):
    {
      "id": 1,
      "email": "user@example.com",
      "full_name": "Nume Prenume",
      "role": "student"
    }

    Erori posibile:
    - 400: date lipsă sau invalide
    - 409: email deja folosit

    Format erori (vezi docs/api/errors.md):
    {
      "error": "EMAIL_TAKEN",
      "message": "Adresa de email este deja folosită."
    }
    """
    return {"message": "register – TODO Task 5"}, 501

@auth_bp.route("/login", methods=["POST"])
def login():
    """
    TODO (Task 5): Autentificare utilizator.

    Request JSON:
    {
      "email": "user@example.com",
      "password": "plaintext-password"
    }

    Răspuns 200 (exemplu):
    {
      "id": 1,
      "email": "user@example.com",
      "full_name": "Nume Prenume",
      "role": "student"
      // (opțional) token, dacă decizi să folosești autentificare bazată pe token
    }

    Erori posibile:
    - 400: date lipsă
    - 401: email/parolă incorecte
    """
    return {"message": "login – TODO Task 5"}, 501
