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


def agregar():
    idlibro = input('id:')
    titulo = input('titulo:')
    genero = input('genero:')
    isbn = input('isbn:')
    editorial = input('editorial:')
    autor = input('autor :')
    x = Libro(idlibro, titulo, genero, isbn, editorial, autor)


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


def searchisbntitle(datos: list):
    print('Escriba el numero opcion que requiera')
    print('Opcion 1 : Buscar por ISBN')
    print('Opcion 2 : Buscar por Titulo')
    option = 0
    while (option != 1) and (option != 2):
        option = int(input("Seleccione una opcion: "))
    if option == 1:
        isbn = input('Escribir ISBN : ')
        flag = True
        for n in datos:
            if n.isbn == isbn:
                n.listar()
                flag = False
        if flag:
            print('No existe un valor con el ISBN solicitado')
    elif option == 2:
        title = input('Escribir Titulo : ')
        flag = True
        for n in datos:
            if n.titulo == title:
                n.listar()
                flag = False
        if flag:
            print('El valor no se encuentra ')


def ordertitle(datos: list):
    change = True
    while change:
        change = False
        for i in range(len(datos) - 1):
            if datos[i].titulo > datos[i + 1].titulo:
                datos[i], datos[i + 1] = datos[i + 1], datos[i]
                change = True
    for x in datos:
        print(x.titulo)


def search_author_editorial_genre(datos: list):
    print('Escriba el numero opcion que requiera')
    print('Opcion 1 : Buscar por autor')
    print('Opcion 2 : Buscar por editorial')
    print('Opcion 3 : Buscar por genero')
    option = 0
    while (option != 1) and (option != 2) and (option != 3):
        option = int(input("Seleccione una opcion: "))
        if option == 1:
            author = input('Escribir author : ')
            flag = True
            for n in datos:
                if n.autor == author:
                    n.listar()
                    flag = False
            if flag:
                print('No existe un valor con el autor solicitado')
        if option == 2:
            editorial = input('Escribir editorial : ')
            flag = True
            for n in datos:
                if n.editorial == editorial:
                    n.listar()
                    flag = False
            if flag:
                print('No existe un valor con el editorial solicitado')
        if option == 3:
            genero = input('Escribir genero : ')
            flag = True
            for n in datos:
                if n.genero == genero:
                    n.listar()
                    flag = False
            if flag:
                print('No existe un valor con el genero solicitado')


def numberauthor(datos: list):
    number_author = int(input('Cantiddad de autores : '))
    for book in datos:
        if len(book.autor.split('.')) == number_author:
            print(book.listar())

        # libro1 = Libro(1, 'The book', 'Accion', 'ISBN', 'El comercio', 'Anonimo')


# readbook(datos)
readbooks(biblio)
# listar(biblio)
# searchisbntitle(biblio)
# ordertitle(biblio)
# search_author_editorial_genre(biblio)
numberauthor(biblio)