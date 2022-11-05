import csv

biblio = []


def readbooks(date):
    with open('text.csv') as f:
        reader = csv.reader(f)
        datos = []
        for i in reader:
            datos.append(i)
        libro1 = Libro(datos[0][0], datos[0][1], datos[0][2], datos[0][3], datos[0][4], datos[0][5])
        biblio.append(libro1)
        libro2 = Libro(datos[1][0], datos[1][1], datos[1][2], datos[1][3], datos[1][4], datos[1][5])
        biblio.append(libro2)
        libro3 = Libro(datos[2][0], datos[2][1], datos[2][2], datos[2][3], datos[2][4], datos[2][5])
        biblio.append(libro3)


def listar(datos):
    for i in datos:
        i.listar()


class Libro:
    def __init__(self, idlibro, titulo, genero, isbn, editorial, autor):
        self.idlibro = idlibro
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.editorial = editorial
        self.autor = autor

    def listar(self):
        print(f'El libro {self.titulo} de {self.autor} del genero {self.genero} posee el ISBN: {self.isbn}')


    def agregar(self):
        idlibro = input('id:')
        titulo = input('titulo:')
        genero = input('genero:')
        isbn = input('isbn:')
        editorial = input('editorial:')
        autor = input('autor :')
        x=Libro(idlibro,titulo,genero,isbn,editorial,autor)


# libro1 = Libro(1, 'The book', 'Accion', 'ISBN', 'El comercio', 'Anonimo')
# readbook(datos)
readbooks(biblio)
listar(biblio)
