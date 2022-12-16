"""
Autores:
    - José Romero Conde
    - Stevan Lino Gartz

Propósito:
    Esta librería puede ser utilizada para realizar operaciones con matrices.

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

        # En el caso donde se define la matriz especificar las dimensiones ni el conenido.
        # Este tipo de matrices se usan solo para poder acceder a los métodos de guardado y carga.
        if len(args) == 0:
            self.filas = 0
            self.columnas = 0
        
        # En el caso donde se define la matriz y su contenido.
        elif len(args) == 1:
            contenido = args[0]
            # En caso de que sea una matriz fila.
            if type(contenido[0]) != list:
                self.filas = 1
                self.contenido_matriz = contenido
                self.columnas = len(contenido)

            else:
                self.filas = len(contenido)
                self.columnas = len(contenido[0])

                for fila in contenido:
                    # Primero se comprueba que las dimensiones son válidas.
                    if len(fila)!=self.columnas:
                        raise Exception("Todas las filas de la matriz deben tener el mismo número de elementos.")

                    self.contenido_matriz.append(Matriz(fila))

        # En el caso donde solo se define la matriz pero no su contenido.
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
                # modifique de una manera no deseada.
                for j in range(1,self.filas+1):
                    fila = Matriz([contenido] * self.columnas)
                    self.contenido_matriz.append(fila)

        else:
            raise Exception('Hay que especificar las dimensiones de la matriz o su contenido.')


    def __getitem__(self, elemento):
        """
        Devuelve el elemento especificado.
        """
        #print(type(elemento))
        try:
            if type(elemento) == int:
                if elemento<1:
                    raise ValueError
                return self.contenido_matriz[elemento-1]
            else:
                raise ValueError

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
        
    
    def __add__(self,matriz):
        """
        Suma de matrices.
        """
        matriz_res=Matriz(self.filas,self.columnas)
        if self.dimension != matriz.dimension:
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
        if self.dimension != matriz.dimension:
            print ("Las matriz no tienen la misma dimensión y por tanto la resta no está definida")
        else: 
            for i in range (1,self.filas+1):
                for j in range (1,self.columnas+1):
                    matriz_res[i][j]=self[i][j]-matriz[i][j]
        return matriz_res


    def __mul__(self,a):
        """
        Multiplicación entre matrices o entre una matriz y un escalar.
        B=𝛼A o B=A'*A
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
        return matriz_producto


    def print(self):
        """
        Presentación del estado actual de la matriz de forma visualmente agradable.
        """

        imprimir = ""

        # Se busca los valores con más caracteres de cada columna, para así
        # decidir el número de espacios en blanco que los separa.
        longitud_maxima = []
        for j in range(1,self.columnas+1):
            valores = []
            for i in range(1,self.filas+1):
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

        print(imprimir)
        

    def fila(self, fila):
        return self[fila]


    def columna(self, columna):
        col = []
        for i in range(1,self.filas+1):
            col.append(self[i][columna])
        return Matriz(col)


    def dimension(self):
        return self.filas, self.columnas


    def diagonal_principal(self, *args):
        """
        Devuelve los elementos de la diagonal de la matriz.
        """
        desplazamiento = 0
        if len(args) != 0:
            desplazamiento = args[0]

        elementos_diagonal = []
        if desplazamiento < 0:
            for j in range(1, min([self.filas+desplazamiento, self.columnas])+1):
                i = j - desplazamiento
                elementos_diagonal.append(self[i][j])

        else:
            for i in range(1, min([self.filas, self.columnas-desplazamiento])+1):
                j = i + desplazamiento
                elementos_diagonal.append(self[i][j])

        return elementos_diagonal
    
    
    def diagonal_opuesta(self, *args):
        """
        Devuelve los elementos de la diagonal de la matriz.
        """
        l= []
        for i in range (1,self.columnas+1):
            l.append(self[i][self.columnas+1-i])
        return l
          
        
    def traspuesta(self):
        matriztras=Matriz(self.columnas,self.filas)
        for i in range (1,self.filas+1):
            for j in range (1,self.columnas+1):
                matriztras[j][i]=self[i][j]
        return matriztras
    
    
    def opuesta(self):
        return self*(-1)

    
    def pide_matriz(self):
        for i in range (1,self.filas+1):
            for j in range (1,self.columnas+1):
                self[i][j]=float(input(f"Dime el elemento de la fila {i} y la columna {j}: "))


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

    
    def guardar(self, archivo, matrices):
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
                nueva_matriz.append(linea.split(","))

        return matrices
    

    def es_cuadrada(self):
        return self.columnas == self.filas
    

    def es_triangular_inf(self):
        triangular_inf = True
        if not self.es_cuadrada: triangular_inf = False
        for i in range (1,self.filas+1):
            for j in range (1,self.columnas+1):
                if i>j and self[i][j] != 0:
                    triangular_inf = False
        return triangular_inf
    

    def es_triangular_sup(self):
        return self.traspuesta().es_triangular_inf()
    

    def es_diagonal(self):
        return self.es_triangular_sup() == self.es_triangular_inf()
    

    def es_fila(self): 
        return self.filas == 1
    

    def es_columna(self):
        return self.columnas == 1
    

    def es_simetrica(self):
        return self.traspuesta() == self
   

    def tipo(self):
        if self.es_cuadrada(): print('Es cuadrada.')
        if self.es_triangular_inf() : print('Es triangular inferior.')
        if self.es_triangular_sup() : print('Es triangular superior.')
        if self.es_diagonal() : print('Es diagonal.')
        if self.es_fila() : print('Es una matriz fila.')
        if self.es_columna() : print('Es una matriz columna.')  
        if self.es_simetrica() : print('Es una matriz simétrica.')  


    def es_magica(self):
    
        def _suma_lista(lista):
            s = 0
            if type(lista) == Matriz:
                lista = lista.contenido_matriz
            for i in range (len(lista)):
                s += lista[i]
            return s 

    
        magica = False
        if self.es_cuadrada():
            a = _suma_lista(self.columna(1))
            if _suma_lista(self.diagonal_principal()) == _suma_lista(self.diagonal_opuesta()) == a:
                magica = True
            for i in range (1,self.columnas+1):
                if _suma_lista(self.columna(i)) != a or _suma_lista(self[i]) != a:
                    magica = False
        return magica  
                

          
