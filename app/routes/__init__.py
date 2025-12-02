"""
Pachetul routes gestionează toate Blueprint-urile API.

TODO (Task 4):
- Importă blueprint-urile individuale.
- Expune o funcție register_blueprints(app) care le înregistrează cu prefix-uri corecte.
"""

from .auth import auth_bp
from .parking import parking_bp
from .reservation import reservation_bp
from .admin import admin_bp

def register_blueprints(app):
    """
    TODO (Task 4):
    - Înregistrează blueprint-urile:
        - auth_bp la /api/auth
        - parking_bp la /api/parking
        - reservation_bp la /api/reservations
        - admin_bp la /api/admin
    """
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(parking_bp, url_prefix="/api/parking")
    app.register_blueprint(reservation_bp, url_prefix="/api/reservations")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
