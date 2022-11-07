def searchisbntitle(datos: list):
    print('Escriba el numero opcion que requiera')
    print('Opcion 1 : Buscar por ISBN')
    print('Opcion 2 : BUscar por Titulo')
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
