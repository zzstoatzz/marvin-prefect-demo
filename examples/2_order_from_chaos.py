import math as m
import pprint
import marvin
from marvin.settings import temporary_settings
from pydantic import BaseModel

def haversine(lon1, lat1, lon2, lat2) -> float:
    """https://en.wikipedia.org/wiki/Haversine_formula"""
    lon1, lat1, lon2, lat2 = map(m.radians, [lon1, lat1, lon2, lat2])
    dlon, dlat = lon2 - lon1, lat2 - lat1
    a = m.sin(dlat / 2)**2 + m.cos(lat1) * m.cos(lat2) * m.sin(dlon / 2)**2
    return 2 * m.asin(m.sqrt(a)) * 3956  # for miles

class Location(BaseModel):
    name: str
    city: str | None
    state: str | None
    country: str | None
    lat: float
    lon: float

with temporary_settings(
    openai__chat__completions__model="gpt-4-1106-preview",
):
    locations = marvin.extract(
        "started at SFO, then took the BART to 19th street in Oakland",
        Location,
    )

pprint.pprint(locations)

assert len(locations) >= 2

total_distance = sum(
    haversine(locations[i].lon, locations[i].lat, locations[i+1].lon, locations[i+1].lat)
    for i in range(len(locations) - 1)
)

print(f"\nTraveled {total_distance:.2f} miles from {locations[0].name} to {locations[-1].name}")