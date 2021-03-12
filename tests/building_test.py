from clicker.building import Building


def test_create_building():
    click = Building(name="Building", batch=1)
    click.create()
    assert click.count == 1


def test_generate_batches():
    click = Building(name="Building", batch=1)
    click.create(10)
    assert click.generate_batches() == 10
