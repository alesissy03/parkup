"""
Modelul Reservation.

TODO (Task 2):
- Creează tabela `reservations` cu câmpurile:
    - id (PK)
    - user_id (FK -> users.id)
    - spot_id (FK -> parking_spots.id)
    - start_time
    - end_time
    - status (active/cancelled/finished)
TODO (Task 9):
- Logică pentru creare/anulare rezervări.
TODO (Task 10):
- Query-uri pentru istoricul rezervărilor unui user.
"""

from ..extensions import db

class Reservation(db.Model):
    __tablename__ = "reservations"

    # TODO (Task 2, 9, 10): definește coloanele și relațiile

    def __repr__(self):
        return "<Reservation>"
