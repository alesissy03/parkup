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
    # TODO (Task 9): creează o rezervare pentru un loc
    return {"message": "create_reservation – TODO Task 9"}, 501

@reservation_bp.route("/<int:reservation_id>", methods=["DELETE"])
def cancel_reservation(reservation_id):
    # TODO (Task 9): anulează rezervarea dată
    return {"message": "cancel_reservation – TODO Task 9"}, 501

@reservation_bp.route("/my", methods=["GET"])
def my_reservations():
    # TODO (Task 10): întoarce rezervările user-ului curent
    return {"message": "my_reservations – TODO Task 10"}, 501
