import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as mpatches

# ******************************************************************************************************************
# ******************************************************************************************************************
# IMPORTANTE: 
# La solución a entregar DEBE implementar los 8 requerimientos descritos en el enunciado del proyecto.
# Una entrega que solo implemente el requerimiento 4 y 8, estaría incompleta y no le permitiría practicar
# todos los conceptos aprendidos en el Nivel 4 del curso, en preparación para el Examen Final.
# ******************************************************************************************************************
# ******************************************************************************************************************


# Requerimiento 1:
def cargar_datos(ruta:str)->pd.DataFrame:
    data = pd.read_csv(ruta)
    return data
data = cargar_datos("icfes.csv")
print(data)
#print(cargar_datos("icfes.csv"))
# Requerimiento 2:
def grafico_barras(data:pd.DataFrame):
    anios = data["anio_nacimiento"].value_counts() 
    anios.plot(kind="bar")
    plt.show()



def practica_de_pandas(data:pd.DataFrame,anio:int)->pd.DataFrame:
    """
    "dado los diferentes departamentos contar cuantos presentaron el exmaen en un año especifico y cual es su promedio
    - graficar pie de torta"
    """
    dataframe = data[(data["anio_nacimiento"] == anio) ] #Filtro
    agrupados = dataframe.groupby("departamento_residencia")["puntaje_global"].mean().sort_values(ascending=False)
    agrupados.head().plot(kind="pie",title="")
    print(agrupados)

    
print(practica_de_pandas(data, 2003))
# Requerimiento 3:
def torta_por_requerimientos(data:pd.DataFrame,anio:int):
    anios = data[data["anio_nacimiento"] == anio]
    mejores = anios["departamento_residencia"].value_counts().head()
    mejores.plot(kind="pie",figsize= (12,10),autopct="%1.1f%%",legend = True,labels = None, title ="La gorda")
    plt.tight_layout()
    plt.show()
    
#print(torta_por_requerimientos(data, 2001))
# Requerimiento 4:
def crear_matriz_estudiantes_por_departamento_y_anio(dataframe: pd.DataFrame) -> tuple:
    """
    Crea una matriz que representa la cantidad de estudiantes por departamento y año de nacimiento.

    Parámetros:
        dataframe (pd.DataFrame): DataFrame que contiene la información de la prueba ICFES Saber 11.
        
    Nota:
        - Se provee el código que crea las listas de departamentos y anios.

    Retorno:
        tuple: Una tupla que contiene:
            - list: Matriz bidimensional con la cantidad de estudiantes 
                        por departamento (filas) y año de nacimiento (columnas).
            - list: Lista de departamentos ordenados en el mismo orden que aparecen en la matriz.
            - list: Lista de años de nacimiento ordenados en el mismo orden que aparecen en la matriz.
    """
    deptos = dataframe["departamento_residencia"].sort_values().unique().tolist()
    anios = dataframe["anio_nacimiento"].sort_values().unique().tolist()
    matriz = []
    for i in range(0,len(deptos)):
        fila = []
        for j in range(0,len(anios)):
            fila.append(0)
        matriz.append(fila)
     
    departamentos = dataframe["departamento_residencia"].tolist()
    años = dataframe["anio_nacimiento"].tolist()
    
    for i in range(0,len(departamentos)):
        depto_actual = deptos.index(departamentos[i])
        anio_actual = anios.index(años[i])
        matriz[depto_actual][anio_actual] += 1
        
    return matriz,deptos,anios 

tupla = crear_matriz_estudiantes_por_departamento_y_anio(data)
#print(tupla)
# Requerimiento 5:
def cantidad_promedio_por_añto(tupla:tuple,anio:int)-> int:
    promedio = 0
    contadores = 0
    matriz,deptos,anios = tupla
    if anio in anios:
       i = 0 
       col = anios.index(anio)
       while i < len(matriz):
         if matriz[i][col] != 0 :
            promedio += matriz[i][col]
            contadores += 1
         i += 1   
    promedio = round(promedio/contadores)
    return promedio
