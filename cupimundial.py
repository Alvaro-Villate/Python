#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Función 1:
def cargar_cupimundial(ruta_archivo: str) -> dict:
    """
    Carga un archivo en formato CSV (Comma-Separated Values) con la información de selecciones y jugadores.

    Parámetros:
        ruta_archivo (str): Ruta del archivo CSV con la información de las selecciones, incluyendo la extensión.
                       El archivo a cargar, es aquel entregado en el esqueleto de N3-PROY, denominado: cupimundial.csv
                           Ejemplo: "./cupimundial.csv" (si el archivo CSV está en el mismo directorio que este archivo).

    Nota: Nunca debe modificar el archivo cupimundial.csv.

    Retorno:
        dict: Un diccionario estructurado de la siguiente manera:
            
            - Las llaves representan los nombres de las selecciones.
                - La selección a la cual pertenece un jugador se encuentra en la columna "team" del CSV.
                - La selección es un string no vacío, sin espacios al inicio o al final.
                    Ejemplo: "Argentina".
                 
            - Los valores son listas de diccionarios, donde cada diccionario representa a un jugador.
                - Cada diccionario de un jugador debe contener los siguientes campos basados en las columnas del archivo CSV:

                    "name" (str): Nombre del jugador. Es un string no vacío, sin espacios al inicio o al final.
                                  Ejemplo: "Lionel Messi".
                                  
                    "age" (int): Edad del jugador. Es un número entero positivo.
                                 Ejemplo: 36.
                                               
                    "pace" (int): Valor que representa la velocidad del jugador. Es un número entero entre 0 y 100.
                                    Ejemplo: 85.
                    
                    "shooting" (int): Valor que representa la habilidad de tiro del jugador. Es un número entero entre 0 y 100.
                                    Ejemplo: 90.
                    
                    "passing" (int): Valor que representa la habilidad de pase del jugador. Es un número entero entre 0 y 100.
                                    Ejemplo: 88.
                                    
                    "dribbling" (int): Valor que representa la habilidad para superar a un rival con control del balón y movimientos técnicos ó regate. 
                                       Es un número entero entre 0 y 100.
                                        Ejemplo: 87.
                                        
                    "position" (str): Posición del jugador en el campo. Es un string no vacío, sin espacios al inicio o al final.
                                      Puede ser: "Defender", "Forward", "Midfielder", "Reserve", "Striker", "Substitute" o "Winger". 
                                      Ejemplo: "Winger".    
                                 
                    "direction" (str): Dirección del jugador respecto al campo. Es un string no vacío, sin espacios al inicio o al final.
                                       Puede ser "Left", "Center", "Right" o "Pending".
                                       Ejemplo: "Right".
                                 
                    "joined" (str): Fecha de ingreso del jugador al equipo. Es un string no vacío, sin espacios al inicio o al final y en el formato "YYYY-MM-DD".
                                    Ejemplo: "2023-01-01".
                                 
                    "contract" (str): Indica el año de finalización del contrato del jugador no vacío, sin espacios al inicio o al final. Es un string en el formato "YYYY".
                                      Ejemplo: "2026".
                                 
                    "preferred_foot" (str): Pie preferido del jugador. Es un string no vacío, sin espacios al inicio o al final.
                                            Puede ser: "Right" o "Left"
                                            Ejemplo: "Right".
                                 
                    "international_rep" (int): Reputación internacional del jugador. Es un número entero positivo en el rango del 1 al 5.
                                                      Ejemplo: 5.
                    
                    "wage" (int) Salario mensual en USD del jugador que pertenece a la selección. Es un entero positivo.
                                 Ejemplo: 320000.
                                 
        Notas importantes sobre la carga de datos:
        
        - Al usar la función open(), agregue la codificación “utf-8” de la siguiente forma, para garantizar la lectura de caracteres especiales del archivo CSV:
        
        open(archivo, "r", encoding="utf-8")
        
        - Al usar la función readline(), agregue una invocación a la función strip() de la siguiente forma, para garantizar que se eliminen los saltos de línea. 
        
        readline().strip()
        
        Si desea mayor información, por favor consulte:
            
        - Documentación de str.strip():
        https://docs.python.org/es/3/library/stdtypes.html#str.strip 
        
        - Documentación de readline():
        https://docs.python.org/es/3/tutorial/inputoutput.html#methods-of-file-objects          
    """
    # TODO 1: Implemente la función tal y como se describe en la documentación.
    archivo = open(ruta_archivo,"r",encoding = "utf-8")
    titulos = archivo.readline().strip().split(",")
    cupimundial = {}
    jugadores = []
    linea = archivo.readline().strip()
    while linea != "":
        datos = linea.split(",")
        cada_uno = {}
        cada_uno["name"] = datos[0].strip()
        cada_uno["age"] = int(datos[1])
        cada_uno["team"] = (datos[2]).strip()
        cada_uno["pace"] = int(datos[3])
        cada_uno["shooting"] = int(datos[4])
        cada_uno["passing"] = int(datos[5])
        cada_uno["dribbling"] = int(datos[6])
        cada_uno["position"] = (datos[7].strip())
        cada_uno["direction"] = (datos[8].strip())
        cada_uno["joined"] = (datos[9].strip())
        cada_uno["contract"] = (datos[10].strip())
        cada_uno["preferred_foot"] = (datos[11].strip())
        cada_uno["international_rep"] = int(datos[12])
        cada_uno["wage"] = int(datos[13])
        jugadores.append(cada_uno)
        linea = archivo.readline().strip()
    
    archivo.close()
    
    for jugador in jugadores:
        seleccion = jugador["team"].lower()
        if seleccion not in cupimundial:
            cupimundial[seleccion] = [jugador]
            del jugador["team"]
        else:
            cupimundial[seleccion].append(jugador)
            del jugador["team"]
    
    return cupimundial
    
