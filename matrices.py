"""
Autores:
    - José Romero Conde
    - Stevan Lino Gartz

Propósito:
    Esta librería puede ser utilizada para realizar operaciones con matrices.

"""

class Matriz:

    def __init__(self, *args, tipo_matriz='vacia'):
        """
        Declaración de una matriz.
        Puede declararse una matriz de las siguientes formas:
            1) Matriz(filas, columnas) # filas y columnas son enteros mayores que 0
            2) Matriz(filas, columnas, tipo_matriz='nula')
            3) Matriz(filas, columnas, tipo_matriz='identidad')
            4) Matriz(filas, columnas, tipo_matriz='vacia')
            5) Matriz(contenido_matriz) # contenido_matriz es de tipo lista
        """
        self.contenido_matriz = []

        # Para facilitar las operaciones, las matrices compuestas por más de una fila almacenarán
        # una matriz fila en cada fila en vez de una simple lista. Gracias a eso se pueden hacer
        # operaciones del tipo matriz[1] + matriz[2]

        # En el caso donde se define la matriz pero no se especifican las dimensiones ni el contenido.
        # Este tipo de matrices se usan solo para poder acceder a los métodos de guardado y carga.
        if len(args) == 0:
            self.filas = 0
            self.columnas = 0
        
        # En el caso donde se define una matriz por contenido, o se define una matriz cuadrada.
        elif len(args) == 1:

            # En el caso donde se define una matriz cuadrada pero sin indicar el contenido.
            if type(args[0]) == int:
                self = self.__init__(args[0], args[0], tipo_matriz=tipo_matriz)

            # En el caso donde se define una matriz por su contenido
            elif type(args[0]) in [list, tuple]:
                contenido = args[0]

                # En caso de que sea una matriz fila.
                if type(contenido[0]) not in [list, tuple]:
                    self.filas = 1
                    self.contenido_matriz = contenido
                    self.columnas = len(contenido)

                else:
                    self.filas = len(contenido)
                    self.columnas = len(contenido[0])

                    for fila in contenido:
                        # Primero se comprueba que las dimensiones son válidas.
                        if len(fila) != self.columnas:
                            raise IndexError("Todas las filas de la matriz deben tener el mismo número de elementos.")

                        self.contenido_matriz.append(Matriz(fila))
            else:
                raise TypeError('Matriz declarada de forma incorrecta. Para más información haz uso de help(Matriz).')

        # En el caso donde solo se define las dimensiones de la matriz y su tipo.
        elif len(args) == 2:
            self.filas = args[0]
            self.columnas = args[1]

            if tipo_matriz == 'identidad':
                if self.columnas != self.filas:
                    raise TypeError('La matriz identidad debe ser cuadrada.')

                for j in range(1,self.filas+1):
                    fila = Matriz([0] * self.columnas)
                    fila[j] = 1
                    self.contenido_matriz.append(fila)
                
            else:
                if tipo_matriz == 'vacia':
                    contenido = None
                elif tipo_matriz == 'nula':
                    contenido = 0
                else:
                    raise TypeError(f'No se soporta una matriz de tipo {tipo_matriz}.')
                    
                # Se hace de este modo para evitar que se guarden referencias a la misma
                # dirección de memoria y que a la hora de modificar la matriz se
                # modifique de una manera no deseada.
                for j in range(1,self.filas+1):
                    fila = Matriz([contenido] * self.columnas)
                    self.contenido_matriz.append(fila)

        else:
            raise TypeError('Matriz declarada de forma incorrecta. Para más información haz uso de help(Matriz).')


    def __getitem__(self, elemento):
        """
        Devuelve el elemento especificado.
        """
        
        try:
            if type(elemento) == int:
                if elemento<1:
                    raise ValueError
                return self.contenido_matriz[elemento-1]
            else:
                raise ValueError

        except ValueError:
            raise IndexError("La fila y la columna especificada debe ser un número entero mayor que 0.")


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
            # Se intercepta el error y se vuelve a lanzar con el propósito de dar una descripción más detallada del problema.
            raise ValueError("La fila y la columna especificada deben ser un número entero mayor que 0.")


    def __str__(self):
        """
        Presentación del estado actual de la matriz.
        """

        imprimir = ""
        if self.filas == 1:
            imprimir = str(self.contenido_matriz)

        else:
            for i in range(1, self.filas+1):
                imprimir += str(self[i])+"\n"

            # Se quita el último salto de línea (porque sobra)
            imprimir = imprimir[:-1] 
        return imprimir
        
    
    def __add__(self,matriz):
        """
        Suma de matrices.
        """

        matriz_res=Matriz(self.filas,self.columnas)
        if self.dimension() != matriz.dimension():
            print ("Las matriz no tienen la misma dimensión y por tanto la suma no está definida")
        else: 
            for i in range (1,self.filas+1):
                for j in range (1,self.columnas+1):
                    matriz_res[i][j]=self[i][j]+matriz[i][j]
        return matriz_res
        
    
    def __sub__(self,matriz):
        """
        Resta de matrices.
        """

        matriz_res=Matriz(self.filas,self.columnas)
        if self.dimension() != matriz.dimension():
            print ("Las matriz no tienen la misma dimensión y por tanto la resta no está definida")
        else: 
            for i in range (1,self.filas+1):
                for j in range (1,self.columnas+1):
                    matriz_res[i][j]=self[i][j]-matriz[i][j]
        return matriz_res


    def __mul__(self,a):
        """
        Multiplicación entre matrices o entre una matriz y un escalar.
        """

        if type(a)==float or type(a)==int:
            matriz_producto=Matriz(self.filas,self.columnas)
            for i in range (1,self.filas+1):
                for j in range (1,self.columnas+1):
                    matriz_producto[i][j]=a*self[i][j]
        elif type(a)==Matriz:
            matriz_producto=Matriz(self.filas,a.columnas)

            # Se comprueba si se pueden multiplicar.
            if self.columnas==a.filas:
                for i in range (1,self.filas+1):
                    for j in range (1,a.columnas+1):
                        matriz_producto[i][j]=0
                        for n in range (1,self.columnas+1):
                            matriz_producto[i][j]=float(self[i][n]*a[n][j])+matriz_producto[i][j]
            else:
                print("La primera matriz no tiene el mismo número de columnas que filas tiene la segunda, por lo que no se pueden multiplicar.")
        return matriz_producto

    
    def imprime(self):
        """
        Presentación del las entradas de la matriz de forma visualmente agradable.
        """
        # En caso de que sea una matriz fila
        if self.filas == 1:
            print(str(self[1]).replace(",", ""))

        else:
            imprimir = ""

            # Se busca los valores con más caracteres de cada columna, para así decidir el número
            # de espacios en blanco que los separa.
            longitud_maxima = []
            for j in range(1,self.columnas+1):
                valores = []
                for i in range(1,self.filas+1):
                    valores.append(len(str(self[i][j])))

                longitud_maxima.append(max(valores))

            for i in range(1,self.filas+1):
                for j in range(1,self.columnas+1):
                    # Se mide la diferencia entre el elemento con más caracteres de la columna y el actual.
                    # Esa diferencia +1 es el número de espacios que aparecen después del elemento para
                    # que esté correctamente presentado.
                    longitud_elemento_actual = len(str(self[i][j]))
                    espaciado = longitud_maxima[j-1]-longitud_elemento_actual+1
                    #a y b serán las porciones del parentesis. La variable 'a' la utilizaremos para el 
                    #lado izquierdo y b para el derecho. Como es natural, solo los elementos de los bordes 
                    #laterales tendran valores en ellas.
                    a = b = ''
                    if j==1:
                        if i==1:
                            a = "/ " 

                        elif i==self.filas:
                            a = "\\ " 

                        else:
                            a = "| " 

                    if j==self.columnas:
                        if i==1:
                            b= "\\"

                        elif i==self.filas:
                            b= "/"

                        else:
                            b= "|"
                    
                    imprimir += a + str(self[i][j]) + " "*espaciado + b
                imprimir += "\n"

            # Se quita el último salto de línea (porque sobra)
            imprimir = imprimir[:-1]
            print(imprimir)

        

    def fila(self, fila):
        """
        Devuelve la fila especificada.
        """

        return self[fila]


    def columna(self, columna):
        """
        Devuelve la columna especificada.
        """

        col = []
        for i in range(1,self.filas+1):
            col.append(self[i][columna])
        return Matriz(col)


    def dimension(self):
        """
        Devuelve una tupla con la siguiente estructura: (filas, columnas).
        """

        return self.filas, self.columnas


    def diagonal_principal(self, *args):
        """
        Devuelve los elementos de la diagonal descendente deseada de la matriz.
        También se puede obtener una diagonal diferente al indicar el desplazamiento de esta.
        Ejemplo: matriz.diagonal_principal(1)
        """
        
        Error = False
        desplazamiento = 0
        if len(args) != 0:
            desplazamiento = args[0]
        
        #Contemplación de valores incorrectos
        if desplazamiento > (self.columnas+1):
            print('Error: el desplazamiento no puede ser mayor que el número de columnas.')
            Error = True
        if desplazamiento < -1*(self.filas+1):
            print('Error: el desplazamiento no puede ser menor que el número de filas.')
            Error = True
        
        elementos_diagonal = []    
        if Error == False:
            if desplazamiento < 0:
                for j in range(1, min([self.filas+desplazamiento, self.columnas])+1):
                    i = j - desplazamiento
                    elementos_diagonal.append(self[i][j])
    
            else:
                for i in range(1, min([self.filas, self.columnas-desplazamiento])+1):
                    j = i + desplazamiento
                    elementos_diagonal.append(self[i][j])

        return elementos_diagonal
    
    
    def diagonal_secundaria(self):
        """
        Devuelve los elementos de la diagonal ascendente principal de la matriz.
        """

        l = []
        tamanho_diagonal = min([self.filas, self.columnas])
        for i in range (1,tamanho_diagonal+1):
            l.append(self[i][tamanho_diagonal+1-i])
        return l
          
        
    def traspuesta(self):
        """
        Devuelve la matriz traspuesta.
        """
        matriztras=Matriz(self.columnas,self.filas)
        for i in range (1,self.filas+1):
            for j in range (1,self.columnas+1):
                matriztras[j][i]=self[i][j]
        return matriztras
    
    
    def opuesta(self):
        """
        Devuelve la matriz opuesta, definida por -I * A (o A * -I).
        Esta matriz tiene como cualidad que A + opA = 0 (Siendo 0 una matriz de todo ceros).
        """

        return self*(-1)

    
    def pide_matriz(self):
        """
        Pide al usuario una matriz por teclado.
        """

        for i in range (1,self.filas+1):
            for j in range (1,self.columnas+1):
                valor_valido = False
                while not valor_valido:
                    try:
                        self[i][j]=float(input(f"Dime el elemento de la fila {i} y la columna {j}: "))
                        valor_valido = True
                    except:
                        print("Error: Debes introducir un número. Por favor, inténtalo de nuevo.")


    def media(self):
        """
        Devuelve la media de los valores de los elementos de la matriz.
        """

        lista=self.lista_elementos()
        a=0
        for i in lista:
            a+=float(i) 
        m=a/len(lista)
        return m


    def mayor(self):
        """
        Devuelve el valor del elemento más grande de la matriz
        """

        lista=self.lista_elementos()
        return max(lista)


    def menor(self):
        """
        Devuelve el valor del elemento más pequeño de la matriz
        """

        lista=self.lista_elementos()
        return min(lista)

        
    def lista_elementos(self):
        """
        Devuelve todos los elementos de la matriz en forma de lista unidimensional.
        """

        l=[]
        for i in range (1,self.filas+1):
            for j in range (1,self.columnas+1):
                l.append(self[i][j]) 
        return l

    
    def guardar(self, archivo, matrices):
        """
        Guarda una lista de matrices en un archivo.
        """

        contenido = ""
        for matriz in matrices:
            for i in range(1, matriz.filas+1):
                for j in range(1, matriz.columnas+1):
                    contenido += str(matriz[i][j]) + ","
                contenido = contenido[:-1]+"\n"
            contenido += "\n"

        archivo = open(archivo, 'w')
        archivo.write(contenido)
        archivo.close()


    def cargar(self, archivo):
        """
        Carga una lista de matrices almacenadas en un archivo con el método guardar,
        y devuelve una lista con todas las matrices.
        """

        archivo = open(archivo, 'r')
        contenido = archivo.read()
        archivo.close()

        matrices = []
        contenido = contenido.split("\n")
        nueva_matriz = []
        for linea in contenido:
            if linea == "":
                if len(nueva_matriz) > 0:
                    matrices.append(Matriz(nueva_matriz))
                nueva_matriz = []
            else:
                fila = linea.split(",")
                fila = [float(elemento) for elemento in fila]
                nueva_matriz.append(fila)

        return matrices
    

    def es_cuadrada(self):
        """
        Devuelve un booleano que indica si la matriz es cuadrada o no.
        """

        return self.columnas == self.filas
    

    def es_triangular_inf(self):
        """
        Devuelve un booleano que indica si la matriz es triangular inferior o no.
        """

        triangular_inf = True
        if not self.es_cuadrada: triangular_inf = False
        for i in range (1,self.filas+1):
            for j in range (1,self.columnas+1):
                if i>j and self[i][j] != 0:
                    triangular_inf = False
        return triangular_inf
    

    def es_triangular_sup(self):
        """
        Devuelve un booleano que indica si la matriz es triangular superior o no.
        """

        return self.traspuesta().es_triangular_inf()
    

    def es_diagonal(self):
        """
        Devuelve un booleano que indica si la matriz es diagonal o no.
        """

        return self.es_triangular_sup() == self.es_triangular_inf() == True
    

    def es_fila(self):
        """
        Devuelve un booleano que indica si la matriz es una fila o no.
        """

        return self.filas == 1
    

    def es_columna(self):
        """
        Devuelve un booleano que indica si la matriz es una columna o no.
        """

        return self.columnas == 1
    

    def es_simetrica(self):
        """
        Devuelve un booleano que indica si la matriz es simétrica o no.
        """

        return self.traspuesta() == self
   

    def es_magica(self):
        """
        Devuelve un booleano que indica si la matriz es mágica o no.
        """
        #Como en esta función pero solo en esta función vamos a necesitar sumar 
        #listas de elementos (filas o culumnas); crearemos aquí una función con tal propósito.
        def _suma_lista(lista):
            s = 0
            if type(lista) == Matriz:
                lista = lista.contenido_matriz
            for i in range (len(lista)):
                s += lista[i]
            return s 

    
        magica = False
        if self.es_cuadrada():
            
            #Primero comprobaremos la propiedad de que todas las sumas de filas columnas y diagonales es constante.
            a = _suma_lista(self.columna(1))
            if _suma_lista(self.diagonal_principal()) == _suma_lista(self.diagonal_secundaria()) == a:
                magica = True
            for i in range (1,self.columnas+1):
                if _suma_lista(self.columna(i)) != a or _suma_lista(self[i]) != a:
                    magica = False
            
            #Ahora comprobaremos que usa todos los números del 1 al (n^2)-1. Sin repeticiones.
            numeros=[]
            for i in range ((self.columnas)**2):
                numeros.append(i+1)
            try:
                for i in range (1,self.filas+1):
                    for j in range (1,self.columnas+1):
                        numeros.remove(self[i][j])
            
            #Solo resultará en excepción si los elementos de la lista y de la matriz no son iguales.
            #Como en la lista están los elementos que debe tener, funciona.
            except:
                magica = False
        return magica  
    

    def constante_magica(self):
        if self.es_magica():
            M = self.columnas*((self.columnas**2)+1)/2
        return M
            
      
    def imprime_tipo(self):
        """
        Imprime en pantalla las características de la matriz.
        """

        if self.es_cuadrada(): print('Es cuadrada.')
        if self.es_diagonal(): print('Es diagonal.')
        if self.es_fila() : print('Es una matriz fila.')
        if self.es_columna() : print('Es una matriz columna.')
        if self.es_simetrica() : print('Es una matriz simétrica.')
        if self.es_triangular_sup() : print('Es triangular superior.')
        if self.es_triangular_inf() : print('Es triangular inferior.')
        if self.es_magica() : print('Es Mágica. Su constante es:',self.constante_magica())
          