#print(cantidad_promedio_por_añto(tupla, 2001))
# Requerimiento 6:
def cantidad_promedio_por_año(tupla:tuple)->dict:
    años = {}
    matriz,deptos,anios = tupla
    for i in range(0,len(anios)):
        promedio = cantidad_promedio_por_añto(tupla,anios[i])
        if anios[i] not in años and promedio != 0:
           años[anios[i]] = promedio
    return años       
#print(cantidad_promedio_por_año(tupla))

# Requerimiento 7: 
def primer_superior(umb:int,tupla:tuple)->tuple:
    matriz,deptos,anios = tupla
    i = 0 
    pos_col = None
    pos_fila = None
    cantidad = None
    encontrado = False
    while i < len(matriz) and encontrado == False:
        j = 0 
        while j < len(matriz[i]) and encontrado == False:
            if matriz[i][j] > umb:
               encontrado = True
               cantidad = matriz[i][j]
               pos_col = anios[j]
               pos_fila = deptos[i]
            j += 1   
        i += 1
    return (cantidad,pos_col,pos_fila)

#print(primer_superior(102, tupla))
# Funcion auxiliar para el Requerimiento 8 (no debe modificar esta función):
def cargar_coordenadas(nombre_archivo: str) -> dict:
    """
    Carga las coordenadas (x, y) de los departamentos de Colombia desde un archivo de texto.

    El archivo de texto tiene el siguiente formato:
    DEPARTAMENTO;x;y
    AMAZONAS;100;200
    ANTIOQUIA;300;400 
    ...
    
    Parámetros:
        nombre_archivo (str): Nombre del archivo de texto que contiene las coordenadas de los departamentos.

    Retorno:
        dict: Diccionario donde las llaves son los nombres de los departamentos y los valores son tuplas
              con las coordenadas (x, y) de cada departamento.
    """   
    deptos = {}
    archivo = open(nombre_archivo, encoding="utf8")
    archivo.readline()
    linea = archivo.readline()
    
    while len(linea) > 0:
        linea = linea.strip()
        datos = linea.split(";")
        deptos[datos[0]] = (int(datos[1]),int(datos[2]))
        linea = archivo.readline()

    archivo.close()
    
    return deptos


# Requerimiento 8:
def cargar_imagen(ruta_mp:str,coordenadas:str,tupla:tuple,anio:int):
    matriz,deptos,anios = tupla
    colores = {  "0-100": [0.0, 0.0, 0.0],  "101-1000": [1.0, 0.0, 0.0],  "1001-2000": [1.0, 0.6, 0.0],
                "2001-5000": [1.0, 1.0, 0.0], "5001-10000": [0.6, 1.0, 0.6], ">10000": [0.0, 0.5, 0.0]  } 
    
    mapa = plt.imread(ruta_mp).tolist()
    coordenadas_x_y  = cargar_coordenadas(coordenadas)
    if anio in anios:
       i = 0
       pos = anios.index(anio)
       while i < len(matriz):
           color = []
           cantidad = matriz[i][pos]
           if cantidad < 101:
              color = colores["0-100"] 
           elif cantidad < 1001:
              color = colores["101-1000"]
           elif cantidad < 2001:
              color = colores["1001-2000"]
           elif cantidad < 5001:
              color = colores["2001-5000"]
           elif cantidad < 10001:
              color = colores["5001-10000"]
           else:
               color = colores[">10000"]
               
           depto = deptos[i]
           if depto in coordenadas_x_y:
              x,y = coordenadas_x_y[depto]
              for k in range(x-7,x+7):
                  for l in range(y-7,y+7):
                      mapa[k][l] = color
           i += 1
               
    legends = []
    for i in colores:
        legends.append(mpatches.Patch(color=colores[i],label=i))

    plt.legend(handles=legends,loc=3,fontsize="large")
    plt.title("Cantidad de estudaintes nacidos en {} que presentaron la prueba".format(anio),fontsize = "large")
    plt.figure(figsize=(10,10))
    plt.tight_layout()
    plt.show()
    plt.imshow(mapa)
 
#print(cargar_imagen("mapa.png", "coordenadas.txt", tupla, 2003))
    
    
    
    