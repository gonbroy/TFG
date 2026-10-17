from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, func
from sqlalchemy.orm import relationship

from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Airport(Base):
    __tablename__ = "airports"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)   # MAD, BCN, CDG...
    name = Column(String, nullable=False)                            # Nombre del aeropuerto
    city = Column(String, nullable=False)                            # Ciudad
    country = Column(String, nullable=False)                         # País

    # Relaciones
    departures = relationship(
        "Flight",
        back_populates="origin_airport",
        foreign_keys="Flight.origin_airport_id"
    )
    arrivals = relationship(
        "Flight",
        back_populates="destination_airport",
        foreign_keys="Flight.destination_airport_id"
    )


class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, unique=True, index=True, nullable=False)  # IB123, VY456...

    origin_airport_id = Column(Integer, ForeignKey("airports.id"), nullable=False)
    destination_airport_id = Column(Integer, ForeignKey("airports.id"), nullable=False)

    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)

    price = Column(Float, nullable=False)
    airline = Column(String, nullable=False)
    available_seats = Column(Integer, nullable=False, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relaciones
    origin_airport = relationship(
        "Airport",
        foreign_keys=[origin_airport_id],
        back_populates="departures"
    )
    destination_airport = relationship(
        "Airport",
        foreign_keys=[destination_airport_id],
        back_populates="arrivals"
    )