if __name__ == "__main__":
    # Este script prueba diferentes funcionalidades para 
    # comprobar rápidamente que todo funiona correctamente.

    otramatriz = Matriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    matriz2 = Matriz([[5,6,7,8],[9,10,11,12],[1,2,3,4]])

    print("\nEjecutando tests...")


    print('\n----(1)----\n')
    # 1. Definición de una matriz a partir de sus dimensiones.
    mimatriz = Matriz(2,3)


    print('\n----(2)----\n')
    # 2.a Asignación de un elemento.
    otramatriz[1][1] = 1337
    
    # 2.b Obtención de un elemento.
    print(otramatriz[1][1])


    print('\n----(3)----\n')
    # 3. Presentación de una matriz.
    otramatriz.imprime() 


    print('\n----(4)----\n')
    # 4. Obtención de una matriz por teclado.
    mimatriz.pide_matriz()


    print('\n----(5)----\n')
    # 5.a Obtención de una fila de la matriz.
    print(matriz2[1])
    print(matriz2.fila(1))

    # 5.b Obtención de una columna de la matriz.
    print(otramatriz.traspuesta()[1])
    print(otramatriz.columna(1))
    
    # 5.c Obtención de la diagonal de la matriz.
    matriz_cuadrada = Matriz([[5,3,7],[9,1,2],[3,6,4]])
    print(matriz_cuadrada.diagonal_principal())
    print(matriz_cuadrada.diagonal_secundaria())
    print(matriz_cuadrada.diagonal_principal(2)) # El 2 indica que es la diagonal que empieza en la columna 3
    print(matriz_cuadrada.diagonal_principal(-1)) # El -1 indica que es la diagonal que empieza en la fila 2
    print(matriz_cuadrada.diagonal_principal(-6))


    print('\n----(6)----\n')
    # 6. Obtención de las dimensiones de la matriz.
    print(otramatriz.dimension())


    print('\n----(7)----\n')
    # 7.a Suma de matrices.
    (otramatriz+matriz2).imprime()

    # 7.b Resta de matrices.
    (otramatriz-matriz2).imprime()


    print('\n----(8)----\n')
    # 8. Matriz opuesta.
    otramatriz.opuesta().imprime()


    print('\n----(9)----\n')
    # 9. Producto de matrices.
    (mimatriz*otramatriz).imprime()


    print('\n----(10)----\n')
    # 10. Producto de un escalar por una matriz.
    print(otramatriz*2)


    print('\n----(11)----\n')
    # 11.a Matriz nula a partir de las dimensiones dadas.
    print(Matriz(3,2,tipo_matriz='nula'))

    # 11.b Matriz identidad a partir de las dimensiones dadas.
    In3 = Matriz(3,tipo_matriz='identidad')


    print('\n----(12)----\n')
    # 12. Matriz traspuesta.
    (otramatriz.traspuesta()).imprime()


    print('\n----(13)----\n')
    # 13. Caracterización de matrices: determinación de las condiciones de matriz cuadrada, fila, columna, simétrica, triangular superior y triangular inferior.
    In3.imprime_tipo()
    print(In3.es_cuadrada())
    print(In3.es_fila())
    print(In3.es_columna())
    print(In3.es_simetrica())
    print(In3.es_triangular_sup())
    print(In3.es_triangular_inf())
    

    print('\n----(14)----\n')
    # 14. Matriz mágica.
    print(otramatriz.es_magica())
    magica = Matriz([[8,1,6],[3,5,7],[4,9,2]])
    print(magica.es_magica())


    print('\n----(15)----\n')
    # 15.a Obtención del mayor valor
    print(otramatriz.mayor())

    # 15.b Obtención del menor valor
    print(otramatriz.menor())

    # 15.c Obtención del la media de los valores de los elementos
    print(otramatriz.media())
                                   
                                                
    print("\n----(Guardado y carga de matrices)----\n")
    # Guardar la matriz en un archivo
    Matriz().guardar('matrices.matrix', [otramatriz, matriz2])

    # Cargar la matriz desde un archivo             
    A, B = Matriz().cargar('matrices.matrix')
    print(A)
    print(B)

    print("\nTests finalizados sin errores en tiempo de ejecución.")