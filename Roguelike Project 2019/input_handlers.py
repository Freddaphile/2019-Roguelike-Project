import libtcodpy as libtcod

from game_states import GameStates

# Make it so you can hit (i) to go out of menu if you want to.

def handle_keys(key, game_state):
    if game_state == GameStates.PLAYERS_TURN:
        return handle_player_turn_keys(key)
    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(key)
    elif game_state == GameStates.TARGETING:
        return handle_targeting_keys(key)
    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        return handle_inventory_keys(key)

    return {}

def handle_inventory_keys(key):
    index = key.c - ord('a')

    if index >= 0:
        return {'inventory_index': index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {'exit': True}

    return {}

def handle_main_menu(key):
    key_char = chr(key.c)

    if key_char == 'a':
        return {'new_game': True}
    elif key_char == 'b':
        return {'load_game': True}
    elif key_char == 'c' or key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}
    
    return {}

def handle_player_turn_keys(key):
    key_char = chr(key.c)

    # vi keys commented out, haven't bothered to implement them yet as I never use them.
    # I've just noted down what they are and where they go for when I eventually do.
    if key.vk == libtcod.KEY_KP8 or key.vk == libtcod.KEY_UP: # or key_char == 'k':
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_KP2 or key.vk == libtcod.KEY_DOWN: # or key_char == 'j':
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_KP4 or key.vk == libtcod.KEY_LEFT: # or key_char == 'h':
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_KP6 or key.vk == libtcod.KEY_RIGHT: # or key_char == 'l':
        return {'move': (1, 0)}
    elif key.vk == libtcod.KEY_KP7 or key_char == 'y':
        return {'move': (-1, -1)}
    elif key.vk == libtcod.KEY_KP9 or key_char == 'u':
        return {'move': (1, -1)}
    elif key.vk == libtcod.KEY_KP1 or key_char == 'b':
        return {'move': (-1, 1)}
    elif key.vk == libtcod.KEY_KP3 or key_char == 'n':
        return {'move': (1, 1)}
    elif key.vk == libtcod.KEY_KP5 or key_char == '.':
        return {'wait': True} # KP5 doesn't work, '.' works though for waiting.

    
    # Interaction keys | Calls other functions at line ~100 in engine.py
    elif key_char == 'g':
        return {'pickup': True}

    elif key_char == 'i':
        return {'show_inventory': True}

    elif key_char == 'd':
        return {'drop_inventory': True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}

def handle_targeting_keys(key):
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}

def handle_player_dead_keys(key):
    key_char = chr(key.c)

    if key_char == 'i':
        return {'show_inventory': True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {'exit': True}

    return {}

def handle_mouse(mouse):
    (x, y) = (mouse.cx, mouse.cy)

    if mouse.lbutton_pressed:
        return {'left_click': (x, y)}
    elif mouse.rbutton_pressed:
        return {'right_click': (x, y)}

    return {}