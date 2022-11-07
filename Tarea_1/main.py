from menu import Menu
from read_books import *
menu = Menu()
    

def run():
    books = menu.list_books()
    menu.select_option(books)


if __name__ == '__main__':
    run()
