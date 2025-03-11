# Empezamos definiendo la clase principal de este ejercicio «libro» con su constructor.
class Libro(): 
    # se debe ser coherente con la nomenclatura del enunciado.
    def __init__(self, titulo, autor, isbn, disponible=True): 
        #aquí declaro los argumentos que tendrá esta clase
        self.titulo = titulo 
        # dejaré los argumentos de forma que me permita añadirlos después y para que sea un constructor con parámetros
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
    # continuamos declarando el resto de métodos según el enunciado
    # Se implementa un error para que salte cuando el ISBN  introducido no sean 4 dígitos.
    def agregar():
            try:
                titulo=input('Introduzca el título del libro que desee añadir')
                autor = input('Introduzca su autor')
                isbn = input('Introduzca el ISBN')
                if not (isbn.isdigit() and len(isbn)==4): #con esta comprobación, lanzamos el error de incumplirse las condiciones
                     raise ValueError("ERROR, el ISBN deben ser 4 dígitos")
                print('¡Libro agregado con éxito!')
                return Libro(titulo,autor,isbn)
            except ValueError as error: #si se dispara el error, se muestra este texto y se vuelve atrás
                 print(f'Error: {error}')
                 print('Recuerde que un ISBN se compone de CUATRO dígitos') #intento aconsejar al usuario
                 return Libro.agregar() # Aquí se usa la recursividad hasta que el usuario siga las instrucciones
    # El método prestar debe cambiar el estado disponible a False si de un libro en la biblioteca.    
    def prestar(self):
            if self.disponible == True:
                self.disponible == False
                print('¡Libro prestado con éxito, disfrute!')
            else:
                 print('Lo sentimos, el libro no está disponible en esta biblioteca,')
    # Este método debe cambiar a True si el libro estaba prestado y se entrega a la biblioteca.   
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print('¡Gracias por devolver el libro a tiempo!')
        else:
            print('El libro ya se encuentra presente, compruebe el número de ISBN')

    def mostrar():
        pass
    def buscar():
        # Esta función se puede resolver tanto por búsqueda binaria como búsqueda común.
        input('Introduzca el ISBN del libro que desea buscar')
        pass
# Ahora voy a crear un menú principal, de forma que sea una función que luego pueda meter en un bucle
 def menu():
     while True:
      print('Seleccione una opción del 1 al 6')
      print('1. Agregar libro al listado general')    
      print('2. Realizar el préstamo de un libro disponible en la biblioteca')
      print('3. Devolver un libro a la biblioteca que usted posee')
      print('4. Mostrar el catálogo general de libros disponibles en la biblioteca')
      print('5. Buscar por ISBN de cuatro números un ejemplar en la biblioteca')
      print('6. Salir del sistema')
# voy a crear unos objetos por defecto, para que no partamos de un registro de libros vacío
quijote = Libro('El Quijote', 'Miguel de Cervantes', '1111')
romeo = Libro('Romeo y Julieta', 'William Shakespeakre', '2222')
leyendas =Libro('Leyendas de Bécquer','Gustavo Adolfo Bécquer', '3333')
anillos = Libro('El señor de los anillos', 'JRR Tolkien', '4444')
print('¡Bienvenido al sistema de la biblioteca de Francisco! ¿En qué puedo ayudarle?')



