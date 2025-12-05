from app import create_app
from app.extensions import db
from app.models import User, ParkingLot, ParkingSpot, Reservation

app = create_app()

with app.app_context():
    print("Tables detected:")
    print(db.inspect(db.engine).get_table_names())
