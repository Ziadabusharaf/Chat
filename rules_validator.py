class RulesValidator:
    def __init__(self):
        # Some example Texas/Dallas-specific rules
        self.texas_dallas_rules = {
            "building_height_limit": 50,  # in feet, just an example
            "foundation_rebar_min": 4,
        }

    def validate_building_height(self, height):
        """Checks if building height meets the Dallas limit."""
        limit = self.texas_dallas_rules["building_height_limit"]
        if height <= limit:
            return True, f"Building height {height} ft is within the limit of {limit} ft."
        else:
            return False, f"Building height {height} ft exceeds the limit of {limit} ft."

    def validate_foundation_rebar(self, rebar_count):
        """Checks the minimum rebar requirement."""
        min_rebar = self.texas_dallas_rules["foundation_rebar_min"]
        if rebar_count >= min_rebar:
            return True, f"Rebar count {rebar_count} meets the minimum requirement of {min_rebar}."
        else:
            return False, f"Rebar count {rebar_count} is below the minimum requirement of {min_rebar}."
