from unittest.mock import Mock

import pytest

from clicker.player import Player
from clicker.building import Building


@pytest.fixture
def building():
    out = Building(name="Building", batch=100, cost=500)
    return out


@pytest.fixture
def player():
    return Player()


def test_clicks(player):
    player.click()
    assert player.cookies == 1


def test_get_cookies(player, building):
    building.create()
    player.get_cookies([building, building])
    assert player.cookies == 200


def test_buy_building(player, building):
    building.create()
    player.get_cookies([building] * 5)
    player.buy_building(building)
    assert building.count == 2
    assert player.cookies == 0
