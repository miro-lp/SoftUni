from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name in [i.name for i in self.pokemon]:
            for i in self.pokemon:
                if i.name == pokemon_name:
                    self.pokemon.remove(i)
            return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        name_info = f"Pokemon Trainer {self.name}"
        count_pokemon = f"Pokemon count {len(self.pokemon)}"
        pokemon_li = "\n".join([f"- {i.pokemon_details()}" for i in self.pokemon])
        return name_info + "\n" + count_pokemon + "\n" + pokemon_li + "\n"
