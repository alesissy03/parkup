"""
Modelul ParkingLot.

TODO (Task 2):
- Creează tabela `parking_lots` cu câmpurile:
    - id (PK)
    - name
    - campus_zone
    - lat_center
    - lng_center
    - total_spots
    - polygon_geojson (TEXT, opțional)
TODO (Task 6):
- Adaugă relația cu ParkingSpot (one-to-many).
"""

from ..extensions import db

class ParkingLot(db.Model):
    __tablename__ = "parking_lots"

    # TODO (Task 2): definește coloanele conform documentației
    # TODO (Task 6): definește relația `spots` = db.relationship("ParkingSpot", ...)

    def __repr__(self):
        return "<ParkingLot>"
