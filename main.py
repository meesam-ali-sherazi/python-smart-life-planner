
import json
from models.destination import Destination
from services.trip_planner import TripPlanner

# Destinations JSON se load karna
with open("data/destinations.json", "r", encoding="utf-8") as file:
    data = json.load(file)

destinations = []

for item in data["destinations"]:
    destination = Destination.from_dict(item)
    destinations.append(destination)

# Smart Life Planner start
print("================================")
print("       SMART LIFE PLANNER")
print("================================")

planner = TripPlanner(destinations)
planner.run()


