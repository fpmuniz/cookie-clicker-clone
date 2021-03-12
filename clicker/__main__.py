from clicker.building import Building


def generate_buildings():
    cursor = Building(batch=0.1, cost=15)
    grandma = Building(batch=1, cost=100)
    farm = Building(batch=8, cost=1.1e3)
    mine = Building(batch=47, cost=12e3)
    factory = Building(batch=260, cost=13e4)
    bank = Building(batch=1.4e3, cost=1.4e6)
    temple = Building(batch=7.8e3, cost=20e6)


if __name__ == "__main__":
    pass