# Función 2:
def buscar_jugadores_por_posicion_salario(cupimundial: dict, posicion: str, salario_maximo: int) -> list:
    """
    Busca los jugadores que juegan en una posición determinada y que tienen un salario menor o igual al valor dado: salario_maximo.

    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.
        posicion (str): Posición del jugador a buscar. Debe ser un string no vacío.
        salario_maximo (int): Salario máximo del jugador a buscar. Debe ser un número entero positivo.

    Notas:
        - La búsqueda no es sensible a mayúsculas y minúsculas, por lo que, por ejemplo
          "Winger" y "winger" son considerados iguales.
          
    Retorno:
        list: Lista de diccionarios, donde cada diccionario representa un jugador y contiene las mismas llaves y valores 
             definidos en la estructura original (por ejemplo, "position", "wage", entre otras). 
             Solo se incluyen los jugadores que cumplen con los criterios de posición y salario. 
             Si no se encuentran jugadores que cumplan, se retorna una lista vacía.
    """
    # TODO 2: Implemente la función tal y como se describe en la documentación.
    cumplidos = []
    for sele in cupimundial:
        for jugador in cupimundial[sele]:
            if jugador["position"].lower() == posicion.lower() and salario_maximo >= jugador["wage"]:
                cumplidos.append(jugador)
    return cumplidos
    
# Función 3:
def buscar_jugador_con_contrato_mas_antiguo(cupimundial: dict) -> dict:
    """
    Busca el jugador con el contrato más antiguo.

    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.

    Notas:
        - El contrato se considera más antiguo si la fecha de ingreso del jugador es anterior a la de todos los demás jugadores.
        - La fecha de ingreso se encuentra en el campo "joined" del diccionario del jugador, con el formato "YYYY-MM-DD".
    
    Retorno:
        dict: Diccionario que representa un jugador y contiene las mismas llaves y valores 
        definidos en la estructura original (por ejemplo, "joined", entre otras).
        Solo se incluye el jugador con el contrato más antiguo.
        Si hay varios jugadores con la misma fecha de ingreso más antigua, se retorna únicamente el primero encontrado.
        Si no se encuentran jugadores, se retorna un diccionario vacío.
    """
    # TODO 3: Implemente la función tal y como se describe en la documentación.
    el_viejo = {}
    menor = "9999-99-99"
    for sele in cupimundial:
        for jugador in cupimundial[sele]:
            if jugador["joined"] < menor:
                menor = jugador["joined"]
                el_viejo = jugador
                
    return el_viejo

# Función 4:
def obtener_salario_total_jugadores_posicion(cupimundial: dict, posicion: str) -> int:
    """
    Obtiene el salario total de todos los jugadores que juegan en una posición específica del campo.
    
    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.
        posicion (str): Posición del jugador a buscar. Debe ser un string no vacío.

    Notas:
        - La búsqueda no es sensible a mayúsculas y minúsculas, por lo que, por ejemplo
            "Winger" y "winger" son considerados iguales.
        - Se considera solo la posición del jugador en el campo.
        
    Retorno:
        int: Salario total de todos los jugadores que juegan en la posición especificada. 
            Si no se encuentran jugadores, se retorna 0.
    """
    # TODO 4: Implemente la función tal y como se describe en la documentación.
    salario = 0
    
    for sele in cupimundial:
        for jugador in cupimundial[sele]:
            if jugador["position"].lower() == posicion.lower():
                salario += jugador["wage"]
    return salario


