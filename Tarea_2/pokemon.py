import requests

class Pokemon:

    def generation_1(self):
        url_generation_1 = "https://pokeapi.co/api/v2/generation/1"
        
        pokemon_data = {
            "pokemon_species": ""
        }

        response = requests.get(url_generation_1)
        data = response.json()
        
        pokemon_data["pokemon_species"] = data["pokemon_species"]

        poke_generation_1 = [pokemon["name"] for pokemon in data["pokemon_species"]]
        print("Elegiste la generación 1")
        print(poke_generation_1)

    def generation_2(self):
        url_generation_2 = "https://pokeapi.co/api/v2/generation/2"
        
        pokemon_data = {
            "pokemon_species": ""
        }

        response = requests.get(url_generation_2)
        data = response.json()
        
        pokemon_data["pokemon_species"] = data["pokemon_species"]

        poke_generation_2 = [pokemon["name"] for pokemon in data["pokemon_species"]]

        print("Elegiste la generación 2")
        print(poke_generation_2)

    def generation_3(self):
        url_generation_3 = "https://pokeapi.co/api/v2/generation/3"
        
        pokemon_data = {
            "pokemon_species": ""
        }

        response = requests.get(url_generation_3)
        data = response.json()
        
        pokemon_data["pokemon_species"] = data["pokemon_species"]

        poke_generation_3 = [pokemon["name"] for pokemon in data["pokemon_species"]]

        print("Elegiste la generación 3")
        print(poke_generation_3)

    def generation_4(self):
        url_generation_4 = "https://pokeapi.co/api/v2/generation/4"
        
        pokemon_data = {
            "pokemon_species": ""
        }

        response = requests.get(url_generation_4)
        data = response.json()
        
        pokemon_data["pokemon_species"] = data["pokemon_species"]

        poke_generation_4 = [pokemon["name"] for pokemon in data["pokemon_species"]]

        print("Elegiste la generación 4")
        print(poke_generation_4)

    def generation_5(self):

        url_generation_5 = "https://pokeapi.co/api/v2/generation/5"
        
        pokemon_data = {
            "pokemon_species": ""
        }

        response = requests.get(url_generation_5)
        data = response.json()
        
        pokemon_data["pokemon_species"] = data["pokemon_species"]

        poke_generation_5 = [pokemon["name"] for pokemon in data["pokemon_species"]]

        print("Elegiste la generación 5")
        print(poke_generation_5)

    def generation_6(self):

        url_generation_6 = "https://pokeapi.co/api/v2/generation/6"
        
        pokemon_data = {
            "pokemon_species": ""
        }

        response = requests.get(url_generation_6)
        data = response.json()
        
        pokemon_data["pokemon_species"] = data["pokemon_species"]

        poke_generation_6 = [pokemon["name"] for pokemon in data["pokemon_species"]]

        print("Elegiste la generación 6")
        print(poke_generation_6)

    def generation_7(self):

        url_generation_7 = "https://pokeapi.co/api/v2/generation/7"
        
        pokemon_data = {
            "pokemon_species": ""
        }

        response = requests.get(url_generation_7)
        data = response.json()
        
        pokemon_data["pokemon_species"] = data["pokemon_species"]

        poke_generation_7 = [pokemon["name"] for pokemon in data["pokemon_species"]]

        print("Elegiste la generación 7")
        print(poke_generation_7)

    def generation_8(self):

        url_generation_8 = "https://pokeapi.co/api/v2/generation/8"
        
        pokemon_data = {
            "pokemon_species": ""
        }

        response = requests.get(url_generation_8)
        data = response.json()
        
        pokemon_data["pokemon_species"] = data["pokemon_species"]

        poke_generation_8 = [pokemon["name"] for pokemon in data["pokemon_species"]]

        print("Elegiste la generación 8")
        print(poke_generation_8)


    def poke_forma(self):
        url_form = 'https://pokeapi.co/api/v2/pokemon-shape/'
        resp = requests.get(url_form)
        data = resp.json()
        print('Escribir uno de los siguientes formas:')
        for x in data["results"]:
            print(x["name"])
        form_selected = input('forma: ')
        url_form += form_selected
        resp = requests.get(url_form)
        data = resp.json()
        for x in data["pokemon_species"]:
            print(x["name"])