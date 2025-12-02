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
    """
    TODO (Task 6): Salvează / actualizează poligoanele (GeoJSON) pentru lots/spots.

    Request JSON (exemple posibile):
    {
      "lots": [ { "id": 1, "polygon_geojson": { ... } }, ... ],
      "spots": [ { "id": 10, "polygon_geojson": { ... } }, ... ]
    }

    Răspuns 200:
    {
      "success": true
    }

    Erori:
    - 400: format JSON invalid
    - 403: user-ul nu este admin
    """
    return {"message": "save_polygons – TODO Task 6"}, 501

@admin_bp.route("/stats", methods=["GET"])
def stats():
    """
    TODO (Task 11): Statistici pentru admin.

    Răspuns 200 (exemplu):
    {
      "total_spots": 120,
      "free_spots": 40,
      "occupied_spots": 60,
      "reserved_spots": 15,
      "out_of_service_spots": 5,
      "active_reservations": 10,
      "finished_reservations": 120,
      "cancelled_reservations": 8
    }
    """
    return {"message": "stats – TODO Task 11"}, 501
