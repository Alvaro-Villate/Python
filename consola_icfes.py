import icfes as ic
import pandas as pd

##### Funciones auxiliares (NO MODIFICAR):
def imprimir_matriz(matriz_info: tuple) -> None:
    """
    Imprime la matriz de estudiantes por departamento y año de nacimiento.
    
    Parámetros:
        - info_matriz (tuple): Tupla que contiene:
            - list: Matriz bidimensional con la cantidad de estudiantes por departamento (filas) y año de nacimiento (columnas).
            - list: Lista de departamentos ordenados en el mismo orden que aparecen en la matriz.
            - list: Lista de años de nacimiento ordenados en el mismo orden que aparecen en la matriz.

    La función imprime la matriz en un formato tabular. 
    """
    if matriz_info is not None and len(matriz_info) == 3:
        matriz, departamentos, anios = matriz_info
        if matriz and departamentos and anios:
            print("\nMatriz de estudiantes por departamento y año de nacimiento:")

            # Obtener el ancho máximo de la columna de los departamentos
            # Buscando el ancho máximo de los departamentos
            ancho_departamento = None
            for departamento in departamentos:
                if ancho_departamento is None or len(departamento) > ancho_departamento:
                    ancho_departamento = len(departamento)

            # Buscando el ancho máximo de los años para las columnas de los años
            ancho_anio = None
            for anio in anios:
                anio = str(anio)
                if ancho_anio is None or len(anio) > ancho_anio:
                    ancho_anio = len(anio)
            header = "Deptos/Años".ljust(ancho_departamento + 2)
            
            # Construir el encabezado con los años
            for anio in anios:
                anio = str(anio)
                header += anio.rjust(ancho_anio + 2)

            border = "+" + "-" * (len(header) + 1) + "+"
            print(border)
            print("| " + header + "|")
            print(border)
            
            # Armar cada fila de la matriz teniendo en cuenta el ancho de los departamentos y años
            for i in range(len(departamentos)):
                fila = departamentos[i].ljust(ancho_departamento + 2)
                for j in range(len(anios)):
                    fila += str(matriz[i][j]).rjust(ancho_anio + 2)
                print("| " + fila + "|")
            print(border)


def mostrar_promedio_estudiantes(promedio_estudiantes: dict) -> None:
    """
    Imprime la cantidad promedio de estudiantes que tomaron la prueba ICFES por año de nacimiento.
    
    Parámetros:
        - promedio_estudiantes (dict): Diccionario con el año de nacimiento como llave y la cantidad promedio de estudiantes como valor.

    La función imprime el promedio de estudiantes por año de nacimiento.
    """
    print("\nCantidad promedio de estudiantes por año de nacimiento:")
    print("-" * 50)

    if promedio_estudiantes is not None and promedio_estudiantes != {}:
        for anio in promedio_estudiantes:
            cantidad = promedio_estudiantes[anio]
            print("*" * 50)
            print("Año de nacimiento:", anio)
            print("Cantidad promedio de estudiantes:", cantidad)

    print("*" * 50)

##### Fin de las funciones auxiliares



dataframe_icfes = ic.cargar_datos("icfes.csv")
# Ejecución del Requerimiento 2:
def ejecutar_graficar_cantidad_estudiantes_por_anio_nacimiento(dataframe_icfes: pd.DataFrame) -> None:
    """
    Ejecuta la función que muestra un gráfico de barras con la cantidad de estudiantes por año de nacimiento.

    Parámetros:
        - dataframe_icfes (pd.DataFrame): DataFrame que contiene la información de la prueba ICFES Saber 11.

    Retorno:
        La función en la lógica muestra el gráfico directamente.
    """
    # TODO1: Complete la función tal y como se describe en la documentación.
    ic.barras(dataframe_icfes)
    


