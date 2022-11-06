from read_books import read_books
from read_books import new_book
from book import Book

class Menu:

    def show_menu(self):
        menu = "\n\t B I B L I O T E C A \n"
        menu += "\n" + "*"*40 + "\n"
        menu += "Opción 1: Listar libros\n"
        menu += "Opción 2: Agregar libro\n"
        menu += "Opción 3: Eliminar libro\n"
        menu += "Opción 4: Buscar libro por ISBN o por título\n"
        menu += "Opción 5: Ordenar libros por título\n"
        menu += "Opción 6: Buscar libros por autor, editorial o género\n"
        menu += "Opción 7: Buscar libros por número de autores\n"
        menu += "Opción 8: Salir\n"
        menu += "\n" + "*"*40

        return menu

    def list_books(self):
        books = read_books('./text.csv')

        for i in books:
            libro = Book(i[0], i[1], i[2], i[3], i[4], i[5])

            print(libro.show_books())

    def add_book(self):
        #Book().add_book()
        new_book('./text.csv')



    def select_option(self):
        print(self.show_menu())
        option = input("Ingrese una opcion válida: ")

        if option == '1':

            self.list_books()

        elif option == '2':
            self.add_book()


        elif option == '3':
            self.option_3()

        elif option == '4':
            self.option_4()

        elif option == '5':
            self.option_5()
        
        elif option == '6':
            self.option_6()
        
        elif option == '7':
            self.option_7()
        
        elif option == '8':
            self.option_8()

        elif option == '9':
            quit

        else:
            print("\n" + "*"*40 + "\n")
            print("\tElija una opción válida")
            print("\n" + "*"*40 + "\n")
            self.select_option()
        
        return

