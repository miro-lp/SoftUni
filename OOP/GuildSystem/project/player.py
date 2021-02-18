class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return "Skill already added"

    def player_info(self):
        name_info = f"Name: {self.name}"
        guild_info = f"Guild: {self.guild}"
        hp_info = f"HP: {self.hp}"
        mp_info = f"MP: {self.mp}"
        skills_info = "\n".join([f"==={k} - {self.skills[k]}" for k in self.skills])
        if len(self.skills) > 0:
            return name_info + "\n" + guild_info + "\n" + hp_info + "\n" + mp_info + "\n" + skills_info + "\n"
        else:
            return name_info + "\n" + guild_info + "\n" + hp_info + "\n" + mp_info + "\n"
