import urwid

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


def click(button):
    player.click()


def widget_layout():
    title = urwid.Text("Cookie Clicker Clone")
    fill = urwid.Filler(title, "top")

    store_widgets = []
    info_widgets = []
    for b in buildings:
        store_widgets.append(urwid.Button(f"{b.name}: {b.cost:.2f} cookies"))
        info_widgets.append(
            urwid.Text(f"{b.name}: {b.count} producing {b.batch} cookies each.")
        )

    clicker = urwid.Button("Click me!", on_press=click)
    total = urwid.Text(f"{player.cookies}")

    click_column = urwid.Pile([clicker, total])
    info = urwid.Pile(info_widgets)
    store = urwid.Pile(store_widgets)

    cols = urwid.Columns([click_column, info, store])
    fill = urwid.Filler(cols)
    return fill


def handle_input(key):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop


if __name__ == "__main__":
    buildings = generate_buildings()
    player = Player()
    layout = widget_layout()
    loop = urwid.MainLoop(layout, unhandled_input=handle_input)
    loop.run()
