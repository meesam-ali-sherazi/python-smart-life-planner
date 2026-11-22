
import math


class TripCostCalculator:

    def calculate_trip_cost(self, destination, travellers, days, nights):

        # Transport cost
        transport_cost = (
            destination.transport_cost_per_person * travellers
        )

        # Hotel rooms calculate karna
        rooms = math.ceil(travellers / destination.room_capacity)

        # Accommodation cost
        accommodation_cost = (
            destination.accommodation_cost_per_room_per_night
            * rooms
            * nights
        )

        # Food cost
        food_cost = (
            destination.food_cost_per_person_per_day
            * travellers
            * days
        )

        # Activities aur miscellaneous cost
        activities_cost = (
            destination.activities_misc_per_person * travellers
        )

        # Total cost before emergency allowance
        subtotal = (
            transport_cost
            + accommodation_cost
            + food_cost
            + activities_cost
        )

        # 10% emergency allowance
        emergency_cost = subtotal * 0.10

        # Final total
        total_cost = subtotal + emergency_cost

        return {
            "transport": transport_cost,
            "rooms": rooms,
            "accommodation": accommodation_cost,
            "food": food_cost,
            "activities": activities_cost,
            "emergency": emergency_cost,
            "total": total_cost,
            "per_person": total_cost / travellers
        }
