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
    nombre_archivo = ""

    while nombre_archivo == "":
        nombre_archivo = input("Introduce el nombre completo del archivo: ")
        if nombre_archivo == "":
            print("Debes introducir un nombre. Por favor, inténtalo de nuevo.")
    Matriz().guardar(nombre_archivo, list(matrices.values()))
    print("Contenido guardado con éxito.")


def pide_matriz():
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
            print("Además, deben ser números enteros mayores que 0. Por favor, inténtalo de nuevo.")


def listar_matrices(matrices):
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
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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


def haz_operacion(*args):
    """
    Realiza una única operación.
    Los primeros parámetros indican los datos a operar.
    El último parámetro es un strings con el nombre de la operación a realizar (+, -, *, T, In, Nn, max, min, med).
    Entradas soportadas:
    (Matriz, Matriz, "+")
    (Matriz, Matriz, "-")
    (Matriz, "+")
    (Matriz, "-")
    (Matriz, Matriz, "*")
    (Matriz, float/int, "*")
    (float/int, Matriz, "*")
    (Matriz, "T")
    (int, "In")
    (Matriz, "max")
    (Matriz, "min")
    (Matriz, "med")
    """
    if len(args) == 2:
        operacion = args[1].lower()
        dato = args[0]
        if type(dato) == Matriz:
            if operacion == "+":
                return dato
            elif operacion == "-":
                return dato*(-1)
            elif operacion == "t":
                return dato.traspuesta()
            elif operacion == "max":
                return dato.mayor()
            elif operacion == "min":
                return dato.menor()
            elif operacion == "med":
                return dato.media()
        elif type(dato) == int and operacion == "in":
            return Matriz(dato, tipo_matriz='identidad')

    elif len(args) == 3:
        operacion = args[2].lower()
        dato1 = args[0]
        dato2 = args[1]
        if operacion == "*":
            if type(dato1) in [int, float]:
                return dato2*dato1
            else:
                return dato1*dato2
        elif type(dato1) == type(dato2) == Matriz:
            if operacion == "+":
                return dato1+dato2
            elif operacion == "-":
                return dato1-dato2
    
    raise Exception("Operación no soportada.")
    

def calcula(matrices, nombre_inventado):
    print()
    print("Calculadora iniciada.")
    print("Usa 'h' para obtener ayuda.")

    opcion = 0
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
                print("'c A' para imprimir las características de la matriz 'A'.")####
                print("'A + B', siendo 'A' y 'B' matrices con las mismas dimensiones.")
                print("'A - B', siendo 'A' y 'B' matrices con las mismas dimensiones.")
                print("'A * B', siendo 'A' y 'B' matrices, y teniendo 'A' las mismas columnas que filas tiene 'B'.")
                print("'A * a' o 'a * A', siendo 'A' una matriz y 'a' un escalar.")
                print("'T(A)' para obtener la traspuesta de la matriz 'A'.")
                print("'-A' para obtener la matriz opuesta de la matriz 'A'.")
                print("'InX' para obtener la matriz identidad de orden X. Ejemplo: 'In3'.")
                #print("'Nn3x2' para obtener la matriz nula de 3 filas y 2 columnas.")
                print("'max(A)' para obtener el valor máximo de los elementos de la matriz 'A'.")
                print("'min(A)' para obtener el valor mínimo de los elementos de la matriz 'A'.")
                print("'med(A)' para obtener la media de los valres de los elementos de la matriz 'A'.")
                #print("Todas las operaciones entre matrices se pueden encadenar en una sola instrucción.")
                #print("Se pueden usar los paréntesis para especificar el orden de las operaciones.")
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
                if matriz.es_diagonal(): print("Es diagonal.")
                if matriz.es_magica(): print("Es mágica.")
            else:
                
                operacion = operacion.replace(" ", "")
                nueva_matriz = None
                guardar = False
                if operacion[0] == "=":
                    operacion = operacion[1:]
                    guardar = True

                try:
                    nueva_matriz = matrices[operacion]

                except:
                    # -A, +A
                    if operacion[0] == "-" or operacion[0] == "+":
                        nueva_matriz = haz_operacion(matrices[operacion[1:]], operacion[0])
                    # A-B
                    elif len(operacion.split("-")) == 2:
                        matriz1, matriz2 = operacion.split("-")
                        nueva_matriz = haz_operacion(matrices[matriz1], matrices[matriz2], "-")
                    # A+B
                    elif len(operacion.split("+")) == 2:
                        matriz1, matriz2 = operacion.split("+")
                        nueva_matriz = haz_operacion(matrices[matriz1], matrices[matriz2], "+")
                    # A*B, A*a, a*A
                    elif len(operacion.split("*")) == 2:
                        dato1, dato2 = operacion.split("*")
                        # a*A
                        if str.isnumeric(dato1):
                            nueva_matriz = haz_operacion(int(dato1), matrices[dato2], "*")
                        # A*a
                        elif str.isnumeric(dato2):
                            nueva_matriz = haz_operacion(matrices[dato1], int(dato2), "*")
                        # A*B
                        else:
                            nueva_matriz = haz_operacion(matrices[dato1], matrices[dato2], "*")

                    # In*
                    elif operacion[:2].lower() == "in":
                        nueva_matriz = haz_operacion(int(operacion[2:]), "In")
                    # max(A), min(A), mid(A)
                    elif operacion[3] == "(" and operacion[-1] == ")":
                        nueva_matriz = haz_operacion(matrices[operacion[4:-1]], operacion[:3])
                    # T(A)
                    elif operacion[:2].lower() == "t(" and operacion[-1] == ")":
                        nueva_matriz = haz_operacion(matrices[operacion[2:-1]], "T")

                # Si el resultado es un número
                if type(nueva_matriz) in [float, int]:
                    print(nueva_matriz)
                # Si el resultado es una matriz
                elif type(nueva_matriz) == Matriz:
                    nueva_matriz.imprime()
                    if guardar:
                        nombre_inventado = nuevo_nombre(nombre_inventado)
                        matrices[nombre_inventado] = nueva_matriz
                        print(f"Salida guardada en la matriz {nombre_inventado}.")
        
        except:
            print("Error: Fallo a la hora de intentar hacer la operación. Usa 'h' para obtener ayuda.")
            print()

    return matrices, nombre_inventado



def pide_operacion_menu():
    opcion = 0
    while True:
        print()
        print("Lista de posibles acciones:")
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
    matrices = {}
    nombre_inventado = ""

    print("Herramienta para realizar cálculos con matrices.")
    print()
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
            print("a")

        # Mostrar todas las matrices y su contenido
        elif operacion == 3:
            listar_matrices(matrices)

        # Modificar contenido de una matriz
        elif operacion == 4:
            print("c")

        # Iniciar calculadora
        elif operacion == 5:
            matrices, nombre_inventado = calcula(matrices, nombre_inventado)

        # Guardar estado de las matrices
        elif operacion == 6:
            guarda_estado(matrices)

        # Salir
        else:
            exit(0)



if __name__ == "__main__":
    main()


"""
TODO:
2.a
2.b
5.a
5.b
5.c
14.
"""