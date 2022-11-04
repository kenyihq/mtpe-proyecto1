from read_api import Pokeapi
from menu import Menu

# def run():
#     list_pokemon = Pokeapi()

#     p = list_pokemon.get_pokemon()

#     for i in p:
#         print(i)

#     print(p)

def run():
    show_menu = Menu().select_option()

    print(show_menu)


if __name__ == '__main__':
    run()