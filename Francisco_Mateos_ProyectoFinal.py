# Sistema de Gestión de Biblioteca
# Este programa simula un sistema básico para gestionar libros y préstamos en una biblioteca.

# Definimos la clase principal "Libro" según el enunciado
class Libro:
    # Constructor con los atributos requeridos: titulo, autor, isbn y disponible (True por defecto)
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    # Método agregar() para crear un nuevo libro con entrada del usuario
    def agregar():
        try:
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            # Validar que ISBN sea un número de 4 dígitos
            if not (isbn.isdigit() and len(isbn) == 4):
                raise ValueError("El ISBN debe ser un número de 4 dígitos.")
            print("Libro agregado con éxito.")
            return Libro(titulo, autor, isbn)
        except ValueError as e:
            print(f"Error: {e}")
            print("Por favor, intenta de nuevo con un ISBN válido.")
            return Libro.agregar()  # Recursión para reintentar

    # Método prestar() para cambiar disponible a False si está disponible
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("Libro prestado con éxito.")
        else:
            print("El libro ya está prestado.")

    # Método devolver() para cambiar disponible a True si está prestado
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print("Libro devuelto con éxito.")
        else:
            print("El libro ya se encuentra presente, compruebe el número de ISBN.")

    # Método mostrar() para mostrar los datos del libro
    def mostrar(self):
        estado = "Sí" if self.disponible else "No"
        return f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}"

    # Método buscar() para encontrar un libro por ISBN
    def buscar(isbn, lista_libros):
        try:
            # Validar que ISBN sea un número de 4 dígitos
            if not (isbn.isdigit() and len(isbn) == 4):
                raise ValueError("El ISBN debe ser un número de 4 dígitos.")
            for libro in lista_libros:
                if libro.isbn == isbn:
                    print(libro.mostrar())
                    return libro
            print("Libro no encontrado.")
            return None
        except ValueError as e:
            print(f"Error: {e}")
            return None

# Lista para almacenar los objetos Libro (inventario)
biblioteca = [
    Libro("El Quijote", "Miguel de Cervantes", "1111"),
    Libro("Romeo y Julieta", "William Shakespeare", "2222"),
    Libro("Leyendas de Bécquer", "Gustavo Adolfo Bécquer", "3333"),
    Libro("El señor de los anillos", "JRR Tolkien", "4444")
]

# Función menú para interactuar con el usuario
def menu():
    while True:
        # Mostrar opciones con saltos de línea para claridad
        print("\nBienvenido al Sistema de Gestión de Biblioteca\n")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar")
        print("6. Salir")
        
        opcion = input("\nElige una opción: ")

        # Opción 1: Agregar un nuevo libro
        if opcion == "1":
            nuevo_libro = Libro.agregar()
            biblioteca.append(nuevo_libro)

        # Opción 2: Prestar un libro por ISBN
        elif opcion == "2":
            try:
                isbn = input("Ingresa el ISBN: ")
                if not (isbn.isdigit() and len(isbn) == 4):
                    raise ValueError("El ISBN debe ser un número de 4 dígitos.")
                libro = Libro.buscar(isbn, biblioteca)
                if libro:
                    libro.prestar()
            except ValueError as e:
                print(f"Error: {e}")

        # Opción 3: Devolver un libro por ISBN
        elif opcion == "3":
            try:
                isbn = input("Ingresa el ISBN: ")
                if not (isbn.isdigit() and len(isbn) == 4):
                    raise ValueError("El ISBN debe ser un número de 4 dígitos.")
                libro = Libro.buscar(isbn, biblioteca)
                if libro:
                    libro.devolver()
            except ValueError as e:
                print(f"Error: {e}")

        # Opción 4: Mostrar todos los libros
        elif opcion == "4":
            print("\nCatálogo de libros:")
            for libro in biblioteca:
                print(libro.mostrar())

        # Opción 5: Buscar un libro por ISBN
        elif opcion == "5":
            isbn = input("Ingresa el ISBN: ")
            Libro.buscar(isbn, biblioteca)

        # Opción 6: Salir del programa
        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break

        # Manejo de opción inválida
        else:
            print("Opción inválida. Por favor, selecciona una opción del 1 al 6.")

# Iniciar el programa
menu()