import libtcodpy as libtcod

from game_messages import Message

from game_states import GameStates

from render_functions import RenderOrder


def kill_player(player):
    player.char = '%'
    player.color = libtcod.dark_red

    return Message('You have perished. The gods judge you unworthy.', libtcod.red), GameStates.PLAYER_DEAD 
    # libtcod.red or libtcod.darkRed?


def kill_monster(monster):
    death_message = Message('The {0} dies.'.format(monster.name.capitalize()), libtcod.orange)

    monster.char = '%'
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = monster.name + ' corpse'
    monster.render_order = RenderOrder.CORPSE

    return death_message