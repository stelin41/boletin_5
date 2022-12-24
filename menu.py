"""
Autores:
    - José Romero Conde
    - Stevan Lino Gartz

Propósito:
    Con este programa un usuario puede realizar operaciones con matrices,
    haciendo uso de la clase Matriz.

"""

from matrices import Matriz


def si_o_no(respuesta_por_defecto):
    """
    Le pide al usuario confirmar o negar una acción.
    La función recibe por parámetro la respuesta por defecto que se dará si
    el usuario no especifica una acción (solo presiona ENTER).
    La función devuelve True si la respuesta es afirmativa, y un False
    si la repuesta es negativa.
    """

    while True:
        if respuesta_por_defecto:
            respuesta = input("[S/n]: ")

        else:
            respuesta = input("[s/N]: ")


        if respuesta == "":
            return respuesta_por_defecto

        elif respuesta.lower() in ["s", "si", "sí", "y", "yes"]:
            return True

        elif respuesta.lower() in ["n", "no"]:
            return False

        else:
            print("Error: Respuesta no reconocida. Debes introducir \"Sí\" o \"No\"")


def carga_estado():
    """
    Pide al usuario un archivo y devuelve las matrices almacenadas en él tras cargarlo.
    """

    archivo_cargado = False
    lista_matrices = []
    while not archivo_cargado:
        nombre_archivo = input("Introduce el nombre completo del archivo: ")
        try:
            lista_matrices = Matriz().cargar(nombre_archivo)
            archivo_cargado = True

        except:
            print("El archivo", nombre_archivo, "no esixte o no es válido. Por favor, inténtalo de nuevo.")

    print("Contenido cargado con éxito.")
    return lista_matrices


def guarda_estado(matrices):
    """
    Guarda el estado de las matrices que se pasen por parámetro en un archivo que se le pide al usuario.
    """

    nombre_archivo = ""

    while nombre_archivo == "":
        nombre_archivo = input("Introduce el nombre completo del archivo: ")
        if nombre_archivo == "":
            print("Debes introducir un nombre. Por favor, inténtalo de nuevo.")

    Matriz().guardar(nombre_archivo, list(matrices.values()))
    print("Contenido guardado con éxito.")


def pide_matriz():
    """
    Pide al usuario las dimensiones de una matriz y su contenido.
    La función devuelve la matriz creada.
    """

    while True:
        dimensiones = input("Introduce el número de filas y columnas de la matriz, separados por un espacio: ")
        try:
            filas, columnas = dimensiones.split(" ")
            filas = int(filas)
            columnas = int(columnas)
            if filas < 1 or columnas < 1:
                raise Exception()

            nueva_matriz = Matriz(filas, columnas)
            nueva_matriz.pide_matriz()
            print("Matriz creada con éxito.")
            return nueva_matriz

        except:
            print("Error. Debes introducir los valores de la forma: <filas> <columnas>")
            print("Por favor, inténtalo de nuevo.")


def listar_matrices(matrices):
    """
    Imprime en pantalla las matrices que se pasaron como parámetro almacenadas en un diccionario.
    """

    for k in matrices.keys():
        print()
        print(f"{k}:")
        matrices[k].imprime()


def nuevo_nombre(ultimo_nombre):
    """
    Genera nuevos nombres para las matrices.
    Ejemplos:
    Entrada - Salida
    A -------> B
    Z -------> AA
    AA ------> AB
    """

    def  _incrementa(letra):
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if letra == "Z":
            return "A"

        else:
            indice = alfabeto.find(letra)
            return alfabeto[indice+1]

    if ultimo_nombre == "":
        return "A"

    else:
        nuevo_nombre = ""

        # Si esto ocurre entonces es necesario crear una nueva letra
        if len(set(ultimo_nombre)) == 1 and list(set(ultimo_nombre))[0] == "Z":
            nuevo_nombre = "A"*(len(ultimo_nombre)+1)

        else:
            ultimo_indice = 0
            for i in range(len(ultimo_nombre)-1, -1, -1):
                ultimo_indice = i
                nueva_letra = _incrementa(ultimo_nombre[i])
                nuevo_nombre = nueva_letra + nuevo_nombre

                # Si esto no se cumple entonces "se lleva una", por lo que deve seguir incrementando las siguientes letras
                if nueva_letra != "A":
                    break
            
            nuevo_nombre = ultimo_nombre[:i] + nuevo_nombre

        return nuevo_nombre


