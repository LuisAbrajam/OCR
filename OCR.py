import matplotlib.image as mpimagen ##sirve para trabajar con imagenes como matlab
import os#El módulo os nos permite acceder a funcionalidades dependientes del Sistema Operativo. 
         #Sobre todo, aquellas que nos refieren información sobre el entorno del mismo y 
         #nos permiten manipular la estructura de directorios (para leer y escribir archivos
import csv#Libreria para el manejo de archivos csv

 
#Razón de nFilas/nColumnas  recibimos como parametro las dimensiones de la matriz que conforma la imagen
def RazonFilasnColumnas(Dimensiones):
    
    #Definimos una variable en la cual se almacenara el resultado  de dividir las filas entre las columnas
    RelacionEntreFilasyColumnas=Dimensiones[0]/Dimensiones[1]
    #Imprimimos la variable que almacena el resultado de nFilas/nColumnas de la imagen
    print(RelacionEntreFilasyColumnas)
    #Retornamos nuestra variable
    return RelacionEntreFilasyColumnas

#Funcion para calcular cuntos pixeles conforman la figura en la imagen
#Recibimos como parametros imagen y Dimensiones         
def PixelesQueConformanElAreaDeLaFigura(imagen,Dimensiones):
    #Declaramos un contador el cual inicializamos en 0
    ContadorDePixelesQueConformanElAreaDeLaFigura=0
    #Utilizamos un ciclo for para recorrer las Filas de la matriz asignando un rango que va desde 0 hasta el numero de columnas que conforman la matriz
    for i in range(0,Dimensiones[0]):
        #Utilizamos un segund ciclo for para recorrer las columnas que conforman la matriz
       for j in range(0,Dimensiones[1]):
           #Utilizamos una condicion en la cual decimos que el valor almacenado en la matriz en la posicion [i][j] es diferente de 0  nos aumente el contador
           #de pixeles  que conforman la figura en la imagen
           if(imagen[i][j]!=0):

              ContadorDePixelesQueConformanElAreaDeLaFigura=ContadorDePixelesQueConformanElAreaDeLaFigura+1
    #Imprimimos el contador y este nos arrojara el numero de veces en la que la condicion se cumplio lo que significa el numero de pixeles que conforman la figura en la  imagen          
    print(ContadorDePixelesQueConformanElAreaDeLaFigura)
    #Retornamos nuestra variable           
    return ContadorDePixelesQueConformanElAreaDeLaFigura
#Esta funcion es para encontrar a traves de una posicion situada a un cuarto en relacion a las filas de la matriz las veces en las que hubo un cambio 
#Recibimos como parametros imagen y Dimensiones
def NumeroDeCambiosEfectuadosEnLaFilaPosicionadaAUnCuarto(imagen,Dimensiones):
    #Declaramos una variable la cual almacenara un valor entero dado por la obtencion del Dimensiones del numero de filas entre un valor de 4 para obtener la posicion a un cuarto de la matriz
    PosicionDeLaFilaAunCuarto = int(Dimensiones[0]/4)
    #Declaramos un contador que inicializamos en 0
    ContadorDeCambiosEnLaFilaAunCuarto=0
    #Declaramos una variable auxiliar a la cual asignaremos el valor que contenga la posicion en que inicializamos el recorrido de la matriz para encontrar los cambios efectuados ahi
    aux=imagen[PosicionDeLaFilaAunCuarto][0]
    #inicializamos nuestro ciclo para recorrer las columnas de la matriz
    for i in range(0,Dimensiones[1]):
        #Declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz realice algo
        
        if(aux!=imagen[PosicionDeLaFilaAunCuarto][i]):
            #Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            aux=imagen[PosicionDeLaFilaAunCuarto][i]
            #Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
            ContadorDeCambiosEnLaFilaAunCuarto=ContadorDeCambiosEnLaFilaAunCuarto+1
        #imagen[FilaPosicionadaAunCuarto][i]=1
    #Imprimimos el contador de cambios         
    print(ContadorDeCambiosEnLaFilaAunCuarto)
    #Retornamos nuestra el resultado de nuestra variable
    return ContadorDeCambiosEnLaFilaAunCuarto
