estudiantes = {}

salir = "no"

while salir != "si":

    print("\n--- MATERIAS Y NOTAS ---")
    print("1 Registrar estudiante")
    print("2 Registrar materia y nota")
    print("3 Mostrar estudiantes")
    print("4 Salir")

    opcion = input("Seleccione una opcion: ")

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

            materia = input("Ingrese la materia: ")
            nota = float(input("Ingrese la nota: "))

            estudiantes[nombre][materia] = nota

            print("Materia y nota registradas")

        else:
            print("El estudiante no existe")

    elif opcion == "3":

        for est in estudiantes:
            print(est)

    elif opcion == "4":

        salir = "si"

    else:
        print("Opcion invalida")