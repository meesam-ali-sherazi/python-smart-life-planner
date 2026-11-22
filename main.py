
import json
from models.destination import Destination
from services.trip_calculator import TripCostCalculator

# Destinations load karna
with open("data/destinations.json", "r", encoding="utf-8") as file:
    data = json.load(file)

destinations = []

for item in data["destinations"]:
    destination = Destination.from_dict(item)
    destinations.append(destination)

print("SMART LIFE PLANNER")
print("------------------")
print("Total destinations:", len(destinations))

for destination in destinations:
    print(destination.name)

# Trip cost calculator test
calculator = TripCostCalculator()

selected_destination = destinations[0]

result = calculator.calculate_trip_cost(
    selected_destination,
    travellers=4,
    days=3,
    nights=2
)

print("\nTRIP COST REPORT")
print("------------------")
print("Destination:", selected_destination.name)
print("Travellers: 4")
print("Days: 3")
print("Nights: 2")
print("Transport: Rs.", result["transport"])
print("Hotel rooms:", result["rooms"])
print("Accommodation: Rs.", result["accommodation"])
print("Food: Rs.", result["food"])
print("Activities: Rs.", result["activities"])
print("Emergency: Rs.", result["emergency"])
print("Total Cost: Rs.", result["total"])
print("Per Person: Rs.", result["per_person"])