# Ejecución del Requerimiento 3:
def ejecutar_graficar_reparticion_por_departamento_y_anio(dataframe_icfes: pd.DataFrame) -> None:
    """
    Ejecuta la función que grafica un pie chart que representa la proporción del número total de estudiantes 
    por departamento de residencia, considerando únicamente a los estudiantes nacidos en un año específico.
    Se grafican únicamente los cinco departamentos con mayor número de estudiantes.

    Se debe pedir al usuario que ingrese un año de nacimiento para el cual desea generar el pie chart.
        - Recuerde convertir este valor a un número entero (int).
        - Recuerde considerar únicamente los cinco departamentos con mayor número de estudiantes

    Parámetros:
        - dataframe_icfes (pd.DataFrame): DataFrame que contiene la información de la prueba ICFES Saber 11.

    Retorno:
        La función en la lógica muestra el gráfico directamente.
    """
    # TODO2: Complete la función tal y como se describe en la documentación.
    año = int(input("ingrese el año"))
    ic.torta_por_requerimientos(dataframe_icfes, año)


# Ejecución del Requerimiento 4:
def ejecutar_crear_matriz_estudiantes_por_departamento_y_anio(dataframe_icfes: pd.DataFrame) -> tuple:
    """
    Ejecuta la función que crea una matriz que representa la cantidad de estudiantes por departamento y año de nacimiento.

    No se le deben pedir datos al usuario.

    Hay 2 casos posibles:
        - Si la matriz o algúna de las listas (departamentos o años) está vacía, se debe mostrar el siguiente mensaje:
            - "Error: La matriz o las listas no se han creado correctamente."
        
        - En el caso contrario, se debe imprimir la matriz usando la función imprimir_matriz().
    
    Parámetros:
        - dataframe_icfes (pd.DataFrame): DataFrame que contiene la información de la prueba ICFES Saber 11.

    Retorno:
        tuple: Una tupla que contiene:
            - list: Matriz bidimensional con la cantidad de estudiantes por departamento (filas) y año de nacimiento (columnas).
            - list: Lista de departamentos ordenados en el mismo orden que aparecen en la matriz.
            - list: Lista de años de nacimiento ordenados en el mismo orden que aparecen en la matriz.

    No debe modificar esta función.
    """
    matriz_info = ic.crear_matriz_estudiantes_por_departamento_y_anio(dataframe_icfes)
    if matriz_info is not None and len(matriz_info) == 3:
        matriz, departamentos, anios = matriz_info
        if matriz and departamentos and anios:
            imprimir_matriz(matriz_info)
        else:
            print("Error: La matriz o las listas no se han creado correctamente.")
    else:
        print("Error: La matriz o las listas no se han creado correctamente.")
    
    return matriz_info


# Ejecución del Requerimiento 5:
def ejecutar_obtener_promedio_estudiantes_anio(info_matriz: tuple) -> None:
    """
    Ejecuta la función que obtiene el promedio de estudiantes nacidos en un año específico.

    Se debe pedir al usuario que ingrese un año de nacimiento para el cual desea obtener el promedio.
        - Recuerde convertir este valor a un número entero (int).

    Existen dos casos posibles:
        - Si el año ingresado no está en el DataFrame, se debe mostrar el siguiente mensaje:
            - "No se encontraron estudiantes nacidos en el año ingresado."

        - En caso contrario, se debe mostrar el siguiente mensaje:
            - "El promedio de estudiantes nacidos en el año [X] que presentaron la prueba ICFES Saber 11 es: [Y]",
            
            Nota: Aquí, los corchetes indican la ubicación para la información definida a continuación:

            Donde:
                - [X] es el año ingresado por el usuario.
                - [Y] es el promedio de estudiantes nacidos en ese año que presentaron la prueba
    
    Ejemplo:
        El promedio por departamento de estudiantes nacidos en 2001 debe ser 859.
    
    Parámetros:
        - info_matriz (tuple): Una tupla que contiene:
            - list: Matriz bidimensional con la cantidad de estudiantes por departamento (filas) y año de nacimiento (columnas).
            - list: Lista de departamentos ordenados en el mismo orden que aparecen en la matriz.
            - list: Lista de años de nacimiento ordenados en el mismo orden que aparecen en la matriz.
    """
    # TODO3: Complete la función tal y como se describe en la documentación.
    pass


