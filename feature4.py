estudiantes = {}

salir = "no"

while salir != "si":

    print("\n--- ANALISIS DE RESULTADOS ---")
    print("1 Registrar estudiante")
    print("2 Registrar materia y nota")
    print("3 Calcular promedios")
    print("4 Mejor estudiante")
    print("5 Salir")

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

        for est in estudiantes:

            suma = 0
            contador = 0

            for mat in estudiantes[est]:

                suma = suma + estudiantes[est][mat]
                contador = contador + 1

            if contador > 0:

                promedio = suma / contador
                print(est, "Promedio:", promedio)

            else:

                print(est, "No tiene notas")

    elif opcion == "4":

        mejor = ""
        mejor_promedio = 0

        for est in estudiantes:

            suma = 0
            contador = 0

            for mat in estudiantes[est]:

                suma = suma + estudiantes[est][mat]
                contador = contador + 1

            if contador > 0:

                promedio = suma / contador

                if promedio > mejor_promedio:

                    mejor_promedio = promedio
                    mejor = est

        if mejor != "":
            print("Mejor estudiante:", mejor)
            print("Promedio:", mejor_promedio)

        else:
            print("No hay datos")

    elif opcion == "5":

        salir = "si"

    else:
        print("Opcion invalida")