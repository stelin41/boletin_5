"""
Autores:
    - José Romero Conde
    - Stevan Lino Gartz

Propósito:
    Esta librería puede realizar operaciones con matrices.

"""

class Matriz:

    def __init__(self, *args, tipo_matriz='normal'):
        """
        Declaración de una matriz.
        Puede declararse una matriz de las siguientes formas:
            Matriz(filas, columnas) # filas y columnas son enteros mayores que 0
            Matriz(filas, columnas, tipo_matriz='nula')
            Matriz(filas, columnas, tipo_matriz='identidad')
            Matriz(contenido_matriz) # contenido_matriz es de tipo lisa
        """
        self.contenido_matriz = []
        # Esto es para el caso donde se define la matriz y su contenido
        if len(args) == 1:
            contenido = args[0]
            # En caso de que sea una matriz fila
            if type(contenido[0]) != list:
                self.filas = 1
                self.contenido_matriz = contenido
                self.columnas = len(contenido)

            else:
                self.filas = len(contenido)
                self.columnas = len(contenido[0])

                for fila in contenido:
                    # Primero se comprueba que las dimensiones son válidas
                    if len(fila)!=self.columnas:
                        raise Exception("Todas las filas de la matriz deben tener el mismo número de elementos.")

                    self.contenido_matriz.append(Matriz(fila))


        # Esto es en el caso donde solo se define la matriz pero no su contenido
        elif len(args) == 2:
            self.filas = args[0]
            self.columnas = args[1]

            if tipo_matriz == 'identidad':
                if self.columnas != self.filas:
                    raise Exception('La matriz identidad debe ser cuadrada.')

                for j in range(1,self.filas+1):
                    fila = Matriz([0] * self.columnas)
                    fila[j] = 1
                    self.contenido_matriz.append(fila)
                
            else:
                if tipo_matriz == 'normal':
                    contenido = None
                elif tipo_matriz == 'nula':
                    contenido = 0
                else:
                    raise Exception(f'No se soporta una matriz de tipo {tipo_matriz}.')
                    
                # Se hace de este modo para evitar que se guarden referencias a la misma
                # dirección de memoria y que a la hora de modificar la matriz se
                # modifique de una manera no deseada
                for j in range(1,self.filas+1):
                    fila = Matriz([contenido] * self.columnas)
                    self.contenido_matriz.append(fila)
            
        

        else:
            raise Exception('Hay que especificar las dimensiones de la matriz o su contenido.')

                
  
    def print(self):
        #Presentación del estado actual de la matriz.

        imprimir = ""

        # Se busca los valores con más caracteres de cada columna, para así
        # decidir el número de espacios en blanco que los separa.
        longitud_maxima = []
        for j in range(1,self.columnas+1):
            valores = []
            for i in range(1,self.filas+1):
                print(j,i)
                valores.append(len(str(self[i][j])))

            longitud_maxima.append(max(valores))

        for i in range(1,self.filas+1):
            for j in range(1,self.columnas+1):
                # Se mide la diferencia entre el elemento con más caracteres de
                # la columna y el actual. Esa diferencia +1 es el número de
                # espacios que aparecen después del elemento para que esté
                # correctamente presentado.
                longitud_elemento_actual = len(str(self[i][j]))
                espaciado = longitud_maxima[j-1]-longitud_elemento_actual+1
                a = b = ''
                if j==1:
                    if i==1:
                        a = "/ " 

                    elif i==self.filas:
                        a = "\\ " 

                    else:
                        a = "| " 

                elif j==self.columnas:

                    if i==1:
                        b= "\\"

                    elif i==self.filas:
                        b= "/"

                    else:
                        b= "|"
                
                imprimir += a + str(self[i][j]) + " "*espaciado + b
            imprimir += "\n"

        return imprimir
  

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
        #print(type(elemento))
        try:
            elemento = int(elemento)
            if elemento<1:
                raise ValueError
            return self.contenido_matriz[elemento-1]

        except ValueError:
            raise "La fila y la columna especificada debe ser un número entero mayor que 0"



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
            return "La fila y la columna especificada debe ser un número entero mayor que 0"
        
    def diagonal(self):
        """
        Devuelve los elementos de la diagonal de la matriz.
        """
        elementos_diagonal = []
        for i in range(1, min([self.filas, self.columnas])+1):
            elementos_diagonal.append(self[i][i])
        return elementos_diagonal


    def pide_matriz(self):
        for i in range (1,self.filas+1):
            for j in range (1,self.columnas+1):
                self[i][j]=float(input(f"Dime el elemento de la fila {i} y la columna {j}: "))
                
                          
    def dimension(self):
        return self.filas, self.columnas
          
        
    def traspuesta(self):
        matriztras=Matriz(self.columnas,self.filas)
        for i in range (1,self.filas+1):
            for j in range (1,self.columnas+1):
                matriztras[j][i]=self[i][j]
        return matriztras
    
    
    def opuesta(self):
        """
        La matriz opuesta (denotada por -A) viene dada por la expresión --> -A = -I * A
        """
        matrizop=Matriz(self.filas,self.columnas)
        for i in range (1,self.filas+1):
            for j in range (1,self.columnas+1):
                matrizop[i][j]=-self[i][j]
        return matrizop
    
    def __mul__(self,a):
        """
        B=𝛼A o B=A'*A
        """
        if type(a)==float or type(a)==int:
            matriz_producto=Matriz(self.filas,self.columnas)
            for i in range (1,self.filas+1):
                for j in range (1,self.columnas+1):
                    matriz_producto[i][j]=a*self[i][j]
        elif type(a)==Matriz:
            matriz_producto=Matriz(self.filas,a.columnas)
            if self.columnas==a.filas:
                print("La multiplicación entre matrices está definida.")
                for i in range (1,self.filas+1):
                    for j in range (1,a.columnas+1):
                        matriz_producto[i][j]=0
                        for n in range (1,self.columnas+1):
                            matriz_producto[i][j]=float(self[i][n]*a[n][j])+matriz_producto[i][j]
        return matriz_producto
    
    def __add__(self,matriz2):
        matriz_res=Matriz(self.columnas,self.filas)
        if self.dimension != matriz2.dimension:
            print ("Las matriz no tienen la misma dimensión y por tanto la suma no está definida")
        else: 
            for i in range (1,self.filas+1):
                for j in range (1,self.columnas+1):
                    matriz_res[i][j]=self[i][j]+matriz2[i][j]
        return matriz_res
        
    
    def __sub__(self,matriz2):
        matriz_res=Matriz(self.columnas,self.filas)
        if self.dimension != matriz2.dimension:
            print ("Las matriz no tienen la misma dimensión y por tanto la suma no está definida")
        else: 
            for i in range (1,self.filas+1):
                for j in range (1,self.columnas+1):
                    matriz_res[i][j]=self[i][j]-matriz2[i][j]
        return matriz_res


    def media(self):
        lista=self.lista_elementos()
        a=0
        for i in lista:
            a+=float(i) 
        m=a/len(lista)
        return m


    def mayor(self):
        lista=self.lista_elementos()
        return max(lista)


    def menor(self):
        lista=self.lista_elementos()
        return min(lista)

        
    def lista_elementos(self):
        l=[]
        for i in range (1,self.filas+1):
            for j in range (1,self.columnas+1):
                l.append(self[i][j]) 
        return l
    
    ##tipos
    
    def es_cuadrada(self):
        cuadrada = self.columna == self.fila
        return cuadrada
    
    def es_triangular_inf(self):
        triangular_inf = True
        if not es_cuadrada: triangular_inf = False
        for i in range (1,self.filas+1):
            for j in range (1,self.columnas+1):
                if i>j and self[i][j] != 0:
                    triangular_inf = False
        return triangular_inf
    
    def es_triangular_sup(self):
        if self.traspuesta().es_triangular_inf():
                triangular_sup = True
        return triangular_sup
    
    def es_diagonal(self):
        if es_triagonal_sup() == es_triagonal_inf() == True:
            diagonal = True
        return diagonal
                              
    def es_fila(self):
        fila = self.fila == 1
        return fila
    
    def es_columna(self):
        fila = self.columna == 1
        return columna
    
    def es_simetrica(self):
        if self.traspuesta() == self: simetrica = True
        return simetrica
   
    def tipo(self):
        if es_cuadrada() == True: print('\nEs cuadrdada.')
        if es_triangular_inf() == True: print('\nEs triangular inferior.')
        if es_triangular_sup() == True: print('\nEs triangular superior.')
        if es_diagonal() == True: print('\nEs diagonal.')
        if es_fila() == True: print('\nEs una matriz fila.')
        if es_columna() == True: print('\nEs una matriz columna.')  
        if es_simetrica() == True: print('\nEs una matriz simétrica.')  


