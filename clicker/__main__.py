from clicker.building import Building
from clicker.player import Player


def generate_buildings():
    cursor = Building("Cursor", batch=0.1, cost=15)
    grandma = Building("Grandma", batch=1, cost=100)
    farm = Building("Farm", batch=8, cost=1.1e3)
    mine = Building("Mine", batch=47, cost=12e3)
    factory = Building("Factory", batch=260, cost=13e4)
    bank = Building("Bank", batch=1.4e3, cost=1.4e6)
    temple = Building("Temple", batch=7.8e3, cost=20e6)
    return [cursor, grandma, farm, mine, factory, bank, temple]


if __name__ == "__main__":
    buildings = generate_buildings()
    player = Player()
