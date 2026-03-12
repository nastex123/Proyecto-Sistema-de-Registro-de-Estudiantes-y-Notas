estudiantes = {}

salir = "no"

while salir != "si":

    print("\n--- INFORMACION ACADEMICA ---")
    print("1 Registrar estudiante")
    print("2 Registrar materia y nota")
    print("3 Mostrar informacion de estudiantes")
    print("4 Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        nombre = input("Ingrese el nombre del estudiante: ")

        if nombre not in estudiantes:
            estudiantes[nombre] = {}

    elif opcion == "2":

        nombre = input("Ingrese el nombre del estudiante: ")

        if nombre in estudiantes:

            materia = input("Ingrese la materia: ")
            nota = float(input("Ingrese la nota: "))

            estudiantes[nombre][materia] = nota

        else:
            print("Estudiante no existe")

    elif opcion == "3":

        if len(estudiantes) == 0:
            print("No hay estudiantes")

        else:

            for est in estudiantes:

                print("\nEstudiante:", est)

                if len(estudiantes[est]) == 0:
                    print("No tiene materias")

                else:

                    for mat in estudiantes[est]:
                        print(mat, "-", estudiantes[est][mat])

    elif opcion == "4":

        salir = "si"

    else:
        print("Opcion invalida")