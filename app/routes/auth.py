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
    # TODO (Task 5): primește date user, validează, creează utilizator nou
    return {"message": "register – TODO Task 5"}, 501

@auth_bp.route("/login", methods=["POST"])
def login():
    # TODO (Task 5): verifică credențiale, setează sesiune/token
    return {"message": "login – TODO Task 5"}, 501