#Esta funcion es para encontrar a traves de una posicion situada a la mitad en relacion a las filas de la matriz las veces en las que hubo un cambio
def NumeroDeCambiosEfectuadosEnLaFilaCentral(imagen,Dimensiones):
    #Declaramos una variable la cual almacenara un valor entero dado por la obtencion del Dimensiones del numero de filas entre 2
    PosicionDeLaFilaCentral=int(Dimensiones[0]/2)
    #Declaramos un contador para determinar el numero de cambios que hubo en el recorrido de la matriz y  que inicializamos en 0
    ContadorDeCambiosEnLaFilaCentral=0
    #Declaramos una variable auxiliar a la cual asignaremos el valor que contenga la posicion en que inicializamos el recorrido de la matriz para encontrar los cambios efectuados ahi
    aux=imagen[PosicionDeLaFilaCentral][0]
    #inicializamos nuestro ciclo para recorrer las columnas de la matriz
    for i in range(0,Dimensiones[1]):
        #Declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz realice algo       
        if(aux!=imagen[PosicionDeLaFilaCentral][i]):
          #Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz  
          aux=imagen[PosicionDeLaFilaCentral][i]
          #Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
          ContadorDeCambiosEnLaFilaCentral=ContadorDeCambiosEnLaFilaCentral+1
        #imagen[mitadHo][i]=1   
    #Imprimimos el contador de cambios       
    print(ContadorDeCambiosEnLaFilaCentral)
    return ContadorDeCambiosEnLaFilaCentral
#Esta funcion es para encontrar a traves de una posicion situada a la mitad en relacion a las filas de la matriz las veces en las que hubo un cambio 
def NumeroDeCambiosEfectuadosEnLaFilaPosicionadaATresCuartos(imagen,Dimensiones):
    #Declaramos una variable la cual almacenara un valor entero dado por la obtencion del Dimensiones del numero de filas entre 4 y multiplicado por tres para obtener la posicion a Tres Cuartos
    PosicionDeLaFilaATresCuartos=int((Dimensiones[0]/4)*3)
    #Declaramos un contador para determinar el numero de cambios que hubo en el recorrido de la matriz y  que inicializamos en 0
    ContadorDeCambiosEnLaFilaATresCuartos=0
    #Declaramos una variable auxiliar a la cual asignaremos el valor que contenga la posicion en que inicializamos el recorrido de la matriz 
    aux=imagen[PosicionDeLaFilaATresCuartos][0]
    #inicializamos nuestro ciclo para recorrer las Columnas de la matriz
    for i in range(0,Dimensiones[1]):
        if(aux!=imagen[PosicionDeLaFilaATresCuartos][i]):
            aux=imagen[PosicionDeLaFilaATresCuartos][i]
            ContadorDeCambiosEnLaFilaATresCuartos=ContadorDeCambiosEnLaFilaATresCuartos+1
        #imagen[TLinea][i]=1    
    print(ContadorDeCambiosEnLaFilaATresCuartos)
    
    return ContadorDeCambiosEnLaFilaATresCuartos    
#En esta funcion calculamos en que posisicion se encuentra un cuarto de la matriz con respecto a lñas columnas
#Recibimos como parametros imagen y Dimensiones    
def NumeroDeCambioEfectuadosEnLaColumnaAUnCuarto(imagen,Dimensiones):
    #Declaramos una variable la cual almacenara un valor entero dado por la obtencion de Dimensiones del numero de columnas entre 4  para obtener la posicion a un  Cuarto
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/4)
    #Declaramos un contador para determinar el numero de cambios que hubo en el recorrido de la matriz y  que inicializamos en 0
    ContadorDeCambiosEnLaColumnaAUnCuarto=0
    #Declaramos una variable auxiliar a la cual asignaremos el valor que contenga la posicion en que inicializamos el recorrido de la matriz 
    aux=imagen[0][PosicionDeLaColumnaAUnCuarto]
    for i in range(0,Dimensiones[0]):
        if(aux!=imagen[i][PosicionDeLaColumnaAUnCuarto]):
            aux=imagen[i][PosicionDeLaColumnaAUnCuarto]
            ContadorDeCambiosEnLaColumnaAUnCuarto=ContadorDeCambiosEnLaColumnaAUnCuarto+1
        #imagen[i][pv]=1    
    print(ContadorDeCambiosEnLaColumnaAUnCuarto)
    return ContadorDeCambiosEnLaColumnaAUnCuarto
