# -*- coding: utf-8 -

def cargar()->list:
    """
    Carga los shows en una lista a partir del archivo Netflix_Shows.csv
    Cada show se carga en un diccionario con la siguiente estructura:
        {title;rating;ratingLevel;ratingDescription;release year;user rating score;user rating size
    -------
    list
        lista que contiene diccionarios con la información de cada película en el archivo

    """
    # TODO: Implementar la carga del archivo CSV y la creación de la lista de diccionarios
    lista = []
    archivo = open("Netflix_Shows.csv","r")
    titulos = archivo.readline().strip().split(",")
    linea = archivo.readline().strip()
    while linea != "":
        datos = linea.split(",")
        diccionario = {}
        diccionario["title"] = datos[0]
        rating = datos[1].strip().replace("." , "")
        if rating.isdigit():
            diccionario["rating"] = float(datos[1])
        else:
            diccionario["rating"] = datos[1]
            
        diccionario["ratingLevel"] = datos[2]
        diccionario["ratingDescription"] = datos[3]
        diccionario["release year"] = datos[4]
        diccionario["user rating score"] = datos[5]
        diccionario["user rating size"] = datos[6]
        lista.append(diccionario)
        linea = archivo.readline().strip()
    archivo.close()
    return lista
        
    
def dar_titulos_anio(shows:list, anio:int)->list:
    """
    Crea y devuelve una lista con los títulos de los shows 
    estrenadas el año que llega por parámetro
    
    Parameters
    ----------
    shows : list
        lista que contiene diccionarios de shows
    anio : int
        año del que se desean conocer los shows

    Returns
    -------
    list
        lista con los títulos de los shows estrenados en el año por 
        parámetro. Lista vacía si ningún show fue estrenado en el año

    """
    # TODO: Implementar la búsqueda de títulos por año
    titulos = []
    i = 0
    while  i < len(shows):
        if shows[i]["release year"] == anio:
            titulos.append(shows[i]["title"])
        i += 1
    return titulos

def dar_titulos_clasificacion(shows:list, clasificacion:str)->list:
    """
    Crea y devuelve una lista con los títulos de los shows 
    con la clasificación que llega por parámetro
    
    Parameters
    ----------
    peliculas : list
        lista que contiene diccionarios de shows
    clasificacion : str
        clasificación de la que se desean conocer los shows

    Returns
    -------
    list
        lista con los títulos de los shows con la clasificación por 
        parámetro. Lista vacía si ningún show tiene la clasificación

    """
    # TODO: Implementar la búsqueda de títulos por clasificación
    lista = []
    i = 0
    while i < len(lista):
        if shows[i]["rating"].lower() == clasificacion.lower():
            lista.append(shows[i]["title"])
    return lista
    

def dar_titulo_anio_clasificacion(shows:list, anio:int, clasificacion: str)->list:
    """
    Crea y devuelve una lista con los títulos de los shows 
    con la clasificación que llega por parámetro estrenadas en el año
    que llega por parámetro
    
    Parameters
    ----------
    peliculas : list
        lista que contiene diccionarios de shows
     anio : int
        año del que se desean conocer los shows
    clasificacion : str
        clasificación de la que se desean conocer los shows

    Returns
    -------
    list
        lista con los títulos de los shows con la clasificación por 
        parámetro estrenados en el año por parámetro.
        Lista vacía si ningún show tiene la clasificación ni fue estrenada en
        el año dados.

    """
    # TODO: Implementar la búsqueda de títulos por año y clasificación
    lista = []
    clasificacion = dar_titulos_clasificacion(shows, clasificacion)
    peliculas = dar_titulos_clasificacion(shows, clasificacion)
    i = 0
    while i < len(clasificacion) or i < len(peliculas):
        if peliculas[i].lower().strip() == clasificacion[i].lower().strip():
            lista.append(peliculas[i])
    return lista

def dar_show_mayor_anio(shows:list)->dict:
    """
    Busca y devuelve el show de mayor año

    Parameters
    ----------
    peliculas : list
        lista que contiene diccionarios de shows

    Returns
    -------
    dict
        Diccionario del show con mayor año de estreno 
        si hay varios con el máximo año devuelve el 
        primero encontrado

    """
    # TODO: Implementar la búsqueda del show con el año de estreno más reciente
    mayor = 
    

def dar_show_nombre_corto(shows:list)->dict:
    """
    Busca y devuelve el show con el título mas corto

    Parameters
    ----------
    peliculas : list
        lista que contiene diccionarios de shows

    Returns
    -------
    dict
        Diccionario del show con nombre mas corto
        si hay varios con la misma longitud devuelve el 
        primero encontrado

    """ 
    # TODO: Implementar la búsqueda del show con el título más corto
    return {}