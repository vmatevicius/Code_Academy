import time


class Carrier:
    """Shuttle cost currency is USD    Shutlle weight is in kg    Year built should be in this format: YYYY"""

    def __init__(
        self,
        cost: float,
        year_built: int,
        weight: float,
    ) -> None:
        self._cost: float = cost
        self._year_built: int = year_built
        self._weight: float = weight

    def get_age(self) -> int:
        current_timestamp = time.time()
        current_year = time.gmtime(current_timestamp).tm_year
        return current_year - self._year_built

    def get_cost(self) -> float:
        return self._cost

    def get_weight(self) -> float:
        return self._weight


class SpaceShuttle(Carrier):
    CEPAJAV_CONSTANT = 2500
    """Use imperial units for the lenght measurements"""

    def _get_burn_rate_variable(self, orbit_height: float) -> float:
        return self.CEPAJAV_CONSTANT / orbit_height

    def get_fuel_cost(
        self, fuel_cost: float, burn_rate: float, orbit_height: float
    ) -> float:
        burn_rate_variable = self._get_burn_rate_variable(orbit_height)
        return fuel_cost * burn_rate * burn_rate_variable

    def get_average_personel_expenses(
        self, base_salary: float, people_count: int
    ) -> float:
        return base_salary * people_count

    def calculate_mission_cost(
        self,
        fuel_cost: float,
        burn_rate: float,
        orbit_height: float,
        base_salary: float,
        people_count: int,
    ) -> float:
        expedition_fuel_cost = self.get_fuel_cost(fuel_cost, burn_rate, orbit_height)
        average_personel_cost = self.get_average_personel_expenses(
            base_salary, people_count
        )
        return expedition_fuel_cost + average_personel_cost
