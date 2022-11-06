

class Book:
    def __init__(self, id_book, title, genre, isbn, editorial, autor):
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
        idlibro = input('id:')
        titulo = input('titulo:')
        genero = input('genero:')
        isbn = input('isbn:')
        editorial = input('editorial:')
        autor = input('autor :')
        #x=Libro(idlibro,titulo,genero,isbn,editorial,autor)




