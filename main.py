
import json
from models.destination import Destination

# JSON file open karna
with open("data/destinations.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# JSON data ko Destination objects mein convert karna
destinations = []

for item in data["destinations"]:
    destination = Destination.from_dict(item)
    destinations.append(destination)

# Total destinations show karna
print("SMART LIFE PLANNER")
print("------------------")
print("Total destinations:", len(destinations))

# Tamam destinations ke naam show karna
for destination in destinations:
    print(destination.name)
