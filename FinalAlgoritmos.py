class Estudiante:
    def __init__(self, nombre, edad, notas=None, promedio=0):
        # Definición del contructor para la creacion de alumnos
        self.nombre = nombre
        self.edad = edad
        self.notas = []



# Agrega la nota indicada al alumno, agregandolo a su list de notas
    def AgregarNota(self, nota):
        if 0 <= nota <= 100:
            self.notas.append(nota)
            print("Calificación agregada correctamente!")
        else:
            print("La calificación indicada es inapropiada. Intente nuevamente y recuerde que las calificaciones son de 0 a 100!")

# Calcula el promedio del estudiante y lo muestra en pantalla
    def Promedio(self):
        #En caso de que el Estudiante no tenga calificaciones, se muestra un Mensaje indicandolo
        if len(self.notas) == 0:
            return "El estudiante aún no tiene calificaciones! Introduzca las calificaciones y vuelva a intentarlo."
        else:
            self.promedio = sum(self.notas) / len(self.notas)
            return self.promedio

# Muestra en pantalla la información del estudiante (nombre, edad y promedio)
    def Informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Promedio: {self.Promedio()}")

# Declaración de la clase materia, con constructor indicando el nombre de la materia y creando la lista de estudiantes vacia
class Materia:
    def __init__(self, nombre, estudiantes=None):
        self.nombre = nombre
        self.estudiantes = []

