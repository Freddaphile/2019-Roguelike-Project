import libtcodpy as libtcod

from random import randint

from game_messages import Message


class Fighter:
    def __init__(self, hp, defense, power, armor_class):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
        self.armor_class = armor_class

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner})

        return results

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack(self, target):
        results = []

        nat_roll = randint(1, 20)
        attack_roll = nat_roll + self.power

        if attack_roll >= target.fighter.armor_class:

            damage = self.power - target.fighter.defense

            if damage > 0:
                results.append({'message': Message('{0} attacks {1} and hits on a {2}! The attack deals {3} damage!'.format(
                    self.owner.name.capitalize(), target.name, attack_roll, str(damage)), libtcod.white)})
                results.extend(target.fighter.take_damage(damage))

            elif nat_roll == 20:
                results.append({'message': Message('{0} attacks {1} and scores a critical hit, dealing double damage for {2} damage!'.format(
                    self.owner.name.capitalize(), target.name, str(damage)), libtcod.yellow)})
                results.extend(target.fighter.take_damage(damage))

            else:
                results.append({'message': Message('{0} attacks {1} but does no damage!'.format(
                    self.owner.name.capitalize(), target.name), libtcod.white)})
        else:
            results.append({'message': Message('{0} attacks {1} but misses on a {2}'.format(
                self.owner.name.capitalize(), target.name, attack_roll), libtcod.white)})

        return results