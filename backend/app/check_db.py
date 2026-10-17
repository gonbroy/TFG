from app.db import SessionLocal
from app import models

db = SessionLocal()

print("📊 CONTENIDO DE LA BASE DE DATOS\n")

# AIRPORTS
airports = db.query(models.Airport).all()
print(f"Aeropuertos ({len(airports)}):")
for a in airports:
    print(a.__dict__)
print()

# FLIGHTS
flights = db.query(models.Flight).all()
print(f"Vuelos ({len(flights)}):")
for f in flights:
    print(f.__dict__)
print()

# USERS (opcional)
users = db.query(models.User).all()
print(f"Usuarios ({len(users)}):")
for u in users:
    print(u.__dict__)

db.close()