#En esta funcion calculamos la posiscion que ocupa la columna central de la matriz 
#Dividiendo entre 2 el total de las columnas 
#con ello pretendemos saber cuantas veces hubo un cambio en esa columna    
def NumeroDeCambioEfectuadosEnLaColumnaCentral(imagen,Dimensiones):
    PosicionDeLaColumnaCentral=int(Dimensiones[1]/2)
    ContadorDeCambiosEnLaColumnaCentral=0
    aux=imagen[0][PosicionDeLaColumnaCentral]
    for i in range(0,Dimensiones[0]):
        
        if(aux!=imagen[i][PosicionDeLaColumnaCentral]):
            aux=imagen[i][PosicionDeLaColumnaCentral]
            ContadorDeCambiosEnLaColumnaCentral=ContadorDeCambiosEnLaColumnaCentral+1
        #imagen[i][V]=1
    print(ContadorDeCambiosEnLaColumnaCentral)
    #Retornamos la variable que contiene el resultado de los cambios efectuados 
    return ContadorDeCambiosEnLaColumnaCentral
#En esta funcion calculamos la posiscion que ocupa la columna a tres cuartos  de la matriz
#Dividiendo el total de las columnas entre 4 y multiplicandola por 3
#utilizaremos nuevamente una variable auxiliar la cual no ayudara encontrar los cambios que se generan en esa parte de la matriz
def NumeroDeCambioEfectuadosEnLaColumnaATresCuartos(imagen,Dimensiones):
    PosicionDeLaColumnaATresCuartos=int((Dimensiones[1]/4)*3)
    ContadorDeCambiosEnLaColumnaATresCuartos=0
    aux=imagen[0][PosicionDeLaColumnaATresCuartos]
    for i in range(0,Dimensiones[0]):
        if(aux!=imagen[i][PosicionDeLaColumnaATresCuartos]):
            aux=imagen[i][PosicionDeLaColumnaATresCuartos]
            ContadorDeCambiosEnLaColumnaATresCuartos=ContadorDeCambiosEnLaColumnaATresCuartos+1
        #imagen[i][TV]=1
    print(ContadorDeCambiosEnLaColumnaATresCuartos)
    #Retornamos la variable que contiene el resultado de los cambios efectuados 
    return ContadorDeCambiosEnLaColumnaATresCuartos
