estudiantes = {}

salir = "no"

while salir != "si":

    print("\n--- SISTEMA DE REGISTRO ACADEMICO ---")
    print("1 Registrar estudiante")
    print("2 Registrar materia y nota")
    print("3 Mostrar información de estudiantes")
    print("4 Calcular promedios")
    print("5 Mejor estudiante")
    print("6 Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre not in estudiantes:
            estudiantes[nombre] = {}
            print("Estudiante registrado")
        else:
            print("El estudiante ya existe")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre in estudiantes:
            continuar = "si"
            while continuar == "si":
                materia = input("Ingrese la materia: ")
                try:
                    nota = float(input("Ingrese la nota: "))
                    estudiantes[nombre][materia] = nota
                    print("Materia y nota registradas")
                except ValueError:
                    print("La nota debe ser un número")

                continuar = input("¿Desea ingresar otra materia? (si/no): ").lower()
        else:
            print("El estudiante no existe")

    elif opcion == "3":
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados")
        else:
            for est in estudiantes:
                print("\nEstudiante:", est)
                if len(estudiantes[est]) == 0:
                    print("No tiene materias registradas")
                else:
                    for mat, nota in estudiantes[est].items():
                        print(mat, "-", nota)

    elif opcion == "4":
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados")
        else:
            for est in estudiantes:
                if len(estudiantes[est]) > 0:
                    promedio = sum(estudiantes[est].values()) / len(estudiantes[est])
                    print(est, "Promedio:", promedio)
                else:
                    print(est, "No tiene notas")

    elif opcion == "5":
        mejor = ""
        mejor_promedio = 0
        for est in estudiantes:
            if len(estudiantes[est]) > 0:
                promedio = sum(estudiantes[est].values()) / len(estudiantes[est])
                if promedio > mejor_promedio:
                    mejor_promedio = promedio
                    mejor = est
        if mejor != "":
            print("Mejor estudiante:", mejor, "con promedio:", mejor_promedio)
        else:
            print("No hay datos suficientes")

    elif opcion == "6":
        salir = "si"

    else:
        print("Opción inválida")