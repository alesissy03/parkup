"""
Modelul Reservation.

TODO (Task 2):
- Creează tabela `reservations` cu câmpurile:
    - id: INTEGER, PK, auto-increment
    - user_id: INTEGER, FK -> users.id
    - spot_id: INTEGER, FK -> parking_spots.id
    - start_time: DATETIME (începutul rezervării)
    - end_time: DATETIME (sfârșitul rezervării)
    - status: VARCHAR (ex: 'active', 'cancelled', 'finished')

TODO (Task 9):
- Logica pentru creare/anulare rezervări + validări (interval valid, disponibilitate spot).

TODO (Task 10):
- Query-uri pentru istoricul rezervărilor unui user.
"""

from ..extensions import db

class Reservation(db.Model):
    __tablename__ = "reservations"

    # TODO (Task 2, 9, 10): definește coloanele și relațiile

    def __repr__(self):
        return "<Reservation id=? user_id=? spot_id=?>"