#En esta funcion calculamos la posicion a un cuarto de la matriz y los pixeles que forman parte de la figura en esta columna  
def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto(imagen,Dimensiones):
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/4)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto=0
    
    for i in range(0,Dimensiones[0]):
        #La condicion espara que cada que encuetre un valor distinto a 0 lo tome en cuenta
        if(imagen[i][PosicionDeLaColumnaAUnCuarto]!=0):
            #el contador aumentara cada que la ondicion detecte un valor diferente a 0
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto+1
        #imagen[i][PLV]=1    
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto)   
    #Retornamos la variable que alverga el resultado calculado en la funcion
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto
#En esta funcion calculamos la posicion de la columna central de la matriz 
#Contamos los pixeles que conforman la figura en esta columna     
def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral(imagen,Dimensiones):
    #Declaramos una variable que alberga un valor entero calculado a partir de la divicion entre el total de columnas entre 2    
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/2)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral=0
    #El ciclo recorre las filas
    for i in range(0,Dimensiones[0]):
        #La condicion espara que cada que encuetre un valor distinto a 0 lo tome en cuenta

        if(imagen[i][PosicionDeLaColumnaAUnCuarto]!=0):
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral+1
        #imagen[i][ML]=1    
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral)
    #Retornamos la variable que contiene el resultado calculado de los pixeles en la columna
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral
#En esta funcion calculamos la posicion de la columna situada a tres cuartos de la matriz
#Dividiendo el total de las columnas entre 4 y multiplicandola por 3 almacenando el resultado en 
#una variable de tipo entero     
def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos(imagen,Dimensiones):
    PosicionDeLaColumnaATresCuartos=int((Dimensiones[1]/4)*3)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos=0
    #El ciclo recorre las filas
    for i in range(0,Dimensiones[0]):
        #La condicion es para detectar dentro del la columna que hemos especificado 
        #Los pixeles que conforman la imagen 
        if(imagen[i][PosicionDeLaColumnaATresCuartos]!=0):
            #Cada que la condicion se cumpla un contador ira en aumento 
            #obtendremos el numero de pixeles en esa columna que forman parte de la figura
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos+1
        #imagen[i][TLV]=1    
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos) 
    #Retornamos la variable que contiene el reusultado de pixeles 
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos
#En esta funcion calculamos la posicion de la fila situada a un cuartos de la matriz
#Dividiendo el total de filas entre 4 el resultado lo guardamos en una variable de tipo entero    
def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaAUnCuarto(imagen,Dimensiones):
    PosicionDeLaFilaAUnCuarto=int(Dimensiones[0]/4)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos=0
    #Recorremos las columnas 
    for i in range(0,Dimensiones[1]):
        #La condicion es para detectar dentro del la fila que hemos especificado 
        #Los pixeles que conforman la imagen 
        if(imagen[PosicionDeLaFilaAUnCuarto][i]!=0):
            #Cada que la condicion se cumpla un contador ira en aumento 
            #obtendremos el numero de pixeles en esa fila que forman parte de la figura
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos+1
        #imagen[PLH][i]=1    
    #Imprimimos el resultado del contador        
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos)
    #Retornamos la variable que contiene el resultado de los pixeles 
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos
#En esta funcion calculamos la posicion que ocupa la fila central de la matriz 
#Guardamos en resultado en una variable de tipo entero al dividir el total de filas entre 2
def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaCentral(imagen,Dimensiones):
    PLH=int(Dimensiones[0]/2)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral=0
    #Recorremos las columas
    for i in range(0,Dimensiones[1]):
        #La condicion es para detectar dentro del la fila que hemos especificado 
        #Los pixeles que conforman la imagen 
        if(imagen[PLH][i]!=0):
            #Cada que la condicion se cumpla un contador ira en aumento 
            #obtendremos el numero de pixeles en esa fila que forman parte de la figura
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral+1
        #imagen[PLH][i]=1
    #Imprimimos el resultado del contador        
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral) 
    #Retornamos la variable que contiene el resultado de los pixeles
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral
#En esta funcion calculamos la posicion que ocupa la fila a tres cuartos de la matriz 
#Guardamos en resultado en una variable de tipo entero al dividir el total de filas entre 4 y multiplicamos por 3    
def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaATresCuartos(imagen,Dimensiones):
    PLH=int((Dimensiones[0]/4)*3)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos=0
    #Recorremos las columas
    for i in range(0,Dimensiones[1]):
        #Cada que la condicion se cumpla un contador ira en aumento 
        #obtendremos el numero de pixeles en esa fila que forman parte de la figura
        if(imagen[PLH][i]!=0):
            #Cada que la condicion se cumpla un contador ira en aumento 
            #obtendremos el numero de pixeles en esa fila que forman parte de la figura
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos+1
       # imagen[PLH][i]=1  
       #Imprimimos el contador     
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos)
    #Retornamos la variable que contiene el resultado de los pixeles
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos

#En esta funcion recibimos como parametros las variables que contienen los resultados de las funciones anteriores
#para comenzar a generar en un documento todas las caracteristicas de las imagenes que se usaran como instancias
def GenerarDataSet(RazonFilasnColumnas,PixelesQueConformanElAreaDeLaFigura,NumeroDeCambiosEfectuadosEnLaFilaPosicionadaAUnCuarto,NumeroDeCambiosEfectuadosEnLaFilaCentral,NumeroDeCambiosEfectuadosEnLaFilaPosicionadaATresCuartos,NumeroDeCambioEfectuadosEnLaColumnaAUnCuarto,NumeroDeCambioEfectuadosEnLaColumnaCentral,NumeroDeCambioEfectuadosEnLaColumnaATresCuartos,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaAUnCuarto,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaCentral,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaATresCuartos):
#Designamos la carpeta en la cual se comenzara el recorrido de subcarpetas que contienen lasimagnes 
    Carpeta='arialSegmented'
#Creamos el archivo con la extencion csv 
    Archivo=open('DataSet.csv','w',newline='')
#Como salida obtenemos el archivo que fue escrito con las caracteristicas obtenidas del conjunto de imagenes
    salida=csv.writer(Archivo)
#Esta variable es un contador que aumentara conforme entra a otra subcarpeta para extraer las caracteristicas del conjunto de imagenes que alberga
    clase=-1
#Declaramos un ciclo for para recorrer la carpeta,subcarpetas y archivos que se encuentran en la carpeta raiz
    for dir, subdirlist, filelist in os.walk(Carpeta):
    #Un segundo ciclo  for para recorrer imagen por imagen dentro de una lista de imagenes     
      for fname in filelist:
        
        #Asignamos a una variable la direccion y el nombre de la imagen que se le  extraeran sus caracteristicas 
        Direccionimagen=dir+'/'+fname
        
        imagen=mpimagen.imread(Direccionimagen)
        #Mostramos la imagen
        #imagenplot=plt.imshow(imagen)
        
        
