
class TripFeasibilityChecker:

    def check_feasibility(self, total_cost, budget):

        if total_cost < budget:
            return {
                "status": "Within Budget",
                "remaining": budget - total_cost,
                "shortage": 0,
                "is_feasible": True
            }

        elif total_cost == budget:
            return {
                "status": "Exactly Within Budget",
                "remaining": 0,
                "shortage": 0,
                "is_feasible": True
            }

        else:
            return {
                "status": "Over Budget",
                "remaining": 0,
                "shortage": total_cost - budget,
                "is_feasible": False
            }
