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
    (int, "Nn")
    (Matriz, "max")
    (Matriz, "min")
    (Matriz, "med")
    """

    if len(args) not in [2, 3]:
        raise Exception("Operación no soportada.")

    if len(args) == 2:
        pass
    elif len(args) == 3:
        pass
        

def calcula(matrices):
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
                print("'l A', siendo 'A' el nombre de la matriz, para mostrar el estado de la matriz.")
                print("'d A' para imprimir las dimensiones de la matriz A")
                print("'c A' para imprimir las características de la matriz A")
                print("'A + B', siendo 'A' y 'B' matrices con las mismas dimensiones.")
                print("'A - B', siendo 'A' y 'B' matrices con las mismas dimensiones.")
                print("'A * B', siendo 'A' y 'B' matrices, y teniendo 'A' las mismas columnas que filas tiene 'B'.")
                print("'A * a' o 'a * A', siendo 'A' una matriz y 'a' un escalar.")
                print("'T(A)' para obtener la traspuesda de la matriz 'A'")
                print("'-A' para obtener la matriz opuesta de la matriz 'A'")
                print("'In3' para obtener la matriz identidad de orden 3")
                print("'Nn3' para obtener la matriz nula de orden 3")
                print("'max(A)' para obtener el valor máximo de los elementos")
                print("'min(A)' para obtener el valor mínimo de los elementos")
                print("'med(A)' para obtener la media de los valres de los elementos")
                #print("Todas las operaciones entre matrices se pueden encadenar en una sola instrucción.")
                #print("Se pueden usar los paréntesis para especificar el orden de las operaciones.")
                #print("'_ = <operación>' para guardar el resultado de la operación en una nueva matriz.")
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
                print("Filas, columnas:",matrices[nombre_matriz].dimensiones())
            #elif operacion[0] == "c":
            else:
                operacion = operacion.replace(" ", "")

                
                    
        except:
            print("Error: Operación no válida. Usa 'h' para obtener ayuda.")
            print()



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
            calcula(matrices)

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