def compute_route(origin: str, destinations: list[str]):
    return {
        "route": [origin] + destinations,
        "estimated_cost": 123,
        "note": "MVP: ruta sin optimización todavía"
    }