#Utilizamos el atributo shape para retornar las dimensiones de la matriz que conforma la imagen
#Asignamos el Dimensiones de la matriz a una variable llamada Dimensiones 
        Dimensiones=imagen.shape
        print('Dimensiones de la imagen ',Dimensiones)
     #Mandamos a llamar nuestras funciones para mostrar los procesos de calculo que se efectuaron    
     #Declaramos variables y  asignamos  el valor que se generaron en cada funcion    
        FilaEntreColumna = RazonFilasnColumnas(Dimensiones)
        AreaDeLaFigura = PixelesQueConformanElAreaDeLaFigura(imagen,Dimensiones)
        NumeroDeCambiosFilaUcCuarto = NumeroDeCambiosEfectuadosEnLaFilaPosicionadaAUnCuarto(imagen,Dimensiones)     
        NumeroDeCambiosFilaCentral = NumeroDeCambiosEfectuadosEnLaFilaCentral(imagen,Dimensiones)
        NumeroDeCambiosFilaTresCuartos = NumeroDeCambiosEfectuadosEnLaFilaPosicionadaATresCuartos(imagen,Dimensiones)
        NumeroDeCambiosColumnasaUCuarto = NumeroDeCambioEfectuadosEnLaColumnaAUnCuarto(imagen,Dimensiones)
        NumeroDeCambiosColumnCentral = NumeroDeCambioEfectuadosEnLaColumnaCentral(imagen,Dimensiones)
        NumeroDeCambiosColumnaTresCuartos = NumeroDeCambioEfectuadosEnLaColumnaATresCuartos(imagen,Dimensiones)
        NumeroPixelesColumnaUnCuarto = NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto(imagen,Dimensiones)
        NumeroPixelesColumnaCentral = NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral(imagen,Dimensiones)
        NumeroPixelesColumnaTresCuartos = NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos(imagen,Dimensiones)
        NumeroPixelesFilaUnCuarto = NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaAUnCuarto(imagen,Dimensiones)
        NumeroPixelesFilaCentral = NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaCentral(imagen,Dimensiones)
        NumeroPixelesFilaTresCuartos = NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaATresCuartos(imagen,Dimensiones)
      #Esta linea nos sirve para ir escribiendo los valores dentro del archivo que creamos anteriormente
      #entre parentesis y corchetes se colocan las variables que almacenan los recultados 
      #Estos se dejara de efectuar hasta que no encuentre mas resultados que almacenar en el documento   
        salida.writerow([FilaEntreColumna,AreaDeLaFigura,NumeroDeCambiosFilaUcCuarto,
                         NumeroDeCambiosFilaCentral, NumeroDeCambiosFilaTresCuartos, 
                         NumeroDeCambiosColumnasaUCuarto, NumeroDeCambiosColumnCentral, 
                         NumeroDeCambiosColumnaTresCuartos, NumeroPixelesColumnaUnCuarto,
                         NumeroPixelesColumnaCentral,NumeroPixelesColumnaTresCuartos,
                         NumeroPixelesFilaUnCuarto,NumeroPixelesFilaCentral,NumeroPixelesFilaTresCuartos,clase])
    #La variable clase hace referencia a las subcarpetas que va analizando el codigo para ir obteniendo las caracteristicas del conjunto de imagenes
    #Esta ira aunmentado de uno en uno cada que analice una nueva subcarpeta                     
      clase=clase+1
    print(clase)
#Cerramos el archivo una vez que se termina de generar el socumento     
    Archivo.close()
    #Retornamos la imagen y las dimensiones de cada una
    return(imagen,Dimensiones)                               

#Mandamos a llamar nuestra funcion principal que es la de generar dataset para que esta ejecute todas las demas funciones.    
GenerarDataSet(RazonFilasnColumnas,PixelesQueConformanElAreaDeLaFigura,NumeroDeCambiosEfectuadosEnLaFilaPosicionadaAUnCuarto,NumeroDeCambiosEfectuadosEnLaFilaCentral,NumeroDeCambiosEfectuadosEnLaFilaPosicionadaATresCuartos,NumeroDeCambioEfectuadosEnLaColumnaAUnCuarto,NumeroDeCambioEfectuadosEnLaColumnaCentral,NumeroDeCambioEfectuadosEnLaColumnaATresCuartos,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaAUnCuarto,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaCentral,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaATresCuartos)