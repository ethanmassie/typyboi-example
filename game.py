from typyboi import world
from typyboi.tiles import MapTile, LootRoom, EnemyRoom
from typyboi.player import Player
import factory

def main():
    while True:
        if _player.moved:
            room = world.get_tile(_player.location_x, _player.location_y)
            room.modify_player(_player)
            _player.moved = False
        if _player.is_alive() and not _player.victory:
            print(room.flavor_text)
            print('Choose an action:\n')
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            print()
            for action in available_actions:
                if action_input == action.hotkey:
                    _player.do_action(action, **action.kwargs)
                    break
        else:
            break



if __name__ == '__main__':
    world.add_tile(MapTile(0, 0, "First room"))
    world.add_tile(MapTile(0, 0, "First room"))
    world.add_tile(LootRoom(1, 0, "East loot room", [factory.dagger()], 5))
    world.add_tile(EnemyRoom(1, 1, 'A spider room', 'A spider attacks', factory.spider() ))
    _player = Player(0, 0 , 100)
    try:
        main()
    except KeyboardInterrupt:
        print()
        exit(0)