
from services.trip_calculator import TripCostCalculator


class TripOptimizer:

    def __init__(self, destinations):
        self.destinations = destinations
        self.calculator = TripCostCalculator()

    def find_affordable_trips(self, budget, travellers, days, nights):

        affordable_trips = []

        for destination in self.destinations:

            result = self.calculator.calculate_trip_cost(
                destination,
                travellers,
                days,
                nights
            )

            if result["total"] <= budget:

                affordable_trips.append({
                    "destination": destination.name,
                    "total_cost": round(result["total"]),
                    "remaining_budget": round(budget - result["total"])
                })

        # Cheapest affordable trip first
        affordable_trips.sort(
            key=lambda trip: trip["total_cost"]
        )

        return affordable_trips

    def show_suggestions(self, budget, travellers, days, nights):

        suggestions = self.find_affordable_trips(
            budget, travellers, days, nights
        )

        print("\nAFFORDABLE TRIP SUGGESTIONS")
        print("---------------------------")

        if not suggestions:
            print("Sorry! No affordable destination found.")
            print("Try increasing your budget or reducing trip duration.")
            return

        for number, trip in enumerate(suggestions, start=1):

            print(f"\n{number}. {trip['destination']}")
            print("Total Cost: Rs.", trip["total_cost"])
            print("Remaining Budget: Rs.", trip["remaining_budget"])
