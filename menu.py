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

    return lista_matrices
            

def pide_operacion():
    print("Lista de posibles acciones:")
    print("(1) Definir matriz")
    print("(2) Listar matrices creadas")
    print("(3) Mostrar contenido de una matriz")
    print("(4) Iniciar calculadora")
    print("(5) Guardar estado de las matrices")
    print("(6) Salir")

    opcion = 0
    while True:
        try:
            opcion = int(input("[1-6]: "))
            if opcion not in range(1,7):
                raise Exception()
            
            return opcion
            
        except:
            print("Debes introducir un número del 1 al 6 (incluidos). Por favor, inténtalo de nuevo.")

def main():
    matrices = []

    print("Herramienta para realizar cálculos con matrices.")
    print("")
    print("¿Deseas cargar el estado previo de las matrices?")
    if si_o_no(False):
        matrices = carga_estado()

    salir = False
    while not salir:
        operacion = pide_operacion()

        if operacion == 1:
            print("a")
        elif operacion == 2:
            print("b")
        elif operacion == 3:
            print("c")
        elif operacion == 4:
            print("d")
        elif operacion == 5:
            print("e")
        else:
            exit(0)



if __name__ == "__main__":
    main()