"""
Endpoint-uri pentru administrator.

TODO (Task 6):
- Salvare/actualizare poligoane (Leaflet.draw) pentru lots/spots.
TODO (Task 11):
- Vizualizare statistici: număr locuri libere/ocupate, număr rezervări etc.
"""

from flask import Blueprint

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/polygons", methods=["POST"])
def save_polygons():
    # TODO (Task 6): primește GeoJSON și salvează geometria în DB
    return {"message": "save_polygons – TODO Task 6"}, 501

@admin_bp.route("/stats", methods=["GET"])
def stats():
    # TODO (Task 11): calculează și întoarce statistici pentru admin
    return {"message": "stats – TODO Task 11"}, 501
