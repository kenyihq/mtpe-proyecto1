class Book:
    def __init__(self, id_book = None, title = None, genre = None, isbn = None, editorial = None, autor = None):
        self.id_book = id_book
        self.title = title
        self.genre = genre
        self.isbn = isbn
        self.editorial = editorial
        self.autor = autor

    def show_books(self):

        show_book = f'\nID\t\t: {self.id_book}\n'
        show_book += f'Título\t\t: {self.title}\n'
        show_book += f'Género\t\t: {self.genre}\n'
        show_book += f'ISBN\t\t: {self.isbn}\n'
        show_book += f'Editorial\t: {self.editorial}\n'
        show_book += f'Autor\t\t: {self.autor}\n'

        return show_book


    def add_book(self):
        print("Ingrese los siguientes datos: \n")
        idlibro = input('ID: ')
        titulo = input('Título: ')
        genero = input('Género: ')
        isbn = input('ISBN: ')
        editorial = input('Editorial: ')
        autor = input('Autor: ')

        new_book = [idlibro, titulo, genero, isbn, editorial, autor]

        print(new_book)

        return new_book