def pide_escoger_matriz(matrices):
    """
    Le pide al usuario seleccionar una matriz de las que están disponibles en el diccionario
    de matrices que se pasa por parámetro, y devuelve un string con el nombre de la matriz.
    Nota importante: si el usuario decide cancelar la operación, se devolverá un string vacío.
    """

    matriz_escogida = ""
    nombres_matrices = list(matrices.keys())
    if len(matrices) == 0:
        print("No hay ninguna matriz declarada.")
        return matrices, ''

    while matriz_escogida not in nombres_matrices and matriz_escogida != "q":
        matriz_escogida = input("\nIntroduce el nombre de la matriz (o usa 'q' para cancelar): ")
        if matriz_escogida not in nombres_matrices and matriz_escogida != "q":
            print(f"Matriz {matriz_escogida} no encontrada.")
            print(f"Estas son las matrices disponibles:")
            print(nombres_matrices)
            print("Por favor, inténtalo de nuevo.")
    
    if matriz_escogida == "q":
        matriz_escogida = ''

    return matriz_escogida


def pide_eliminar_matriz(matrices):
    """
    Le pide al usuario eliminar una matriz almacenada en el diccionario de matrices que se pasa por parámetro a la función.
    La función devuelve un nuevo diccionario sin la matriz eliminada por el usuario, y el nombre de la última matriz.
    """

    eliminar = pide_escoger_matriz(matrices)
    nombres_matrices = list(matrices.keys())
    # Para conservar la organización de las matrices, se sobreescribe la matriz a eliminar
    # con la matriz contigua a esta (si esixte), y luego esa otra matriz se vuelve a sobreescribir
    # con la siguiente, y el proceso se repite hasta llegar a la última matriz. Finalmete se elimina
    # la última matriz (que estará repetida).
    if eliminar != "":
        matriz_a_desplazar = eliminar
        matriz_desplazada = eliminar
        while matriz_a_desplazar != nombres_matrices[-1]:
            matriz_desplazada = matriz_a_desplazar
            matriz_a_desplazar = nuevo_nombre(matriz_a_desplazar)
            matrices[matriz_desplazada] = matrices[matriz_a_desplazar]

        del matrices[matriz_a_desplazar]
        print("\nMatriz eliminada con éxito.")

    if len(matrices) > 1:
        return matrices, nombres_matrices[-2]

    else:
        return matrices, nombres_matrices[-1]


def pide_cambiar_matriz(matrices):
    """
    Le pide al usuario escoger una matriz de las que se pasaron por parámetro dentro de un diccionario.
    Luego pide especificar un elemento y un nuevo valor para ese elemento.
    Devuelve el diccionario de matrices con el elemento modificado.
    """

    nombre_matriz = pide_escoger_matriz(matrices)
    matriz_a_cambiar = matrices[nombre_matriz]

    if matriz_a_cambiar != "":
        matriz_a_cambiar.imprime()
        fila = 1
        columna = 1
        valor = matriz_a_cambiar[fila][columna]
        while True:
            try:
                posicion = input("\nIntroduce la fila y la columna en la que está el elemento, separado por un espacio: ").split(" ")
                fila = int(posicion[0])
                columna = int(posicion[1])
                _ = matriz_a_cambiar[fila][columna]
                while True:
                    try:
                        valor = float(input("Introduce el valor deseado: "))
                        break

                    except:
                        print("Error: Debes introducir un número.")
                        print("Por favor, inténtalo de nuevo.")
                    
                break

            except:
                print("Error. Debes introducir la posición de un elemento dentro de la matriz, de la forma: <fila> <columna>")
                print("Por favor, inténtalo de nuevo.")
        
        matrices[nombre_matriz][fila][columna] = valor
        print("\nElemento modificado correctamente.")

    return matrices


