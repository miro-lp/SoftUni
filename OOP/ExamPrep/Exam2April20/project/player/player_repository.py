class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def __iter__(self):
        return self.players

    def add(self, player):
        if player.username in [p.username for p in self.players]:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        for p in self.players:
            if p.username == player:
                self.players.remove(p)
                self.count -= 1
                break

    def find(self, username):
        for p in self.players:
            if p.username == username:
                return p
