from fastapi import FastAPI, HTTPException, Query
from typing import List
import json
from geopy.distance import geodesic

app = FastAPI()


# Load data from the local JSON file on application startup
@app.on_event("startup")
async def startup_event():
    with open("fleets.json", "r") as file:
        data = json.load(file)
    app.ships = data["records"]


# Get ships by country from the loaded data
def get_ships_by_country(country: str):
    # This function should return list of ship's names only(without the other fields)
    # that associated with the given country.
    return [ship['ship']['name'] for ship in app.ships if ship["ship"]["country"] == country]


# Get ships within a specified distance from a given point
def get_ships_by_distance(point: dict, radius_km: float):
    ships_with_distance = []
    for ship in app.ships:
        ship_name = ship["ship"].get("name")  # Use .get() to avoid KeyError if "name" is missing
        if ship_name is not None:  # Check if the ship has a name
            ship_coordinates = ship["position"]["coordinates"][:2]
            distance = geodesic(point.values(), ship_coordinates).kilometers
            if distance <= radius_km:
                ships_with_distance.append({"name": ship_name, "distance_km": distance})
    ships_with_distance.sort(key=lambda x: x["distance_km"])
    return ships_with_distance


# API endpoint to get ships by country
@app.get("/ships/by-country/{country}", response_model=List[str])
async def get_ships_by_country_route(country: str):
    ships = get_ships_by_country(country)
    if not ships:
        raise HTTPException(status_code=404, detail="No ships found for the given country")
    return ships


# API endpoint to get ships by distance from a specified point
@app.get("/ships/by-distance", response_model=List[dict])
async def get_ships_by_distance_route(
    lat: float = Query(..., description="Latitude of the point"),
    lon: float = Query(..., description="Longitude of the point"),
    radius_km: float = Query(..., description="Radius in kilometers")
):
    point = {"lat": lat, "lon": lon}
    ships = get_ships_by_distance(point, radius_km)
    if not ships:
        raise HTTPException(status_code=404, detail="No ships found within the specified radius")

    # In order to Return the modified data structure with 'name' and 'distance_km' keys
    return [{"name": ship["name"], "distance_km": ship["distance_km"]} for ship in ships]