#Metodo para agregar un nuevo estudiante, preguntando la cantidad de notas a ingresar. 
    def AgregarEstudiante(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = input("Ingrese la edad del estudiante: ")

        estudiante = Estudiante(nombre, edad)
        self.estudiantes.append(estudiante)

        n = int(input("Cuántas notas quiere ingresar: "))
        for i in range(n):
            estudiante.AgregarNota(float(input("Nota: ")))
#Metodo para mostrar todos los estudiantes de una materia, utilizando un for para recorrer la lista de estudiantes e imprimiendo la info co el metodo creado anteriormente
    def MostrarEstudiantes(self):
        for est in self.estudiantes:
            est.Informacion()

    #Metodo para mostrar todos los estudiantes de una materia, utilizando un for para recorrer la lista de estudiantes e imprimiendo la info co el metodo creado anteriormente
    
#Metodo para mostrar quien fue el mejor promedio dentro de todos los estudiantes
    def MejorPromedio(self):
        if not self.estudiantes:
            print("No hay estudiantes en esta materia.")
            return

        mejorProm = max(self.estudiantes, key=lambda est: est.Promedio() if isinstance(est.Promedio(), (int, float)) else -1)

        print("El estudiante con mejor promedio es:")
        mejorProm.Informacion()

#MENU
def Menu():
    print(separador)
    print("""
    Menu Principal

    1. Crear Materia
    2. Agregar Estudiante
    3. Agregar Nota
    4. Mostrar Estudiantes
    5. Mostrar Mejor Promedio
    6. Mostrar Materias
    S. Salir
    """)
    print(separador)

#defino la funcion para buscar las paterias encontradas
def BuscarMateria(nombre, materias):
    for materia in materias:
        if materia.nombre == nombre:
            return materia
    return None


def SalidaFinal():
    print("""

            ¡Gracias por usar el

_________________¶¶¶1___¶¶¶____¶¶¶1_______________
__________________¶¶¶____¶¶¶____1¶¶1______________
___________________¶¶¶____¶¶¶____¶¶¶______________
___________________¶¶¶____¶¶¶____¶¶¶______________
__________________¶¶¶____1¶¶1___1¶¶1______________
________________1¶¶¶____¶¶¶____¶¶¶1_______________
______________1¶¶¶____¶¶¶1___¶¶¶1_________________
_____________¶¶¶1___1¶¶1___1¶¶1___________________
____________1¶¶1___1¶¶1___1¶¶1____________________
____________1¶¶1___1¶¶1___1¶¶¶____________________
_____________¶¶¶____¶¶¶1___¶¶¶1___________________
______________¶¶¶¶___1¶¶¶___1¶¶¶__________________
_______________1¶¶¶1___¶¶¶1___¶¶¶¶________________
_________________1¶¶1____¶¶¶____¶¶¶_______________
___________________¶¶1____¶¶1____¶¶1______________
___________________¶¶¶____¶¶¶____¶¶¶______________
__________________1¶¶1___1¶¶1____¶¶1______________
_________________¶¶¶____¶¶¶1___1¶¶1_______________
________________11_____111_____11_________________
__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
1¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
1¶¶¶¶¶¶¶¶¶¶¶__1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
1¶¶_______¶¶__1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
1¶¶_______¶¶__1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
1¶¶_______¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
1¶¶_______¶¶__1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
_¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
_¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
__________¶¶___1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1________
__________1¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________
____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11__________
11_____________________________________________111
1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1
__¶¶111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111¶__   
             
            Programa, Hasta Pronto!!!
      
      """)


#Ejecución
#Utilizo la variable separador para hacer mas clara la salida a nivel consola, simplemente visual!
separador = "-" * 45
materias = []
opcion = ""

print(separador)
Menu()
print(separador)


while opcion != "S":
    print(separador)
    opcion = input("Ingrese la opción deseada (número): ").upper()
    print(separador)

    if opcion == "1":
        #CREAR MATERIA
        print(separador)
        nombre_materia = input("Ingrese el nombre de la materia: ")
        print(separador)
        materias.append(Materia(nombre_materia))
        print(separador)
        print("Materia creada exitosamente.")
        print(separador)

    elif opcion == "2":
        #AGREGAR ESTUDIANTE
        print(separador)
        nomMateria = input("Ingrese el nombre de la materia: ")
        print(separador)
        materia = BuscarMateria(nomMateria, materias)
        if materia:
            print(separador)
            materia.AgregarEstudiante()
            print(separador)
        else:
            print(separador)
            print("La materia indicada no se encuentra cargada!")
            print(separador)

    elif opcion == "3":
        #AGREGAR NOTA
        print(separador)
        nomMateria = input("Ingrese el nombre de la materia: ")
        print(separador)
        materia = BuscarMateria(nomMateria, materias)
        if materia:
            print(separador)
            estudiante_nombre = input("Ingrese el nombre del estudiante: ")
            print(separador)
            estudiante = next((e for e in materia.estudiantes if e.nombre == estudiante_nombre), None)
            if estudiante:
                print(separador)
                estudiante.AgregarNota(float(input("Nota: ")))
                print(separador)
            else:
                print("Estudiante no encontrado!")
        else:
            print("La materia indicada no se encuentra cargada!")

    elif opcion == "4":
        #MOSTRAR ESTUDIANTES
        print(separador)
        nomMateria = input("Ingrese el nombre de la materia: ")
        print(separador)
        materia = BuscarMateria(nomMateria, materias)
        if materia:
            print(separador)
            materia.MostrarEstudiantes()
            print(separador)
        else:
            print("La materia indicada no se encuentra cargada!")

    elif opcion == "5":
        #MOSTRAR MEJOR PROMEDIO
        print(separador)
        nomMateria = input("Ingrese el nombre de la materia: ")
        print(separador)
        materia = BuscarMateria(nomMateria, materias)
        if materia:
            print(separador)
            materia.MejorPromedio()
            print(separador)
        else:
            print("La materia indicada no se encuentra cargada!")

    elif opcion == "6":
        #MOSTRAR MATERIAS
        if materias:
            print(separador)
            print("Materias creadas:")
            print(separador)
            for materia in materias:
                print(f"- {materia.nombre}")
        else:
            print("No hay materias creadas.")
    elif opcion == "S":
        break
    else:
        print(separador)
        print("Opción no válida. Intente nuevamente.")
        print(separador)

SalidaFinal()
