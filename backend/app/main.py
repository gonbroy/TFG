from fastapi import FastAPI
from pydantic import BaseModel
from backend.app.algorithms.route_opt import compute_route

app = FastAPI()

class RouteRequest(BaseModel):
    origin: str
    destinations: list[str]

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}

@app.post("/route")
def route(req: RouteRequest):
    return compute_route(req.origin, req.destinations)
