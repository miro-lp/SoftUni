from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        if type.lower() == "beginner":
            player = Beginner(username)
        elif type.lower() == "advanced":
            player = Advanced(username)
        self.player_repository.add(player)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        if type == "Magic":
            card = MagicCard(name)
        elif type == "Trap":
            card = TrapCard(name)
        self.card_repository.add(card)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        for c in self.card_repository.cards:
            if c.name == card_name:
                for p in self.player_repository.players:
                    if p.username == username:
                        p.card_repository.add(c)
                        break
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = [p for p in self.player_repository.players if p.username == attack_name][0]
        enemy = [p for p in self.player_repository.players if p.username == enemy_name][0]
        BattleField().fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ""
        for p in self.player_repository.players:
            result += f"Username: {p.username} - Health: {p.health} - Cards {p.card_repository.v_count}" + "\n"
            result += '\n'.join(
                [f'### Card: {c.name} - Damage: {c.damage_points}' for c in p.card_repository.cards]) + "\n"

        return result
