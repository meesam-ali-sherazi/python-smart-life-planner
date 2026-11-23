
from services.trip_calculator import TripCostCalculator
from services.feasibility_checker import TripFeasibilityChecker
from services.trip_optimizer import TripOptimizer
from services.itinerary_generator import ItineraryGenerator


class TripPlanner:

    def __init__(self, destinations):
        self.destinations = destinations
        self.calculator = TripCostCalculator()
        self.feasibility_checker = TripFeasibilityChecker()
        self.optimizer = TripOptimizer(destinations)
        self.itinerary = ItineraryGenerator()

    def show_destinations(self):
        print("\nAVAILABLE DESTINATIONS")
        print("----------------------")

        for number, destination in enumerate(self.destinations, start=1):
            print(f"{number}. {destination.name}")

    def get_positive_number(self, message, allow_zero=False):
        while True:
            try:
                number = int(input(message))

                if number < 0 or (number == 0 and not allow_zero):
                    print("Please enter a valid number.")
                    continue

                return number

            except ValueError:
                print("Please enter numbers only.")

    def run(self):

        self.show_destinations()

        while True:
            choice = self.get_positive_number(
                "\nSelect destination number: "
            )

            if 1 <= choice <= len(self.destinations):
                destination = self.destinations[choice - 1]
                break

            print("Invalid destination choice.")

        budget = self.get_positive_number("Enter your budget (PKR): ")
        travellers = self.get_positive_number("Enter number of travellers: ")
        days = self.get_positive_number("Enter number of days: ")

        nights = self.get_positive_number(
            "Enter number of nights: ",
            allow_zero=True
        )

        if nights > days:
            print("Nights cannot be greater than days.")
            return

        # Calculate trip cost
        result = self.calculator.calculate_trip_cost(
            destination, travellers, days, nights
        )

        # Check budget feasibility
        feasibility = self.feasibility_checker.check_feasibility(
            result["total"], budget
        )

        # Display cost report
        print("\nYOUR TRIP COST REPORT")
        print("=====================")

        print("Destination:", destination.name)
        print("Travellers:", travellers)
        print("Days:", days)
        print("Nights:", nights)

        print("\nCOST BREAKDOWN")
        print("---------------------")
        print("Transport: Rs.", round(result["transport"]))
        print("Hotel rooms required:", result["rooms"])
        print("Accommodation: Rs.", round(result["accommodation"]))
        print("Food: Rs.", round(result["food"]))
        print("Activities: Rs.", round(result["activities"]))
        print("Emergency allowance: Rs.", round(result["emergency"]))

        print("\nTotal estimated cost: Rs.", round(result["total"]))
        print("Cost per person: Rs.", round(result["per_person"]))
        print("Your budget: Rs.", budget)
        print("Status:", feasibility["status"])

        if feasibility["is_feasible"]:
            print(
                "Remaining amount: Rs.",
                round(feasibility["remaining"])
            )

        else:
            print(
                "Extra amount needed: Rs.",
                round(feasibility["shortage"])
            )

            # Show affordable alternative destinations
            self.optimizer.show_suggestions(
                budget, travellers, days, nights
            )

        # Generate day-wise itinerary
        self.itinerary.generate_itinerary(destination, days)
