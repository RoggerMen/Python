from typing import Any

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        
    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no está disponible")

    def return_book(self):
        self.available = True
        print(f"El libro {self.title} ha sido devuelto")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []    

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} No está DISPONIBLE")

    def return_book(self, book):
        # SI el libro(book) esta entre los libros prestados
        # ENTONCES LO RETORNAMOS
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} No esta en la lista de prestados")

# CLASE BIBLIOTECA: Va a gestionar tanto usuarios como los libros

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado")

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")
        
    def show_available_books(self):
        print("Libros disponibles: ")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author}")

# CREAMOS LOS LIBROS
book1 = Book("El Principito", "Antoine de Saint-Exupéry")
book2 = Book("1984", "George Orwell")


# CREAMOS USUARIOS
user1 = User("Rogger", "001")


# CREAMOS LA BIBLIOTECA QUE ES LA QUE GESTIONA AMBAS LISTAS (libros(books) y usuarios(users))
library = Library()

library.add_book(book1)
library.add_book(book2)

library.register_user(user1)

# MOSTRAMOS LOS LIBROS
library.show_available_books()


# REALIZAMOS UN PRESTAMO
user1.borrow_book(book1)

# MOSTRAMOS NUEVAMENTE LOS LIBROS PARA VER CUALES ESTAN DISPONIBLES
library.show_available_books()


# DEVOLVEMOS LIBROS
user1.return_book(book1)


# VOLVEMOS A VISUALIZAR LOS LIBROS QUE ESTAN DISPONIBLES
library.show_available_books()

