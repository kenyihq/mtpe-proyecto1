import requests


class Pokemon:

    def generation_1(self):
        print("Elegiste la generación 1")

    def generation_2(self):
        print("Elegiste la generación 2")

    def generation_3(self):
        print("Elegiste la generación 3")

    def generation_4(self):
        print("Elegiste la generación 4")

    def generation_5(self):
        print("Elegiste la generación 5")

    def generation_6(self):
        print("Elegiste la generación 6")

    def generation_7(self):
        print("Elegiste la generación 7")

    def generation_8(self):
        print("Elegiste la generación 8")

    def generation_9(self):
        print("Elegiste la generación 9")

    def ability(self):
        url_ability = 'https://pokeapi.co/api/v2/ability/'
        resp = requests.get(url_ability)
        data = resp.json()
        print('Escribir una de la siguientes habilidades:')
        for x in data['results']:
            print(x['name'])
        ability_selected = input('habilidad: ')
        url_ability += ability_selected
        resp = requests.get(url_ability)
        data = resp.json()
        for x in data['pokemon']:
            print(x['pokemon']['name'])

    def habit(self):
        url_habit = 'https://pokeapi.co/api/v2/pokemon-habitat/'
        resp = requests.get(url_habit)
        data = resp.json()
        print('Escribir uno de los siguientes habitats:')
        for x in data['results']:
            print(x['name'])
        habit_selected = input('Habitat: ')
        url_habit += habit_selected
        resp = requests.get(url_habit)
        data = resp.json()
        for x in data['pokemon_species']:
            print(x['name'])

    def types(self):
        url_type_rock = 'https://pokeapi.co/api/v2/type/'
        resp = requests.get(url_type_rock)
        data = resp.json()
        print('Escribir uno de los siguientes tipos:')
        for x in data['results']:
            print(x['name'])
        tipe_selected = input('Tipo: ')
        url_type_rock += tipe_selected
        resp = requests.get(url_type_rock)
        data = resp.json()
        for x in data['pokemon']:
            print(x['pokemon']['name'])