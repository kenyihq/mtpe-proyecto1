


class Menu:

    def show_menu(self):
        menu = "\t P  O  K  E  A  P  I \n"
        menu += "*"*40 + "\n"
        menu += "\nOpción 1: Listar pokemons por generación\n"
        menu += "Opción 2: Listar pokemons por forma\n"
        menu += "Opción 3: Listar pokemons por habilidad\n"
        menu += "Opción 4: Listar pokemons por habitat\n"
        menu += "Opción 5: Listar pokemons por tipo\n"
        menu += "\n" + "*"*40

        return menu

    def select_option(self):
        print(self.show_menu())
        option = input("Ingrese una opcion válida: ")

        if option == '1':
            self.option_1()

        elif option == '2':
            self.option_2()

        elif option == '3':
            self.option_3()

        elif option == '4':
            self.option_4()

        elif option == '5':
            self.option_5()

        else:
            print("Elija una opción válida")
            
        return True

    def option_1(self):
        print("Elegiste opcion 1")


    def option_2(self):
        print("Elegiste opcion 2")


    def option_3(self):
        print("Elegiste opcion 3")


    def option_4(self):
        print("Elegiste opcion 4")


    def option_5(self):
        print("Elegiste opcion 5")