if __name__ == "__main__":
    # Este script prueba diferentes funcionalidades para 
    # comprobar rápidamente que
    # todo funiona correctamente

    otramatriz = Matriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    matriz2 = Matriz([[5,6,7,8],[9,10,11,12],[1,2,3,4]])

    # 1. Definición de una matriz a partir de sus dimensiones
    mimatriz = Matriz(2,3)

    # 2.a Asignación de un elemento
    otramatriz[1][1] = 1337

    # 2.b Obtención de un elemneto
    print(otramatriz[1][1])

    # 3. Presentación de una matriz
    otramatriz.print()

    # 4. Obtención de una matriz por teclado
    mimatriz.pide_matriz()

    # 5.a Obtención de una fila de la matriz
    print(mimatriz[1])

    # 5.b Obtención de una columna de la matriz
    
    # 5.c Obtención de la diagonal de la matriz
    print(otramatriz.diagonal())

    # 6. Obtención de las dimensiones de la matriz
    print(otramatriz.dimension())

    # 7.a Suma de matrices
    print(otramatriz+matriz2)

    # 7.b Resta de matrices
    print(otramatriz-matriz2)

    # 8. Matriz opuesta (Preguntar si -A es correcto)
    print(otramatriz.opuesta())

    # 9. Producto de matrices
    print(mimatriz*otramatriz)

    # 10. Producto de un escalar por un vector
    print(otramatriz*2)

    # 11.a Matriz nula a partir de las dimensiones dadas
    print(Matriz(3,2,tipo_matriz='nula'))

    # 11.b Matriz identidad a partir de las dimensiones dadas
    print(Matriz(3,3,tipo_matriz='identidad'))

    # 12. Matriz traspuesta
    print(otramatriz.traspuesta())

    # 13. Caracterización de matrices: determinación de las condiciones de matriz cuadrada, fila, columna, simétrica, triangular superior y triangular inferior. (TODO)

    # 14. Matriz mágica

    # 15.a Obtención del mayor valor
    print(otramatriz.mayor())

    # 15.b Obtención del menor valor
    print(otramatriz.menor())

    # 15.c Obtención del la media de los valores de los elementos
    print(otramatriz.media())
                                                
