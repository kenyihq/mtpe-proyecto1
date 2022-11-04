import requests

class Pokeapi:

    def get_pokemon(self):
        url = 'https://pokeapi.co/api/v2/pokemon'
        res = requests.get(url)

        res = res.json()

        for i in res['results']:
            print(i["name"])
