from itertools import permutations
from typing import List, Dict
from sqlalchemy.orm import Session

import backend.app.models as models


def get_cheapest_flight(db: Session, origin_code: str, destination_code: str):
    flights = db.query(models.Flight).all()

    valid_flights = []
    for flight in flights:
        if (
            flight.origin_airport.code == origin_code
            and flight.destination_airport.code == destination_code
        ):
            valid_flights.append(flight)

    if not valid_flights:
        return None

    cheapest = min(valid_flights, key=lambda f: f.price)
    return cheapest


def compute_route(origin: str, destinations: List[str], db: Session) -> Dict:
    results = []

    for perm in permutations(destinations):
        route = [origin] + list(perm)

        total_cost = 0
        valid_route = True
        flight_details = []

        for i in range(len(route) - 1):
            tramo_origen = route[i]
            tramo_destino = route[i + 1]

            cheapest_flight = get_cheapest_flight(db, tramo_origen, tramo_destino)

            if cheapest_flight is None:
                valid_route = False
                break

            total_cost += cheapest_flight.price

            flight_details.append({
                "from": tramo_origen,
                "to": tramo_destino,
                "flight_number": cheapest_flight.flight_number,
                "price": cheapest_flight.price,
                "airline": cheapest_flight.airline,
                "departure_time": str(cheapest_flight.departure_time),
                "arrival_time": str(cheapest_flight.arrival_time),
            })

        if valid_route:
            results.append({
                "route": route,
                "estimated_cost": total_cost,
                "note": "Ruta calculada con vuelos de la BD",
                "flights": flight_details
            })

    results.sort(key=lambda x: x["estimated_cost"])

    return {
        "results": results
    }