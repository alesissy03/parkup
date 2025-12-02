"""
Endpoint-uri pentru parcări și locuri de parcare.

TODO (Task 6):
- Obținerea geometriilor (poligoane) pentru parking lots și spots.
TODO (Task 7):
- Vizualizarea locurilor de parcare (returnare date pentru hartă).
TODO (Task 8):
- Filtrare după numele parking lot / număr locuri libere.
"""

from flask import Blueprint

parking_bp = Blueprint("parking", __name__)

@parking_bp.route("/lots", methods=["GET"])
def get_lots():
    # TODO (Task 6, 7, 8): întoarce lista de parcări + info necesar pentru frontend
    return {"message": "get_lots – TODO Task 6/7/8"}, 501

@parking_bp.route("/spots", methods=["GET"])
def get_spots():
    # TODO (Task 6, 7, 8): întoarce lista de locuri (eventual filtrată)
    return {"message": "get_spots – TODO Task 6/7/8"}, 501
