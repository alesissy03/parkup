# TODO: importă Blueprints-urile și expune o funcție register_blueprints(app)
# care să fie apelată în create_app (app/__init__.py).

from .auth import auth_bp
from .parking import parking_bp
from .reservation import reservation_bp
from .admin import admin_bp

def register_blueprints(app):
    """Înregistrează toate Blueprints-urile pe aplicația Flask."""
    # TODO: ajustează prefixurile URL după nevoie
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(parking_bp, url_prefix="/api/parking")
    app.register_blueprint(reservation_bp, url_prefix="/api/reservations")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
