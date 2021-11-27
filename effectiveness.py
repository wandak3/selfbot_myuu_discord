import pokedex as pokedex

class effectiveness:
    def __init__(self, string):
        self.string = string
        self.name = ''
        self.abilities = []
        self.types = []

    def check_effectiveness(self, attack, defense):
        type_attack = pokedex.get_type(attack)
        if defense in [types.name for types in type_attack[0]]:
            return 0.0
        elif defense in [types.name for types in type_attack[0]]:
            return 0.5
        elif defense in [types.name for types in type_attack[0]]:
            return 2.0
        else:
            return 1.0
