estudiantes = {
    
}

salir = "no"

while salir != "si":

    print("\n--- SISTEMA ACADEMICO ---")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        nombre = input("Ingrese nombre del estudiante: ")

        if nombre not in estudiantes:
            estudiantes[nombre] = {}
            print("Estudiante registrado")
        else:
            print("El estudiante ya existe")

    elif opcion == "2":

        if len(estudiantes) == 0:
            print("No hay estudiantes registrados")
        else:
            print("Lista de estudiantes:")
            for est in estudiantes:
                print(est)

    elif opcion == "3":
        salir = "si"

    else:
        print("Opcion invalida")