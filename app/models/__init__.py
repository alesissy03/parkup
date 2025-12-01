# TODO: importă și expune toate modelele SQLAlchemy,
# ca să poți face from app.models import User, ParkingLot, ParkingSpot, Reservation

from .user import User
from .parking_lot import ParkingLot
from .parking_spot import ParkingSpot
from .reservation import Reservation

# (opțional) listă de export explicită
__all__ = ["User", "ParkingLot", "ParkingSpot", "Reservation"]
