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


"""
def calculadora():
    print()
    print("Calculadora iniciada.")
    print("Escribe h para obtener ayuda.")

    opcion = 0
    while True:
        operacion = input(">> ")
        try:
            if operacion == "h":
                print()
            elif operacion == ""
            
        except:
            print("Error: Operación no válida. Usa h para obtener ayuda.")
            print()
"""


def pide_operacion_menu():
    opcion = 0
    while True:
        print()
        print("Lista de posibles acciones:")
        print("(1) Definir matriz")
        print("(2) Listar matrices creadas")
        print("(3) Modificar contenido de una matriz")
        print("(4) Iniciar calculadora")
        print("(5) Guardar estado de las matrices")
        print("(6) Salir")
        opcion = input("[1-6]: ")
        try:
            opcion = int(opcion)
            if opcion not in range(1,7):
                raise Exception()
            
            return opcion
            
        except:
            print("Debes introducir un número del 1 al 6 (incluidos). Por favor, inténtalo de nuevo.")


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

        # Mostrar todas las matrices y su contenido
        elif operacion == 2:
            listar_matrices(matrices)

        # Modificar contenido de una matriz
        elif operacion == 3:
            print("c")

        # Iniciar calculadora
        elif operacion == 4:
            print("d")

        # Guardar estado de las matrices
        elif operacion == 5:
            guarda_estado(matrices)

        # Salir
        else:
            exit(0)



if __name__ == "__main__":
    main()