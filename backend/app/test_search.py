from app.db import SessionLocal
from app import models
from itertools import permutations


def cheapest_flight_per_day(flights):
    mejores = {}

    for flight in flights:
        origin_code = flight.origin_airport.code
        destination_code = flight.destination_airport.code
        departure_date = flight.departure_time.date().isoformat()

        clave = (origin_code, destination_code, departure_date)

        if clave not in mejores:
            mejores[clave] = flight
        else:
            if flight.price < mejores[clave].price:
                mejores[clave] = flight

    return list(mejores.values())

def build_flight_map(flights):
    flight_map = {}

    for flight in flights:
        key = (flight.origin_airport.code, flight.destination_airport.code)
        flight_map[key] = flight

    return flight_map


db = SessionLocal()

try:
    flights = db.query(models.Flight).all()

    print(f"Vuelos antes del filtro: {len(flights)}")

    best_daily_flights = cheapest_flight_per_day(flights)

    print(f"Vuelos después del filtro: {len(best_daily_flights)}")
    print()

    for flight in best_daily_flights:
        print(
            f"{flight.origin_airport.code} -> {flight.destination_airport.code} | "
            f"{flight.departure_time.date()} | "
            f"{flight.flight_number} | "
            f"{flight.price}€"
        )

    flight_map = build_flight_map(best_daily_flights)

    origin = "SVQ"
    destinations = ["MAD", "BCN"]

    best_route = None
    best_cost = float("inf")

    for order in permutations(destinations):
        route = [origin] + list(order) + [origin]

        total_cost = 0
        valid = True
        selected_flights = []

        for i in range(len(route) - 1):
            tramo = (route[i], route[i + 1])

            if tramo not in flight_map:
                valid = False
                break

            flight = flight_map[tramo]
            total_cost += flight.price
            selected_flights.append(flight)

        if valid and total_cost < best_cost:
            best_cost = total_cost
            best_route = (route, selected_flights)

    if best_route:
        print("\nMejor ruta encontrada:")
        print(" -> ".join(best_route[0]))
        print(f"Coste total: {best_cost}€")

        print("\nVuelos elegidos:")
        for flight in best_route[1]:
            print(
                f"{flight.origin_airport.code} -> {flight.destination_airport.code} | "
                f"{flight.flight_number} | {flight.price}€"
            )
    else:
        print("No se encontró ninguna ruta válida")

finally:
    db.close()