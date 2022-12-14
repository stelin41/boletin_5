"""
Autores:
    - José Romero Conde
    - Stevan Lino Gartz

Propósito:
    Esta librería puede realizar operaciones con matrices.

"""

class Matriz:

    def __init__(self, *args):
        """
        Declaración de una matriz.
        Puede declararse una matriz de dos formas:
            Matriz(filas, columnas) # filas y columnas son enteros mayores que 0
            Matriz(contenido_matriz) # contenido_matriz de tipo lisa
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

            # Se hace de este modo para evitar que se guarden referencias a la misma
            # dirección de memoria y que a la hora de modificar la matriz se
            # modifique de una manera no deseada
            for j in range(self.filas):
                fila = Matriz([None] * self.columnas)
                self.contenido_matriz.append(fila)

        else:
            raise Exception('Hay que especificar las dimensiones de la matriz o su contenido.')

                
    """
    def __str__(self):
        #Presentación del estado actual de la matriz.

        imprimir = ""

        # Se busca los valores con más caracteres de cada columna, para así
        # decidir el número de espacios en blanco que los separa.
        longitud_maxima = []
        for j in range(self.columnas):
            valores = []
            for i in range(self.filas):
                valores.append(len(str(self.contenido_matriz[i][j])))

            longitud_maxima.append(max(valores))

        for i in range(self.filas):
            for j in range(self.columnas):
                # Se mide la diferencia entre el elemento con más caracteres de
                # la columna y el actual. Esa diferencia +1 es el número de
                # espacios que aparecen después del elemento para que esté
                # correctamente presentado.
                longitud_elemento_actual = len(str(self.contenido_matriz[i][j]))
                espaciado = longitud_maxima[j]-longitud_elemento_actual+1
                if j==0:
                    if i==0:
                        imprimir += "/ " +str(self.contenido_matriz[i][j]) + " "*espaciado

                    elif i==self.filas-1:
                        imprimir += "\\ " +str(self.contenido_matriz[i][j]) + " "*espaciado

                    else:
                        imprimir += "| " +str(self.contenido_matriz[i][j]) + " "*espaciado

                elif j==self.filas:

                    if i==0:
                        imprimir += str(self.contenido_matriz[i][j]) + " "*espaciado + "\\"

                    elif i==self.filas-1:
                        imprimir += str(self.contenido_matriz[i][j]) + " "*espaciado + "/"

                    else:
                        imprimir += str(self.contenido_matriz[i][j]) + " "*espaciado + "|"

                else:imprimir += str(self.contenido_matriz[i][j]) + " "*espaciado
            imprimir += "\n"

        return imprimir
    """

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
        for i in min([self.filas, self.columnas]):
            elementos_diagonal.append(self.contenido_matriz[i][i])
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
    

    def es_triangular_inf(self):
        triangular_inf = True
        for i in range (1,self.filas+1):
            for j in range (1,self.columnas+1):
                if i>j and self[i][j] != 0:
                    triangular_inf = False
        return triangular_inf
                        
    
    def tipo(self):
        fila = self.fila == 1
        columna = self.columna == 1
        cuadrada = self.columna == self.fila
        tri_inf = False
        tri_sup = False
        diagonal = False
        if cuadrada:
            if self == self.traspuesta():
                simetrica = True 
            if self.es_triangular_inf():
                tri_inf = True
            if self.traspuesta().es_triangular_inf():
                tri_sup = True
            if tri_inf and tri_sup:
                diagonal



if __name__ == "__main__":
    # Este script prueba diferentes funcionalidades para comprobar rápidamente que
    # todo funiona correctamente

     
    # Declaración de matrices
    mimatriz = Matriz(2,3)
    otramatriz = Matriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    otramatriz[1][1] = 1337
    print(otramatriz)

    mimatriz.pide_matriz()
    print(mimatriz)
    
    print("Producto:\n",mimatriz*otramatriz)
    print(mimatriz.opuesta())

                                                  
   
