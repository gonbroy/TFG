from fastapi import FastAPI
from pydantic import BaseModel
from backend.app.algorithms.route_opt import compute_route

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # para desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RouteRequest(BaseModel):
    origin: str
    destinations: list[str]

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}

@app.post("/route")
def route(req: RouteRequest):
    return compute_route(req.origin, req.destinations)