# Ejecución del Requerimiento 6:
def ejecutar_obtener_promedio_estudiantes_todos_los_anios(info_matriz: tuple) -> None:
    """
    Ejecuta la función que obtiene el promedio de estudiantes nacidos en cada año.

    No se le deben pedir datos al usuario.

    Se debe usar la función auxiliar mostrar_promedio_estudiantes() para imprimir el resultado.
    
    El resultado esperado debe ser el siguiente:
        
    Cantidad promedio de estudiantes por año de nacimiento:
    --------------------------------------------------
    **************************************************
    Año de nacimiento: 1998
    Cantidad promedio de estudiantes: 38
    **************************************************
    Año de nacimiento: 1999
    Cantidad promedio de estudiantes: 79
    **************************************************
    Año de nacimiento: 2000
    Cantidad promedio de estudiantes: 248
    **************************************************
    Año de nacimiento: 2001
    Cantidad promedio de estudiantes: 859
    **************************************************
    Año de nacimiento: 2002
    Cantidad promedio de estudiantes: 2137
    **************************************************
    Año de nacimiento: 2003
    Cantidad promedio de estudiantes: 4642
    **************************************************
    Año de nacimiento: 2004
    Cantidad promedio de estudiantes: 2500
    **************************************************
    Año de nacimiento: 2005
    Cantidad promedio de estudiantes: 100
    **************************************************
    Año de nacimiento: 2006
    Cantidad promedio de estudiantes: 4
    **************************************************
    Año de nacimiento: 2007
    Cantidad promedio de estudiantes: 2
    **************************************************
    Año de nacimiento: 2008
    Cantidad promedio de estudiantes: 1
    **************************************************
    Año de nacimiento: 2009
    Cantidad promedio de estudiantes: 1
    **************************************************

    Parámetros:
        - info_matriz (tuple): Una tupla que contiene:
            - list: Matriz bidimensional con la cantidad de estudiantes por departamento (filas) y año de nacimiento (columnas).
            - list: Lista de departamentos ordenados en el mismo orden que aparecen en la matriz.
            - list: Lista de años de nacimiento ordenados en el mismo orden que aparecen en la matriz.
            
    No debe modificar esta función.
    """
    promedio_estudiantes = ic.obtener_promedio_estudiantes_todos_los_anios(info_matriz)
    mostrar_promedio_estudiantes(promedio_estudiantes)


# Ejecución del Requerimiento 7:
def ejecutar_obtener_primera_cantidad_superior_a_umbral(info_matriz: tuple) -> None:
    """
    Ejecuta la función que busca la primera cantidad de estudiantes que supera un umbral en la matriz de información.

    Se debe pedir al usuario que ingrese un umbral de estudiantes.
        - Recuerde convertir este valor a un número entero (int).

    Existen dos casos posibles:
        - Si no se encuentra ninguna cantidad que supere el umbral, se debe mostrar el siguiente mensaje:
            - "No se encontró ninguna cantidad de estudiantes que supere el umbral ingresado."

        - En caso contrario, se debe mostrar el siguiente mensaje:
            - "La primera cantidad de estudiantes que supera el umbral ingresado es: [X] en el departamento [Y] y año de nacimiento [Z].",
            
            Nota: Aquí, los corchetes indican la ubicación para la información definida a continuación:

            Donde:
                - [X] es la cantidad de estudiantes que supera el umbral.
                - [Y] es el nombre del departamento donde se encontró esa cantidad.
                - [Z] es el año de nacimiento correspondiente.
                
    Ejemplo:
        Si el umbral ingresado es: 1100, la respuesta debe ser: 
            "La primera cantidad de estudiantes que supera el umbral ingresado es: 1159 en el departamento ANTIOQUIA y año de nacimiento 2000".

    Parámetros:
        - info_matriz (tuple): Una tupla que contiene:
            - list: Matriz bidimensional con la cantidad de estudiantes por departamento (filas) y año de nacimiento (columnas).
            - list: Lista de departamentos ordenados en el mismo orden que aparecen en la matriz.
            - list: Lista de años de nacimiento ordenados en el mismo orden que aparecen en la matriz.
    """
    # TODO4: Complete la función tal y como se describe en la documentación.
    pass
    

