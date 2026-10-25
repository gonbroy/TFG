from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime

from backend.app.algorithms.route_opt import compute_route
from backend.app.db import Base, engine, get_db
import backend.app.models as models

from backend.app.config_logs import setup_logging

logger = setup_logging()

app = FastAPI()

# Crear tablas en el arranque
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- MODELOS DE PETICIÓN --------

class RouteRequest(BaseModel):
    origin: str
    destinations: list[str]


class AirportCreate(BaseModel):
    code: str
    name: str
    city: str
    country: str


class FlightCreate(BaseModel):
    flight_number: str
    origin_airport_id: int
    destination_airport_id: int
    departure_time: datetime
    arrival_time: datetime
    price: float
    airline: str
    available_seats: int


# -------- ENDPOINTS --------

@app.get("/")
def root():
    return {"message": "API funcionando"}

@app.post("/route")
def route(req: RouteRequest, db: Session = Depends(get_db)):
    logger.info(
        "Búsqueda de ruta | origen=%s | destinos=%s",
        req.origin,
        req.destinations,
    )

    try:
        result = compute_route(req.origin, req.destinations, db)

        logger.info(
            "Cálculo de ruta finalizado | origen=%s | destinos=%s",
            req.origin,
            req.destinations,
        )

        return result

    except Exception:
        logger.exception(
            "Error al calcular la ruta | origen=%s | destinos=%s",
            req.origin,
            req.destinations,
        )
        raise

# -------- AEROPUERTOS --------

@app.get("/airports")
def get_airports(db: Session = Depends(get_db)):
    return db.query(models.Airport).all()


@app.post("/airports")
def create_airport(airport: AirportCreate, db: Session = Depends(get_db)):
    new_airport = models.Airport(**airport.dict())
    db.add(new_airport)
    db.commit()
    db.refresh(new_airport)
    return new_airport


# -------- VUELOS --------

@app.get("/flights")
def get_flights(db: Session = Depends(get_db)):
    return db.query(models.Flight).all()


@app.post("/flights")
def create_flight(flight: FlightCreate, db: Session = Depends(get_db)):
    new_flight = models.Flight(**flight.dict())
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    return new_flight
    