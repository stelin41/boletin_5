#
#   Autores:
#    - 
#    - Stevan Lino Gartz
#
#   Propósito:
#    Esta librería se puede usar para realizar operaciones con matrices.
#

class Matriz:

    def __init__(self, filas, columnas):
        """ 
        Declaración de una matriz.
        Debe especificarse el número de filas y columnas.
        """

        self.filas = filas
        self.columnas = columnas

        # Se hace de este modo para evitar que se guarden referencias a la misma dirección de memoria
        fila = [None]*columnas
        self.contenido_matriz = []
        for j in range(filas):
            self.contenido_matriz.append(fila[:])

    def __str__(self):

        # TODO
        #imprimir = ""
        #
        #for i in range(fila):
        #    for j in range(columna):
        #        imprimir += ""
        #    imprimir += "\n"

        return str(self.contenido_matriz)
        
    # Devuelve el elementdo especificado
    def elemento(self, fila, columna):
        return self.contenido_matriz[fila-1][columna-1]
        
    # Modifica el elemento especificado
    def cambiar_elemento(self, fila, columna, valor):
        self.contenido_matriz[fila-1][columna-1] = valor


