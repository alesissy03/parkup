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
    """
    TODO (Task 6, 7, 8): Returnează lista de parcări (parking lots).

    Query params (opțional, Task 8):
    - name: filtrare după numele parcării (parțial)
    - campus_zone: filtrare după zonă (Nord, Sud etc.)

    Răspuns 200 (exemplu):
    [
      {
        "id": 1,
        "name": "Parcare Cămin A",
        "campus_zone": "Nord",
        "lat_center": 44.435,
        "lng_center": 26.05,
        "total_spots": 50,
        "polygon_geojson": { ... } // obiect JSON
      },
      ...
    ]

    Erori posibile:
    - 500: eroare internă (ex: DB)
    """
    return {"message": "get_lots – TODO Task 6/7/8"}, 501

@parking_bp.route("/spots", methods=["GET"])
def get_spots():
    """
    TODO (Task 6, 7, 8): Returnează lista de locuri de parcare (parking spots).

    Query params (Task 8):
    - lot_id: doar locurile dintr-o anumită parcare
    - status: 'free' | 'occupied' | 'reserved' | 'out_of_service'
    - type: 'student' | 'staff' | 'disabled' | 'visitor'

    Răspuns 200 (exemplu):
    [
      {
        "id": 10,
        "lot_id": 1,
        "spot_number": "A12",
        "type": "student",
        "current_status": "free",
        "last_status_change": "2025-11-24T10:15:32",
        "polygon_geojson": { ... }
      },
      ...
    ]
    """
    return {"message": "get_spots – TODO Task 6/7/8"}, 501
