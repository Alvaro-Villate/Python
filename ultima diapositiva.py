

def funcion(codigo:int,vuelos:dict)->list:
    """
    Escribe una función que reciba por parámetro el código de un
    aeropuerto y el diccionario de vuelos y retorne una lista con los códigos
    de todos los vuelos que parten de ese aeropuerto
    """
    lista = []
    for llave,valor in vuelos.items():
        if valor == codigo:
            lista.apppend(valor)
    
    return lista
  

def funcion_v(codigo:int,vuelos:dict)->dict:
    """
    Escribe una función que reciba por parámetro el código de un vuelo y
    el diccionario de vuelos y retorne un diccionario con la información del
    mismo. Si el vuelo no existe, la función retorna None
    """
    
    for nombre,c_codigo in vuelos.items():
        if c_codigo == codigo:
            diccionario = {nombre : c_codigo}
        else:
            diccionario = None
    return diccionario
     
def mayor_distancia(IATA: str, vuelos: dict) -> str:
    vuelo_mas_largo = ""
    max_distancia = -1
    
    for codigo, datos in vuelos.items():
        # Primero revisamos si el vuelo es de la aerolínea (IATA)
        if datos.get("aerolinea") == IATA:
            distancia_actual = datos.get("distancia", 0)
            
            # Si esta distancia es mayor a la que conocemos, actualizamos
            if distancia_actual > max_distancia:
                max_distancia = distancia_actual
                vuelo_mas_largo = codigo
                
    return vuelo_mas_largo
    
       