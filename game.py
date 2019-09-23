from typyboi.world import World
from typyboi.tiles import MapTile, LootRoom, EnemyRoom
from typyboi.player import Player
import factory

def game_loop():
    player = Player(0, 0, 100)
    world = World()
    world.add_tile(MapTile(0, 0, "First room"))
    world.add_tile(LootRoom(1, 0, "East loot room", [factory.dagger()], 5))
    world.add_tile(EnemyRoom(1, 1, 'A spider room', factory.spider() ))
    while True:
        if player.moved:
            room = world.get_tile(player.location_x, player.location_y)
            room.modify_player(player)
            print(room.flavor_text)
            player.moved = False
        if player.is_alive() and not player.victory:
            print('Choose an action:\n')
            available_actions = room.available_actions(world)
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            print()
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
        else:
            break



if __name__ == '__main__':
    try:
        game_loop()
    except KeyboardInterrupt:
        print()
        exit(0)
