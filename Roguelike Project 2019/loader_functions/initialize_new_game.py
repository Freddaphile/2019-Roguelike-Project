import libtcodpy as libtcod

from components.fighter import Fighter
from components.inventory import Inventory

from entity import Entity

from game_messages import MessageLog

from game_states import GameStates

from map_objects.game_map import GameMap

from render_functions import RenderOrder


def get_constants():
    window_title = 'Roguelike Project 2019'

    screen_width = 80
    screen_height = 50

    # Draw health bar
    bar_width = 20
    panel_height = 7
    panel_y = screen_height - panel_height

    message_x = bar_width + 2
    message_width = screen_width - bar_width - 2
    message_height = panel_height - 1

    # Map size in tiles
    map_width = 80
    map_height = 43

    # Variables for the rooms in the map
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10

    max_monsters_per_room = 3
    max_items_per_room = 2

    # MAP COLOR SCHEME SET-UP | GRAPHICS SETTINGS GO HERE?
    colors = {
            #'dark_wall': libtcod.Color(132, 109, 116), # Dark gray 
            #'dark_ground': libtcod.Color(183, 166, 173), # Lighter gray
            'light_wall': libtcod.Color(121, 63, 13),
            'light_ground': libtcod.Color(172, 112, 61),
            'dark_wall': libtcod.Color(0, 0, 100),
            'dark_ground': libtcod.Color(50, 50, 150)
            #'light_wall': libtcod.Color(130, 110, 50),
            #'light_ground': libtcod.Color(200, 180, 50)
        }

    # Defines stuff that shouldn't change. It CAN, but it shouldn't.
    # Python has no readonly feature so constants is used as the name.
    constants = {
        'window_title': window_title,
        'screen_width': screen_width,
        'screen_height': screen_height,
        'bar_width': bar_width,
        'panel_height': panel_height,
        'panel_y': panel_y,
        'message_x': message_x,
        'message_width': message_width,
        'message_height': message_height,
        'map_width': map_width,
        'map_height': map_height,
        'room_max_size': room_max_size,
        'room_min_size': room_min_size,
        'max_rooms': max_rooms,
        'fov_algorithm': fov_algorithm,
        'fov_light_walls': fov_light_walls,
        'fov_radius': fov_radius,
        'max_monsters_per_room': max_monsters_per_room,
        'max_items_per_room': max_items_per_room,
        'colors': colors
    }

    return constants


    # Player statistics
def get_game_variables(constants):
    fighter_component = Fighter(hp=30, defense=0, power=5, armor_class=10)
    inventory_component = Inventory(26)
    player = Entity(0, 0, '@', libtcod.white, 'Player', blocks=True, render_order=RenderOrder.ACTOR,
                    fighter=fighter_component, inventory=inventory_component)
    entities = [player]

    game_map = GameMap(constants['map_width'], constants['map_height'])
    game_map.make_map(constants['max_rooms'], constants['room_min_size'], constants['room_max_size'],
                      constants['map_width'], constants['map_height'], player, entities,
                      constants['max_monsters_per_room'], constants['max_items_per_room'])

    message_log = MessageLog(constants['message_x'], constants['message_width'], constants['message_height'])

    game_state = GameStates.PLAYERS_TURN

    return player, entities, game_map, message_log, game_state