import requests


class Pokemon:

    def generation_1(self):
        print("Elegiste la generación 1")
        for x in range(10):
            #resp = requests.get(f'https://pokeapi.co/api/v2/pokemon/{x+1}')
            #resp = resp.json()
            #print(resp['past_types'])
            resp = requests.get(f'https://pokeapi.co/api/v2/pokemon/{x+1}')
            resp = resp.json()
            for y in resp:
                print(y)

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
