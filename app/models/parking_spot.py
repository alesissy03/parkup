"""
Modelul ParkingSpot.

TODO (Task 2):
- Creează tabela `parking_spots` cu câmpurile:
    - id (PK)
    - lot_id (FK -> parking_lots.id)
    - spot_number
    - type
    - current_status
    - last_status_change
    - polygon_geojson
TODO (Task 6):
- Relația cu ParkingLot (many-to-one).
TODO (Task 9):
- Relația cu Reservation (one-to-many).
"""

from ..extensions import db

class ParkingSpot(db.Model):
    __tablename__ = "parking_spots"

    # TODO (Task 2, 6, 9): definește coloanele și relațiile

    def __repr__(self):
        return "<ParkingSpot>"
