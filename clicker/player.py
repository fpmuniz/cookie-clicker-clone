from typing import List

from clicker.building import Building


class Player:
    def __init__(self):
        self._cookies = 0
        self._clicker = Building(name="Clicker", batch=1)
        self._clicker.create()

    @property
    def cookies(self) -> float:
        return self._cookies

    def buy_building(self, building: Building):
        if self.cookies < building.cost:
            return
        self._cookies -= building.cost
        building.create()

    def get_cookies(self, building_list: List[Building]):
        for building in building_list:
            self._cookies += building.generate_batches()

    def click(self):
        self._cookies += self._clicker.generate_batches()
