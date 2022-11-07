from book import Book


# Estos metodos necesitan adaptarce al objeto book
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
                n.show_books()
                flag = False
        if flag:
            print('No existe un valor con el ISBN solicitado')
    elif option == 2:
        title = input('Escribir Titulo : ')
        flag = True
        for n in datos:
            if n.title == title:
                n.show_books()
                flag = False
        if flag:
            print('El valor no se encuentra ')


def ordertitle(datos: list):
    change = True
    while change:
        change = False
        for i in range(len(datos) - 1):
            if datos[i].title > datos[i + 1].title:
                datos[i], datos[i + 1] = datos[i + 1], datos[i]
                change = True
    for x in datos:
        print(x.title)


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
                    n.show_books()
                    flag = False
            if flag:
                print('No existe un valor con el autor solicitado')
        if option == 2:
            editorial = input('Escribir editorial : ')
            flag = True
            for n in datos:
                if n.editorial == editorial:
                    n.show_books()
                    flag = False
            if flag:
                print('No existe un valor con el editorial solicitado')
        if option == 3:
            genero = input('Escribir genero : ')
            flag = True
            for n in datos:
                if n.genre == genero:
                    n.show_books()
                    flag = False
            if flag:
                print('No existe un valor con el genero solicitado')


def numberauthor(datos: list):
    number_author = int(input('Cantiddad de autores : '))
    for bookk in datos:
        if len(bookk.autor.split('.')) == number_author:
            print(bookk.show_books())