if __name__ == "__main__":
    # Este script prueba diferentes funcionalidades para 
    # comprobar rápidamente que todo funiona correctamente.

    otramatriz = Matriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    matriz2 = Matriz([[5,6,7,8],[9,10,11,12],[1,2,3,4]])

    # 1. Definición de una matriz a partir de sus dimensiones.
    mimatriz = Matriz(2,3)

    # 2.a Asignación de un elemento.
    otramatriz[1][1] = 1337

    # 2.b Obtención de un elemneto.
    print(otramatriz[1][1])

    # 3. Presentación de una matriz.
    otramatriz.print() 
    print(otramatriz)

    # 4. Obtención de una matriz por teclado.
    mimatriz.pide_matriz()

    # 5.a Obtención de una fila de la matriz.
    print(matriz2[1])
    print(matriz2.fila(1))

    # 5.b Obtención de una columna de la matriz.
    print(otramatriz.traspuesta()[1])
    print(otramatriz.columna(1))
    
    # 5.c Obtención de la diagonal de la matriz.
    print(otramatriz.diagonal_principal())
    print(otramatriz.diagonal_principal(2)) # El 2 indica que es la diagonal que empieza en la columna 3
    print(otramatriz.diagonal_principal(-1)) # El -1 indica que es la diagonal que empieza en la fila 2

    # 6. Obtención de las dimensiones de la matriz.
    print(otramatriz.dimension())

    # 7.a Suma de matrices.
    print(otramatriz+matriz2)

    # 7.b Resta de matrices.
    print(otramatriz-matriz2)

    # 8. Matriz opuesta (Preguntar si -A es correcto).
    print(otramatriz.opuesta())

    # 9. Producto de matrices.
    print(mimatriz*otramatriz)

    # 10. Producto de un escalar por una matriz.
    print(otramatriz*2)

    # 11.a Matriz nula a partir de las dimensiones dadas.
    print(Matriz(3,2,tipo_matriz='nula'))

    # 11.b Matriz identidad a partir de las dimensiones dadas.
    In3 = Matriz(3,3,tipo_matriz='identidad')

    # 12. Matriz traspuesta.
    print(otramatriz.traspuesta())

    # 13. Caracterización de matrices: determinación de las condiciones de matriz cuadrada, fila, columna, simétrica, triangular superior y triangular inferior.
    In3.tipo()
    print(In3.es_fila())
    print(In3.es_columna())
    print(In3.es_triangular_inf())
    print(In3.es_triangular_sup())
    print(In3.es_cuadrada())
    print(In3.es_simetrica())
    
    # 14. Matriz mágica.
    print(otramatriz.es_magica())
    magica = Matriz([[8,1,6],[3,5,7],[4,9,2]])
    print(magica.es_magica())

    # 15.a Obtención del mayor valor
    print(otramatriz.mayor())

    # 15.b Obtención del menor valor
    print(otramatriz.menor())

    # 15.c Obtención del la media de los valores de los elementos
    print(otramatriz.media())
                                                

    # Guardar la matriz en un archivo
    Matriz().guardar('matrices.csv', [otramatriz, matriz2])

    # Cargar la matriz desde un archivo             
    A, B = Matriz().cargar('matrices.csv')
    print(A)
    print(B)