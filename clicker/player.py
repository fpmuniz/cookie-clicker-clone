from typing import List
import logging

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
            logging.info(f"Not enough cookies to buy {building.name}.")
            return
        self._cookies -= building.cost
        building.create()
        logging.info(f"Bought a new {building.name}!")

    def get_cookies(self, building_list: List[Building]):
        new_cookies = 0
        for building in building_list:
            new_cookies += building.generate_batches()
        self._cookies += new_cookies
        logging.info(f"Got {new_cookies} cookies from buildings.")

    def click(self):
        new_cookies = self._clicker.generate_batches()
        self._cookies += new_cookies
        logging.info(f"Got {new_cookies} cookies from clicking.")