def haz_operacion(operacion, matrices):
    """
    Realiza la operación matemática especificada (véase la función calculadora).
    Recibe por parámetro una única operación en forma de string, y la lista de matrices en forma de diccionario.
    Devuelve el resultado de la operación y si se pide guardar el resultado.
    Este resultado puede ser de tipo float, int, Matriz o None si la operación no es válida.
    Operaciones soportadas: "A", "-A", "+A", "A-B", "A+B", "A*B", "A*a", "a*A", "In<orden>", "max(A)", "min(A)", "med(A)".
    """

    operacion = operacion.replace(" ", "")
    nueva_matriz = None
    guardar = False
    if operacion[0] == "=":
        operacion = operacion[1:]
        guardar = True

    try:
        # -A
        if operacion[0] == "-":
            nueva_matriz = matrices[operacion[1:]].opuesta()

        # +A
        elif operacion[0] == "+":
            nueva_matriz = matrices[operacion[1:]]

        # A-B
        elif len(operacion.split("-")) == 2:
            matriz1, matriz2 = operacion.split("-")
            nueva_matriz = matrices[matriz1] - matrices[matriz2]

        # A+B
        elif len(operacion.split("+")) == 2:
            matriz1, matriz2 = operacion.split("+")
            nueva_matriz = matrices[matriz1] + matrices[matriz2]

        # A*B, A*a, a*A
        elif len(operacion.split("*")) == 2:
            dato1, dato2 = operacion.split("*")
            # a*A
            if str.isnumeric(dato1):
                nueva_matriz = matrices[dato2] * float(dato1) 
            # A*a
            elif str.isnumeric(dato2):
                nueva_matriz = matrices[dato1] * float(dato2)
            # A*B
            else:
                nueva_matriz = matrices[dato1] * matrices[dato2]

        # In<orden>
        elif operacion[:2].lower() == "in":
            nueva_matriz = Matriz(int(operacion[2:]), tipo_matriz='identidad')

        # max(A), min(A), mid(A)
        elif len(operacion) > 5 and operacion[3] == "(" and operacion[-1] == ")":
            funcion = operacion[:3]
            matriz = matrices[operacion[4:-1]]
            if funcion == "max":
                nueva_matriz = matriz.mayor()
            elif funcion == "min":
                nueva_matriz = matriz.menor()
            elif funcion == "med":
                nueva_matriz = matriz.media()

        # T(A)
        elif len(operacion) > 3 and operacion[:2].lower() == "t(" and operacion[-1] == ")":
            nueva_matriz = matrices[operacion[2:-1]].traspuesta()

        # A
        else:
            nueva_matriz = matrices[operacion]

    except:
        nueva_matriz = None
        guardar = False

    # Si la matriz es 1x1 devuelve el único elemento de la matriz.
    if type(nueva_matriz) == Matriz and nueva_matriz.dimension() == (1,1):
        nueva_matriz = nueva_matriz[1][1]

    return nueva_matriz, guardar
    

