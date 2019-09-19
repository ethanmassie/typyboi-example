from typyboi import player, items, tiles

def main():
    world = tiles.World()
    world.add_tile(tiles.MapTile(0, 0, "First room"))
    world.add_tile(tiles.LootRoom(1, 0, "East loot room", [], 5))

if __name__ == '__main__':
    main()