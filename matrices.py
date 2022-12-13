"""
Autores:
    - Jose Romero Conde
    - Stevan Lino Gartz

Propósito:
    Esta librería puede realizar operaciones con matrices.

"""

class Matriz:

    def __init__(self, filas, columnas):
        """
        Declaración de una matriz.
        Debe especificarse el número de filas y columnas.
        """

        self.filas = filas
        self.columnas = columnas

        if filas == 1:
            self.contenido_matriz = [None] * columnas
        else:
            # Se hace de este modo para evitar que se guarden referencias a la misma
            # dirección de memoria y que a la hora de modificar la matriz se
            # modifique de una manera no deseada
            self.contenido_matriz = []
            for j in range(filas):
                fila = Matriz(1, columnas)
                self.contenido_matriz.append(fila)

    def __str__(self):
        """
        Presentación del estado actual de la matriz.
        """

        imprimir = ""
        if self.filas == 1:
            imprimir = str(self.contenido_matriz)+"\n"

        else:
            for i in range(1, self.filas+1):
                imprimir += str(self[i])

        return imprimir


    def __getitem__(self, elemento):
        """
        Devuelve el elemento especificado.
        """

        try:
            elemento = int(elemento)
            if elemento<1:
                raise ValueError
            return self.contenido_matriz[elemento-1]

        except ValueError:
            print("La fila y la columna especificada debe ser un número entero mayor que 0")
            return False

        except IndexError:
            print(f'No esixte el elemento {fila},{columna}')
            return False

    def __setitem__(self, elemento, valor):
        """
        Modifica el elemento especificado.
        """
        try:
            elemento = int(elemento)
            if elemento<1:
                raise ValueError
            self.contenido_matriz[elemento-1] = valor

        except ValueError:
            print("La fila y la columna especificada debe ser un número entero mayor que 0")
            return False

        except IndexError:
            print(f'No esixte el elemento {fila},{columna}')
            return False



    def pide_matriz(self):
        for i in range (self.filas):
            for j in range (self.columnas):
                self.contenido_matriz[i][j]=float(input(f"Dime el elemento de la fila {i} y la columna {j}: ")
    def dimensiones(self):                                     
        return self.filas, self.columnas
          
     

if __name__ == "__main__":
    # Este script prueba diferentes funcionalidades para comprobar rápidamente que
    # todo funiona correctamente

    from matrices import Matriz

    mimatriz = Matriz(4,5)

    mimatriz[2][3] = 414243
    print(mimatriz[2][3])
    print(mimatriz)
    #mimatriz[-2][81] = 41
    #print(mimatriz["A"]["B"])
      

                                                  
   
