"""
Modelul ParkingSpot.

TODO (Task 2):
- Creează tabela `parking_spots` cu câmpurile:
    - id: INTEGER, PK, auto-increment
    - lot_id: INTEGER, FK -> parking_lots.id
    - spot_number: VARCHAR / INTEGER (ex: 1, 2, "A23")
    - type: VARCHAR (ex: 'student', 'staff', 'disabled', 'visitor')
    - current_status: VARCHAR (ex: 'free', 'occupied', 'reserved', 'out_of_service')
    - last_status_change: DATETIME (ultima schimbare de status)
    - polygon_geojson: TEXT (geometria locului în format GeoJSON)

TODO (Task 6):
- Relația many-to-one cu ParkingLot (parking_spot.lot).

TODO (Task 9):
- Relația one-to-many cu Reservation (spot.reservations).
"""

from ..extensions import db

class ParkingSpot(db.Model):
    __tablename__ = "parking_spots"

    # TODO (Task 2, 6, 9): definește coloanele și relațiile

    def __repr__(self):
        return "<ParkingSpot id=? lot_id=? spot_number=?>"