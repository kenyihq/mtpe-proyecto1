import requests


def get_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon'
    res = requests.get(url)

    res = res.json()

    for i in res['results']:
        print(i)

get_pokemon()