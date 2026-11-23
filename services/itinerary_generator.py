
class ItineraryGenerator:

    def generate_itinerary(self, destination, days):

        print("\nDAY-WISE TRIP ITINERARY")
        print("=======================")
        print("Destination:", destination.name)

        for day in range(1, days + 1):

            print(f"\nDay {day}")

            if day == 1:
                print("Morning: Travel to destination.")
                print("Afternoon: Hotel check-in and rest.")
                print("Evening: Explore nearby places.")

            elif day == days:
                print("Morning: Breakfast and local sightseeing.")
                print("Afternoon: Shopping and packing.")
                print("Evening: Return journey.")

            else:
                print("Morning: Visit popular attractions.")
                print("Afternoon: Enjoy local food and activities.")
                print("Evening: Explore the destination.")

        print("\nHave a safe and enjoyable trip!")
