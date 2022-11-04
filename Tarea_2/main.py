from read_api import Pokeapi

def run():
    list_pokemon = Pokeapi()

    list_pokemon.get_pokemon()


if __name__ == '__main__':
    run()