# Función 5:
def obtener_posicion_mas_costosa(cupimundial: dict) -> dict:
    """
    Obtiene la posición cuyo salario total acumulado de sus jugadores es el más alto.

    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.

    Nota:
        - La posición se considera más costosa si el salario total de los jugadores que juegan en esa posición es mayor que el de otras posiciones.
    
    Retorno:
        dict: Diccionario con las llaves "posicion" y "salario_total".
        - "posicion": (str) El nombre de la posición más costosa identificada. Es un string no vacío, en minúsculas y sin espacios al inicio o al final.
        - "salario_total": (int) Suma de los salarios de los jugadores que juegan en dicha posición. Es un número entero positivo.
        Solo se incluye la posición cuyo salario total acumulado es el más alto.
        Si hay varias posiciones con el mismo salario total más alto, se retorna únicamente la primera encontrada.
        Si no se encuentran jugadores, se retorna el diccionario: {"posicion": "", "salario_total": 0}.
    """
    # TODO 5: Implemente la función tal y como se describe en la documentación.
    posiciones = {}
    cara = {"posicion": "", "salario_total": 0}
    for sele in cupimundial:
        for jugador in cupimundial[sele]:
            pos = jugador["position"]
            if pos not in posiciones:
                posiciones[pos] = jugador["wage"]
            else:
                posiciones[pos] += jugador["wage"]
    for cada_uno in posiciones:
        if posiciones[cada_uno] > cara["salario_total"]:
            cara = {"posicion": cada_uno.lower(), "salario_total": posiciones[cada_uno]}
    return cara
# Función 6:
def crear_hashtag_para_jugadores(cupimundial: dict) -> None:
    """
    Crea un hashtag promocional para cada jugador de las selecciones siguiendo un formato específico.

    Esta función modifica directamente el diccionario recibido, añadiendo a cada jugador una nueva llave "hashtag" con su respectivo valor.
    
    El hashtag debe cumplir las siguientes condiciones:
    
    - Iniciar con "#Vamos".
    - Incluir el primer nombre del jugador en minúsculas y sin caracteres especiales.
    - Incluir el nombre de la selección en minúsculas y sin caracteres especiales.
    - Incluir el año de inicio del contrato del jugador.
    - Incluir el año de finalización del contrato del jugador.
    - Separar cada parte mediante guiones bajos ("_").
    
    El formato del hashtag es:
    #Vamos_[A]*[B]*[C]_[D]
    
    Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación:     
    - [A]: primer nombre del jugador en minúsculas y sin caracteres especiales.
    - [B]: nombre de la selección en minúsculas y sin caracteres especiales.
    - [C]: año de inicio del contrato.
    - [D]: año de finalización del contrato.
    
    Ejemplo:
    Si el jugador se llama "Lionel Messi", pertenece a la selección "Argentina" y su contrato va de "2021-01-01" a "2026", el hashtag (string) sería:
    #Vamos_lionel_argentina_2021_2026

    Notas:
        - El año de inicio del contrato se encuentra en el campo "joined" del diccionario del jugador, con el formato "YYYY-MM-DD".
        - El año de finalización del contrato se encuentra en el campo "contract" del diccionario del jugador, con el formato "YYYY".
    
    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.
        
    Retorno:
        None: Esta función modifica directamente al diccionario original de forma permanente. 
            No es necesario retornarlo ni crear una copia del mismo.
    """
    # TODO 6: Implemente la función tal y como se describe en la documentación.
    hashtag = ""
    for sele in cupimundial:
        for jugador in cupimundial[sele]:
            listas  = []
            nombre = jugador["name"].split()
            listas.append(nombre[0].lower())
            team = sele.lower()
            listas.append(team)
            inicio = jugador["joined"].split("-")
            listas.append(inicio[0])
            final = jugador["contract"]
            listas.append(final)
            hashtag = "#Vamos_"+"_".join(listas)
            jugador["hashtag"] = hashtag
    
            

# Función 7:
def buscar_primer_jugador_reputacion_5(cupimundial: dict, seleccion: str) -> dict:
    """
    Busca el primer jugador de una selección dada que tenga una reputación internacional igual a 5.

    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.
        seleccion (str): Nombre de la selección en la cual se realizará la búsqueda.

    Nota:
        - La búsqueda es sensible a mayúsculas y minúsculas, por lo que, por ejemplo
            "Argentina" y "argentina" no son considerados iguales.

    Retorno:
        dict: Diccionario del primer jugador de la selección dada que tenga una reputación internacional de 5.
            Si no se encuentra ningún jugador que cumpla con la condición, se retorna un diccionario vacío.
    """
    # TODO 7: Implemente la función tal y como se describe en la documentación.
    seleccion = seleccion.lower()
    encontrado = False
    jugador_estrella = {}
    i = 0
    while i < len(cupimundial[seleccion]) and encontrado == False:
        jugador = cupimundial[seleccion]
        if jugador[i]["international_rep"] == 5:
            jugador_estrella = jugador[i]
            encontrado = True
        i += 1
        
    return jugador_estrella
    
    
