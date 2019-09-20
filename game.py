from typyboi import player, items, tiles, world

_player = None

def main():
    while True:
        room = world.get_tile(_player.location_x, _player.location_y)
        room.modify_player(_player)
        if(_player.is_alive()):
            print('Choose an actions:\n')
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    _player.do_action(action, **action.kwargs)
                    break
        else:
            break



if __name__ == '__main__':
    world.add_tile(tiles.MapTile(0, 0, "First room"))
    world.add_tile(tiles.MapTile(0, 0, "First room"))
    world.add_tile(tiles.LootRoom(1, 0, "East loot room", [], 5))
    _player = player.Player(0, 0 , 100)
    main()