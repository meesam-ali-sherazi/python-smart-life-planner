
class Destination:
    def __init__(
        self,
        name,
        region,
        destination_type,
        transport_cost_per_person,
        accommodation_cost_per_room_per_night,
        food_cost_per_person_per_day,
        activities_misc_per_person,
        room_capacity
    ):
        self.name = name
        self.region = region
        self.destination_type = destination_type
        self.transport_cost_per_person = transport_cost_per_person
        self.accommodation_cost_per_room_per_night = accommodation_cost_per_room_per_night
        self.food_cost_per_person_per_day = food_cost_per_person_per_day
        self.activities_misc_per_person = activities_misc_per_person
        self.room_capacity = room_capacity

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def display_info(self):
        print(f"Destination: {self.name}")
        print(f"Region: {self.region}")
        print(f"Type: {self.destination_type}")
        print(f"Transport per person: Rs. {self.transport_cost_per_person}")
        print(f"Hotel per room/night: Rs. {self.accommodation_cost_per_room_per_night}")
        print(f"Food per person/day: Rs. {self.food_cost_per_person_per_day}")
        print(f"Room capacity: {self.room_capacity}")
