from datetime import datetime
from app.db import SessionLocal
from app import models


def seed_airports():
    db = SessionLocal()

    print("Entrando en la función seed_airports()...")

    if db.query(models.Airport).count() > 0:
        print("⚠️ Aeropuertos ya existen, no se insertan")
        db.close()
        return

    airports = [
        models.Airport(code="SVQ", name="Aeropuerto de Sevilla", city="Sevilla", country="España"),
        models.Airport(code="MAD", name="Aeropuerto de Madrid", city="Madrid", country="España"),
        models.Airport(code="BCN", name="Aeropuerto de Barcelona", city="Barcelona", country="España"),
    ]

    db.add_all(airports)
    db.commit()
    db.close()

    print("✅ Aeropuertos insertados correctamente")


def seed_flights():
    db = SessionLocal()

    print("Entrando en la función seed_flights()...")

    if db.query(models.Flight).count() > 0:
        print("⚠️ Vuelos ya existen, no se insertan")
        db.close()
        return

    svq = db.query(models.Airport).filter_by(code="SVQ").first()
    mad = db.query(models.Airport).filter_by(code="MAD").first()
    bcn = db.query(models.Airport).filter_by(code="BCN").first()

    if not svq or not mad or not bcn:
        print("❌ Faltan aeropuertos en la base de datos")
        db.close()
        return

    flights = [
        # =========================
        # SVQ -> MAD (mismo día, varios precios)
        # =========================
        models.Flight(
            flight_number="IB101",
            origin_airport_id=svq.id,
            destination_airport_id=mad.id,
            departure_time=datetime(2026, 4, 1, 8, 0, 0),
            arrival_time=datetime(2026, 4, 1, 9, 30, 0),
            price=100.0,
            airline="Iberia",
            available_seats=50
        ),
        models.Flight(
            flight_number="IB102",
            origin_airport_id=svq.id,
            destination_airport_id=mad.id,
            departure_time=datetime(2026, 4, 1, 14, 0, 0),
            arrival_time=datetime(2026, 4, 1, 15, 30, 0),
            price=150.0,
            airline="Iberia",
            available_seats=45
        ),
        models.Flight(
            flight_number="IB103",
            origin_airport_id=svq.id,
            destination_airport_id=mad.id,
            departure_time=datetime(2026, 4, 1, 20, 0, 0),
            arrival_time=datetime(2026, 4, 1, 21, 30, 0),
            price=120.0,
            airline="Iberia",
            available_seats=40
        ),

        # =========================
        # SVQ -> BCN (mismo día, varios precios)
        # =========================
        models.Flight(
            flight_number="IB201",
            origin_airport_id=svq.id,
            destination_airport_id=bcn.id,
            departure_time=datetime(2026, 4, 1, 7, 30, 0),
            arrival_time=datetime(2026, 4, 1, 9, 0, 0),
            price=110.0,
            airline="Iberia",
            available_seats=50
        ),
        models.Flight(
            flight_number="IB202",
            origin_airport_id=svq.id,
            destination_airport_id=bcn.id,
            departure_time=datetime(2026, 4, 1, 13, 30, 0),
            arrival_time=datetime(2026, 4, 1, 15, 0, 0),
            price=130.0,
            airline="Iberia",
            available_seats=45
        ),
        models.Flight(
            flight_number="IB203",
            origin_airport_id=svq.id,
            destination_airport_id=bcn.id,
            departure_time=datetime(2026, 4, 1, 19, 0, 0),
            arrival_time=datetime(2026, 4, 1, 20, 30, 0),
            price=105.0,
            airline="Iberia",
            available_seats=42
        ),

        # =========================
        # MAD -> BCN (mismo día, varios precios)
        # =========================
        models.Flight(
            flight_number="VY301",
            origin_airport_id=mad.id,
            destination_airport_id=bcn.id,
            departure_time=datetime(2026, 4, 3, 8, 0, 0),
            arrival_time=datetime(2026, 4, 3, 9, 30, 0),
            price=80.0,
            airline="Vueling",
            available_seats=60
        ),
        models.Flight(
            flight_number="VY302",
            origin_airport_id=mad.id,
            destination_airport_id=bcn.id,
            departure_time=datetime(2026, 4, 3, 12, 0, 0),
            arrival_time=datetime(2026, 4, 3, 13, 30, 0),
            price=70.0,
            airline="Vueling",
            available_seats=55
        ),
        models.Flight(
            flight_number="VY303",
            origin_airport_id=mad.id,
            destination_airport_id=bcn.id,
            departure_time=datetime(2026, 4, 3, 18, 0, 0),
            arrival_time=datetime(2026, 4, 3, 19, 30, 0),
            price=75.0,
            airline="Vueling",
            available_seats=58
        ),

        # =========================
        # BCN -> MAD (mismo día, varios precios)
        # =========================
        models.Flight(
            flight_number="FR401",
            origin_airport_id=bcn.id,
            destination_airport_id=mad.id,
            departure_time=datetime(2026, 4, 5, 8, 0, 0),
            arrival_time=datetime(2026, 4, 5, 9, 30, 0),
            price=85.0,
            airline="Ryanair",
            available_seats=70
        ),
        models.Flight(
            flight_number="FR402",
            origin_airport_id=bcn.id,
            destination_airport_id=mad.id,
            departure_time=datetime(2026, 4, 5, 14, 0, 0),
            arrival_time=datetime(2026, 4, 5, 15, 30, 0),
            price=80.0,
            airline="Ryanair",
            available_seats=65
        ),
        models.Flight(
            flight_number="FR403",
            origin_airport_id=bcn.id,
            destination_airport_id=mad.id,
            departure_time=datetime(2026, 4, 5, 20, 0, 0),
            arrival_time=datetime(2026, 4, 5, 21, 30, 0),
            price=95.0,
            airline="Ryanair",
            available_seats=60
        ),

        # =========================
        # MAD -> SVQ (mismo día, varios precios)
        # =========================
        models.Flight(
            flight_number="VY501",
            origin_airport_id=mad.id,
            destination_airport_id=svq.id,
            departure_time=datetime(2026, 4, 6, 8, 0, 0),
            arrival_time=datetime(2026, 4, 6, 9, 30, 0),
            price=165.0,
            airline="Vueling",
            available_seats=60
        ),
        models.Flight(
            flight_number="VY502",
            origin_airport_id=mad.id,
            destination_airport_id=svq.id,
            departure_time=datetime(2026, 4, 6, 13, 0, 0),
            arrival_time=datetime(2026, 4, 6, 14, 30, 0),
            price=160.0,
            airline="Vueling",
            available_seats=58
        ),
        models.Flight(
            flight_number="VY503",
            origin_airport_id=mad.id,
            destination_airport_id=svq.id,
            departure_time=datetime(2026, 4, 6, 19, 0, 0),
            arrival_time=datetime(2026, 4, 6, 20, 30, 0),
            price=168.0,
            airline="Vueling",
            available_seats=55
        ),

        # =========================
        # BCN -> SVQ (mismo día, varios precios)
        # =========================
        models.Flight(
            flight_number="FR601",
            origin_airport_id=bcn.id,
            destination_airport_id=svq.id,
            departure_time=datetime(2026, 4, 6, 9, 0, 0),
            arrival_time=datetime(2026, 4, 6, 10, 40, 0),
            price=90.0,
            airline="Ryanair",
            available_seats=70
        ),
        models.Flight(
            flight_number="FR602",
            origin_airport_id=bcn.id,
            destination_airport_id=svq.id,
            departure_time=datetime(2026, 4, 6, 15, 0, 0),
            arrival_time=datetime(2026, 4, 6, 16, 40, 0),
            price=85.0,
            airline="Ryanair",
            available_seats=68
        ),
        models.Flight(
            flight_number="FR603",
            origin_airport_id=bcn.id,
            destination_airport_id=svq.id,
            departure_time=datetime(2026, 4, 6, 21, 0, 0),
            arrival_time=datetime(2026, 4, 6, 22, 40, 0),
            price=95.0,
            airline="Ryanair",
            available_seats=64
        ),
    ]

    db.add_all(flights)
    db.commit()
    db.close()

    print("✅ Vuelos insertados correctamente")


if __name__ == "__main__":
    seed_airports()
    seed_flights()