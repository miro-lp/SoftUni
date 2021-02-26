from project import Player
from project import Guild

player_1 = Player("George", 50, 100)
print(player_1.add_skill("Shield Break", 20))
print(player_1.player_info())
guild = Guild("UGT")
print(guild.assign_player(player_1))
print(guild.guild_info())

player = Player("Pesho", 90, 90)
print(player.player_info())

guild_1 = Guild("GGXrd")
player = Player("Pesho", 90, 90)
print(guild_1.assign_player(player))
print(guild_1.assign_player(player))
print(guild_1.assign_player(player_1))