def calculadora(matrices):
    """
    Inicia una calculadora de matrices. Recibe por parámetro un diccionario de matrices y
    tras haber hecho los cálculos devuelve un nuevo diccionario de matrices y el nombre de la última matriz.
    """

    print("\nCalculadora iniciada.")
    print("Usa 'h' para obtener ayuda.")

    nombre_inventado = list(matrices.keys())[-1]
    while True:
        operacion = input(">> ")
        try:
            if operacion == "":
                continue

            elif operacion == "h":
                print("Lista de posibles operaciones:")
                print("'h' para mostrar este texto.")
                print("'q' para salir de la calculadora y volver al menú.")
                print("'l' para mostrar todas las matrices y su estado.")
                print("'l A' o 'A', siendo 'A' el nombre de la matriz, para mostrar el estado de la matriz.")
                print("'d A' para imprimir las dimensiones de la matriz 'A'")
                print("'c A' para imprimir las características de la matriz 'A'.")
                print("'A + B', siendo 'A' y 'B' matrices con las mismas dimensiones.")
                print("'A - B', siendo 'A' y 'B' matrices con las mismas dimensiones.")
                print("'A * B', siendo 'A' y 'B' matrices, y teniendo 'A' las mismas columnas que filas tiene 'B'.")
                print("'A * a' o 'a * A', siendo 'A' una matriz y 'a' un escalar.")
                print("'T(A)' para obtener la traspuesta de la matriz 'A'.")
                print("'-A' para obtener la matriz opuesta de la matriz 'A'.")
                print("'In<orden>' para obtener la matriz identidad de orden <orden>. Ejemplo: 'In3'.")
                print("'max(A)' para obtener el valor máximo de los elementos de la matriz 'A'.")
                print("'min(A)' para obtener el valor mínimo de los elementos de la matriz 'A'.")
                print("'med(A)' para obtener la media de los valres de los elementos de la matriz 'A'.")
                print("'=<operación>' para guardar el resultado de la operación en una nueva matriz.")
                print("    Nota: Si el resultado de la operación es un número el resultado no será guardado.")

            elif operacion == "q":
                break

            elif operacion[0] == "l":
                if operacion == "l":
                    listar_matrices(matrices)

                else:
                    nombre_matriz = operacion.split(" ")[1]
                    listar_matrices({nombre_matriz:matrices[nombre_matriz]})

            elif operacion[0] == "d":
                nombre_matriz = operacion.split(" ")[1]
                print("Filas, columnas:",matrices[nombre_matriz].dimension())

            elif operacion[0] == "c":
                nombre_matriz = operacion.split(" ")[1]
                matriz = matrices[nombre_matriz]
                print("La matriz",nombre_matriz)
                matriz.imprime_tipo()

            else:
                resultado, guardar = haz_operacion(operacion, matrices)

                # Si el resultado es un número
                if type(resultado) in [float, int]:
                    print(resultado)

                # Si el resultado es una matriz
                elif type(resultado) == Matriz:
                    resultado.imprime()
                    if guardar:
                        nombre_inventado = nuevo_nombre(nombre_inventado)
                        matrices[nombre_inventado] = resultado
                        print(f"Salida guardada en la matriz {nombre_inventado}.")

                else:
                    print("Error: Fallo a la hora de intentar hacer la operación. Usa 'h' para obtener ayuda.")
        
        except:
            print("Error: Fallo a la hora de intentar hacer la operación. Usa 'h' para obtener ayuda.\n")

    return matrices, nombre_inventado


def pide_operacion_menu():
    """
    Le pide al usuario una acción de las disponibles en el menú.
    Devuelve el número de la acción especificada por el usuario.
    """

    opcion = 0
    while True:
        print("\nLista de posibles acciones:")
        print("(1) Definir matriz")
        print("(2) Eliminar matriz")
        print("(3) Listar matrices")
        print("(4) Modificar contenido de una matriz")
        print("(5) Iniciar calculadora")
        print("(6) Guardar estado de las matrices")
        print("(7) Salir")
        opcion = input("[1-7]: ")
        try:
            opcion = int(opcion)
            if opcion not in range(1,8):
                raise Exception()
            
            return opcion
            
        except:
            print("Debes introducir un número del 1 al 7 (incluidos). Por favor, inténtalo de nuevo.")


def main():
    """
    Función principal que dá inicio al programa.
    """

    matrices = {}
    nombre_inventado = ""

    print("Herramienta para realizar cálculos con matrices.\n")
    print("¿Deseas cargar un estado previo de las matrices?")
    if si_o_no(False):
        matrices_cargadas = carga_estado()
        for matriz in matrices_cargadas:
            nombre_inventado = nuevo_nombre(nombre_inventado)
            matrices[nombre_inventado] = matriz

    while True:
        operacion = pide_operacion_menu()

        # Crear nueva matriz
        if operacion == 1:
            nueva_matriz = pide_matriz()
            nombre_inventado = nuevo_nombre(nombre_inventado)
            matrices[nombre_inventado] = nueva_matriz
            print(f"Matriz \"{nombre_inventado}\" creada con éxito.")

        # Eliminar una matriz
        elif operacion == 2:
            matrices, nombre_inventado = pide_eliminar_matriz(matrices)

        # Mostrar todas las matrices y su contenido
        elif operacion == 3:
            listar_matrices(matrices)

        # Modificar contenido de una matriz
        elif operacion == 4:
            matrices = pide_cambiar_matriz(matrices)

        # Iniciar calculadora
        elif operacion == 5:
            matrices, nombre_inventado = calculadora(matrices)

        # Guardar estado de las matrices
        elif operacion == 6:
            guarda_estado(matrices)

        # Salir
        else:
            exit(0)



if __name__ == "__main__":
    main()