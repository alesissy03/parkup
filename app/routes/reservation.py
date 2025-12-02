"""
Endpoint-uri pentru rezervări.

TODO (Task 9):
- Creare rezervare (POST /)
- Anulare rezervare (DELETE /<id>)
TODO (Task 10):
- Vizualizare rezervări anterioare pentru user (GET /my)
"""

from flask import Blueprint

reservation_bp = Blueprint("reservation", __name__)

@reservation_bp.route("/", methods=["POST"])
def create_reservation():
    """
    TODO (Task 9): Creează o rezervare pentru un loc de parcare.

    Request JSON:
    {
      "spot_id": 10,
      "start_time": "2025-11-24T10:00:00",
      "end_time": "2025-11-24T12:00:00"
    }

    Răspuns 201 (exemplu):
    {
      "id": 5,
      "user_id": 1,
      "spot_id": 10,
      "start_time": "2025-11-24T10:00:00",
      "end_time": "2025-11-24T12:00:00",
      "status": "active"
    }

    Erori:
    - 400: interval invalid (start >= end etc.)
    - 409: loc deja rezervat / ocupat în interval
    """
    return {"message": "create_reservation – TODO Task 9"}, 501

@reservation_bp.route("/<int:reservation_id>", methods=["DELETE"])
def cancel_reservation(reservation_id):
    """
    TODO (Task 9): Anulează o rezervare existentă.

    Răspuns 200 (exemplu):
    {
      "success": true
    }

    Erori:
    - 404: rezervare inexistentă
    - 403: user-ul nu are dreptul să anuleze această rezervare
    """
    return {"message": "cancel_reservation – TODO Task 9"}, 501

@reservation_bp.route("/my", methods=["GET"])
def my_reservations():
    """
    TODO (Task 10): Returnează rezervările utilizatorului curent (istoric).

    Răspuns 200 (exemplu):
    [
      {
        "id": 5,
        "spot_id": 10,
        "lot_id": 1,
        "start_time": "...",
        "end_time": "...",
        "status": "finished"
      },
      ...
    ]
    """
    return {"message": "my_reservations – TODO Task 10"}, 501