# Ejecución del Requerimiento 8:
def ejecutar_crear_mapa(info_matriz: tuple, ruta_mapa: str, ruta_coordenadas: str) -> None:
    """
    Ejecuta la función que muestra un mapa de Colombia con la cantidad de estudiantes por departamento dado un año de nacimiento específico.

    Se debe pedir al usuario que ingrese un año de nacimiento para el cual desea generar el mapa.   
        - Recuerde convertir este valor a un número entero (int).

    Retorno:
        La función en la lógica muestra el mapa directamente.
    """
    # TODO5: Complete la función tal y como se describe en la documentación.
    pass



##### Funciones del menú (NO MODIFICAR):
def iniciar_aplicacion() -> None:
    """
    Inicia la aplicación de análisis de información de la prueba ICFES Saber 11.
    """
    archivo = input("Ingrese el nombre del archivo de datos o presione Enter si este se llama icfes.csv: ")
    if archivo == "":
        archivo = "icfes.csv"
    
    dataframe_icfes = ic.cargar_datos(archivo)
    info_matriz = None
    print("\nDatos cargados exitosamente. \n")
    ejecutando = True
    print("#" * 70)
    print("Bienvenido a la aplicación de análisis de información de la prueba ICFES Saber 11")
    print("#" * 70)
    while ejecutando:
        ejecutando, info_matriz = mostrar_menu_aplicacion(dataframe_icfes, info_matriz)

def mostrar_menu_aplicacion(dataframe_icfes: pd.DataFrame, info_matriz) -> tuple:
    print("\nMenú de opciones:")
    print("1. Graficar cantidad de estudiantes por año de nacimiento")
    print("2. Graficar pie chart de estudiantes por departamento y año de nacimiento")
    print("3. Crear matriz de cantidad de estudiantes por departamento y año de nacimiento")
    print("4. Obtener promedio de estudiantes nacidos en un año específico")
    print("5. Obtener promedio de estudiantes nacidos en todos los años")
    print("6. Obtener primera cantidad de estudiantes que supera un umbral")
    print("7. Crear mapa de estudiantes por departamento y año de nacimiento")
    print("8. Salir")

    opcion = input("Ingrese la opción que desea ejecutar: ").strip()

    continuar_ejecutando = True

    MSG_ERROR = "Error: Primero debe crear la matriz de cantidad de estudiantes por departamento y año de nacimiento. (Opción 3)"

    if opcion == "1":
        ejecutar_graficar_cantidad_estudiantes_por_anio_nacimiento(dataframe_icfes)
    elif opcion == "2":
        ejecutar_graficar_reparticion_por_departamento_y_anio(dataframe_icfes)
    elif opcion == "3":
        info_matriz = ejecutar_crear_matriz_estudiantes_por_departamento_y_anio(dataframe_icfes)
    elif opcion == "4":
        if info_matriz is not None:
            ejecutar_obtener_promedio_estudiantes_anio(info_matriz)
        else:
            print(MSG_ERROR)
    elif opcion == "5":
        if info_matriz is not None:
            ejecutar_obtener_promedio_estudiantes_todos_los_anios(info_matriz)
        else:
            print(MSG_ERROR)
    elif opcion == "6":
        if info_matriz is not None:
            ejecutar_obtener_primera_cantidad_superior_a_umbral(info_matriz)
        else:
            print(MSG_ERROR)
    elif opcion == "7":
        if info_matriz is not None:
            archivo_mapa = input("Ingrese el nombre del archivo de mapa o presione Enter si este se llama mapa.png: ")
            if archivo_mapa == "":
                archivo_mapa = "mapa.png"
                
            archivo_coordenadas = input("Ingrese el nombre del archivo de coordenadas o presione Enter si este se llama coordenadas.txt: ")
            if archivo_coordenadas == "":
                archivo_coordenadas = "coordenadas.txt"
                
            ejecutar_crear_mapa(info_matriz, archivo_mapa, archivo_coordenadas)
        else:
            print(MSG_ERROR)

    elif opcion == "8":
        print("¡Gracias por usar la aplicación de análisis de información de la prueba ICFES Saber 11!")
        continuar_ejecutando = False
    else:
        print("Opción invalida. Intentelo de nuevo.")

    return continuar_ejecutando, info_matriz
###### Fin de las funciones del menú


if __name__ == "__main__":
    iniciar_aplicacion()