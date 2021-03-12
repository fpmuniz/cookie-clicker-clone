import pytest

from clicker.building import Building


@pytest.fixture
def building():
    return Building(name="Building", batch=1)


def test_create_building(building):
    building.create()
    assert building.count == 1


def test_increase_cost_after_creation(building):
    building.cost = 1
    building.create()
    assert building.cost == 1.15


def test_generate_batches(building):
    building.create(10)
    assert building.generate_batches() == 10
