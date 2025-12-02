"""
Modelul ParkingLot.

TODO (Task 2):
- Creează tabela `parking_lots` cu câmpurile:
    - id: INTEGER, PK, auto-increment
    - name: VARCHAR (ex: "Parcare Cămin A"), not null
    - campus_zone: VARCHAR (ex: "Nord", "Sud"), opțional
    - lat_center: FLOAT (latitudinea centrului parcării)
    - lng_center: FLOAT (longitudinea centrului parcării)
    - total_spots: INTEGER (numărul total de locuri)
    - polygon_geojson: TEXT (geometria parcării în format GeoJSON, opțional)

TODO (Task 6):
- Relația one-to-many cu ParkingSpot:
    - lots.spots -> listă de locuri aparținând parcării.
"""

from ..extensions import db

class ParkingLot(db.Model):
    __tablename__ = "parking_lots"

    # TODO (Task 2): definește coloanele conform documentației
    # TODO (Task 6): definește relația `spots` = db.relationship("ParkingSpot", ...)

    def __repr__(self):
        return "<ParkingLot id=? name=?>"
