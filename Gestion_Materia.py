import os


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def imprimir_menu():
    print("Base de datos 1:")
    print("1. Ingresar estudiante")
    print("2. Mostrar estudiantes aprobados")
    print("3. Mostrar estudiantes desaprobados")
    print("4. Salir")


def obtener_opcion():
    opcion = input("Ingrese una opción: ")
    while opcion not in ["1", "2", "3", "4"]:
        opcion = input("Opción inválida. Ingrese una opción nuevamente: ")
    return opcion


def agregar():
    variable = []
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese Apellido: ")
    nombre_completo = nombre + " " + apellido
    variable.append(nombre_completo)
    dni(variable)


def dni(a):
    variable = a
    dni = input("Ingrese DNI: ")
    archivo = open("datos_alumnos.csv", "r")
    _ = archivo.readline()
    for i in archivo.readlines():
        if dni in i:
            while dni in i:
                print("Estudiante ya existente:")
                dni = input("Ingrese DNI: ")
    else:
        variable.append(dni)
        agregar_notas(variable)
    archivo.close()


def agregar_notas(a):
    variable = a
    promedio = float(0)
    for i in range(6):
        numero = float(input(f"Ingrese la nota {i+1}:  "))
        promedio = promedio + numero
        archivo = open("agenda.csv", "a")
        variable.append(str(numero))
    variable.append(str(promedio / 4))
    if promedio / 4 >= 6:
        variable.append(str("Aprobado"))
    else:
        variable.append(str("Desaprobado"))
    archivo = open("datos_alumnos.csv", "a")
    archivo.write(";".join(variable) + "\n")
    archivo.close()


def ver_estudiantes_aprobados():
    print("ALUMNOS APROBADOS:\n\n\n")
    archivo = open("datos_alumnos.csv", "r")
    _ = archivo.readline()
    notafinal = []
    aprobados = 0
    for i in archivo.readlines():
        notafinal = i.split(";")
        if float(notafinal[8]) >= 6:
            aprobados = aprobados + 1
    archivo.close
    archivo = open("datos_alumnos.csv", "r")
    _ = archivo.readline()
    if aprobados > 0:
        for i in archivo.readlines():
            notafinal = i.split(";")
            if float(notafinal[8]) >= 6:
                print(i)
    else:
        print("No hay aprobados\n\n\n")


def ver_estudiantes_desaprobados():
    print("ALUMNOS DESAPROBADOS:\n\n\n")
    archivo = open("datos_alumnos.csv", "r")
    _ = archivo.readline()
    notafinal = []
    aprobados = 0
    for i in archivo.readlines():
        notafinal = i.split(";")
        if float(notafinal[8]) < 6:
            aprobados = aprobados + 1
    archivo.close()
    archivo = open("datos_alumnos.csv", "r")
    _ = archivo.readline()
    if aprobados > 0:
        for i in archivo.readlines():
            notafinal = i.split(";")
            if float(notafinal[8]) < 6:
                print(i)
    else:
        print("No hay desaprobados\n\n\n")
    archivo.close()


while True:
    imprimir_menu()
    opcion = obtener_opcion()
    if opcion == "1":
        agregar()
    elif opcion == "2":
        ver_estudiantes_aprobados()
    elif opcion == "3":
        ver_estudiantes_desaprobados()
    elif opcion == "4":
        print("Programa finalizado")
        break
    print("1: Volver al menú \n2: Salir")
    respuesta = input()
    while respuesta not in ["1", "2"]:
        print("Opción no válida, reintente")
        respuesta = input()
    if respuesta == "2":
        print("Programa finalizado")
        break
    limpiar_pantalla()
