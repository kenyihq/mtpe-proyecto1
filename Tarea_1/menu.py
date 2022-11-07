from read_books import read_books
from read_books import new_book
from book import Book
from test import *


class Menu:

    def show_menu(self):
        menu = "\n\t B I B L I O T E C A \n"
        menu += "\n" + "*" * 40 + "\n"
        menu += "Opción 1: Listar libros\n"
        menu += "Opción 2: Agregar libro\n"
        menu += "Opción 3: Eliminar libro\n"
        menu += "Opción 4: Buscar libro por ISBN o por título\n"
        menu += "Opción 5: Ordenar libros por título\n"
        menu += "Opción 6: Buscar libros por autor, editorial o género\n"
        menu += "Opción 7: Buscar libros por número de autores\n"
        menu += "Opción 8: Salir\n"
        menu += "\n" + "*" * 40

        return menu



    def list_books(self):
        books = read_books('./text.csv')
        b = []
        for i in books:
            libro = Book(i[0], i[1], i[2], i[3], i[4], i[5])
            b.append(libro)

            print(libro.show_books())
        return b

    def add_book(self):
        new_book('./text.csv')

    def delete_book(self):
        delete_book = Book().delete_book()
        delete_book = int(delete_book)

        books = read_books('./text.csv')

        # for i in range(len(books)):
        #     for j in range(len(books)):

        #         if str(books[i][j]) == str(delete_book):

        #             mes = books[delete_book - 1]

        for i in books:
            if int(i[0]) == delete_book:
                mes = f"ID del libro es: {i[0]}"

        print(mes)

    def select_option(self, books):
        print(self.show_menu())
        option = input("Ingrese una opcion válida: ")

        if option == '1':
            self.list_books()

        elif option == '2':
            self.add_book()

        elif option == '3':
            self.delete_book()

        elif option == '4':
            searchisbntitle(books)

        elif option == '5':
            ordertitle(books)

        elif option == '6':
            search_author_editorial_genre(books)

        elif option == '7':
            numberauthor(books)

        elif option == '8':
            self.option_8()

        elif option == '9':
            quit

        else:
            print("\n" + "*" * 40 + "\n")
            print("\tElija una opción válida")
            print("\n" + "*" * 40 + "\n")
            self.select_option()

        return