#Función 8:
def recomendar_jugador_destacado( 
        cupimundial: dict, 
        seleccion: str,
        edad_minima: int, 
        edad_maxima: int, 
        reputacion_minima: int, 
        pie_preferido: str
    ) -> dict:
    """
    Recomienda el primer jugador que:
      - Juega en la posición más costosa (por salario total).
      - Pertenece a una seleccion dada por parámetro (sensible a mayúsculas/minúsculas).
      - Su edad está en el rango especificado (entre edad_minima y edad_maxima, inclusivo).
      - Tiene una reputación internacional mayor o igual a reputacion_minima.
      - Usa el pie preferido especificado (no sensible a mayúsculas/minúsculas).

    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.
        seleccion (str): Selección que se busca filtrar. Debe ser un string no vacío.
        edad_minima (int): Edad mínima permitida. Debe ser un número entero positivo.
        edad_maxima (int): Edad máxima permitida. Debe ser un número entero positivo.
        reputacion_minima (int): Reputación internacional mínima requerida. Debe ser un número entero entre 1 y 5.
        pie_preferido (str): Pie preferido del jugador. Debe ser "Left" o "Right". 
        
    Notas:
        - La posición más costosa se determina por el salario total de los jugadores que juegan en esa posición.
        - El pie preferido no es sensible a mayúsculas y minúsculas, por lo que, por ejemplo, "Right" y "right" son considerados iguales.

    Retorno:
        dict: Diccionario que representa un jugador y contiene las mismas llaves y valores definidos 
        en la estructura original (por ejemplo, "position", "age", "international_rep", "preferred_foot", entre otras).
        Solo se incluye el primer jugador que cumple con todos los criterios.
        Si no se encuentra ningún jugador que cumpla con los criterios, se retorna un diccionario vacío.    
    """
    # TODO 8: Implemente la función tal y como se describe en la documentación.
    encontrado = False
    recomendado = {}
    preferido = obtener_posicion_mas_costosa(cupimundial)
    indice = 0
    seleccion = seleccion.lower().strip()
    
    while encontrado == False and indice < len(cupimundial[seleccion]):
        jugador = cupimundial[seleccion][indice]
        if seleccion in cupimundial:
            if jugador["position"].lower() == preferido["posicion"]:
                    if edad_minima <= jugador["age"] <= edad_maxima:
                        if reputacion_minima <= jugador["international_rep"]:
                            if jugador["preferred_foot"].lower() == pie_preferido.lower():
                                recomendado = jugador
                                encontrado = True
        
        indice += 1
        
    return recomendado


# Función 9:
def buscar_jugadores_juegan_en_posiciones(cupimundial : dict) -> dict:
    """
    Retorna un diccionario que relaciona las posiciones con los nombres de los jugadores que juegan en ellas.

    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.
    
    Notas:
    - No puede haber jugadores repetidos en una misma posición.
    - Las posiciones deben estar en minúsculas y sin espacios al inicio ni al final.
    - Los nombres de los jugadores se mantienen en su forma original, respetando mayúsculas y minúsculas.
    
    Ejemplo:
        Para la llave "winger", una parte de la lista de jugadores podría ser:
        ["Lionel Andrés Messi Cuccittini", "Lucas Ariel Ocampos", "Emiliano Buendía", "Nicolás Iván González", "Rubens Omar Óscar Sambueza", ...]
    
    Nota:
        Los puntos suspensivos (...) aquí indican que hay más jugadores en esa posición, pero no se muestran para simplificar el ejemplo.
    
    Retorno:
        dict: Diccionario donde cada llave es una posición (en minúsculas y sin espacios al inicio o al final) y 
        cada valor es una lista de strings con los nombres de los jugadores que juegan en dicha posición.
        Si no se encuentran jugadores, se retorna un diccionario vacío.
    """
    # TODO 9: Implemente la función tal y como se describe en la documentación.
    posiciones_t = {}
    for sele in cupimundial:
        for jugador in cupimundial[sele]:
            nombre = jugador["name"]
            pos = jugador["position"].lower().strip()
            if pos not in posiciones_t:
               posiciones_t[pos] = [nombre]
            else:
                if nombre not in posiciones_t[pos]:
                    posiciones_t[pos].append(nombre)
    return posiciones_t