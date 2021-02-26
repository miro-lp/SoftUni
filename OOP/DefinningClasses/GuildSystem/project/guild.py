from .player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        if player_name in [i.name for i in self.players]:
            for j in self.players:
                j: Player
                if j.name == player_name:
                    self.players.remove(j)
                    j.guild = "Unaffiliated"
                    break
            return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        name_info = f"Guild: {self.name}"
        players_info = "\n".join([p.player_info() for p in self.players])
        return name_info + "\n" + players_info
