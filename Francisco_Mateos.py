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
    #continuamos declarando el resto de métodos
    def agregar():
            titulo=input('Introduzca el título del libro que desee añadir')
            autor = input('Introduzca su autor')
            isbn = input('Introduzca el ISBN')
            return Libro(titulo,autor,isbn)
        
    def prestar():
            if self.disponible == True:
        
    def devolver():
        if Libro.disponible == False:
            Libro.disponible == True
        else print('El libro ya se encuentra presente, compruebe el número de ISBN')
        pass
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



