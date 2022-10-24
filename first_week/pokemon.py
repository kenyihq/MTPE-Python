import requests

def load_pokemon(pokemon):
    path = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'

    response = requests.get(path)

    if response:
        result = response.json()

        abilities = list()
    
        for ability in result['abilities']:
            name_ability = ability['ability'] ['name']
            abilities.append(name_ability)

    return abilities

pokemon_name = input("Ingrese el nombre de su Pokemon: ").lower()
print(load_pokemon(pokemon_name))