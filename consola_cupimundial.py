#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cupimundial as c

###### Funciones auxiliares (NO MODIFICAR):

def mostrar_jugador(jugador: dict) -> None:
    """
    Muestra la información de un jugador.

    Parámetros:
        jugador (dict): Diccionario con la información del jugador.
    """
    if jugador is not None and jugador != {}:
        print("\n")
        print("#" * 50)
        
        print((
            "Nombre: {}\n"
            "Edad: {}\n"
            "Velocidad: {}\n"
            "Tiros al arco: {}\n"
            "Pases: {}\n"
            "Regate: {}\n"
            "Posición: {}\n"
            "Dirección: {}\n"
            "Fecha de ingreso: {}\n"
            "Año de fin del contrato: {}\n"
            "Pie preferido: {}\n"
            "Reputación internacional: {}\n"
            "Salario: ${} USD\n"
        ).format(
            jugador['name'], jugador['age'],
            jugador['pace'], jugador['shooting'], jugador['passing'],
            jugador['dribbling'], jugador['position'], jugador['direction'], jugador['joined'],
            jugador['contract'], jugador['preferred_foot'],
            jugador['international_rep'], jugador['wage']
        ))
        
        print("#" * 50)
    else: 
        print("Error: Diccionario de jugador inválido.")


def mostrar_jugadores(jugadores: list) -> None:
    """
    Muestra la información de una lista de jugadores.

    Parámetros:
        jugadores (list): Lista de diccionarios con la información de los jugadores.
    """
    if jugadores is not None and jugadores != []:
        print("\n Jugadores de Cupimundial:")
        print("-" * 50)
        
        for jugador in jugadores:
            mostrar_jugador(jugador)
            
        print("-" * 50)
    else:
        print("Error: Lista de jugadores inválida.")

    
def mostrar_nombres_jugadores(jugadores: list) -> None:
    """
    Muestra los nombres de los jugadores de Cupimundial.

    Parámetros:
        jugadores (list): Lista con los nombres de los jugadores.
    """
    if jugadores is not None and jugadores != []:
        print("\n Jugadores de Cupimundial:")
        print("-" * 50)
        
        for jugador in jugadores:
            print(jugador)
        
        print("-" * 50)
    else:
        print("Error: Lista de jugadores inválida.")
###### Fin de funciones auxiliares



# Funciones a implementar (solo aquellas con TODOs):

# Ejecución de Función 2:
def ejecutar_buscar_jugadores_por_posicion_salario(cupimundial: dict) -> None:
    """
    Ejecuta la búsqueda de los jugadores que cumplen con una posición y un salario máximo.

    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.
    
    Se debe pedir al usuario la posición del jugador en el campo y un salario máximo.
    
    Existen 2 casos posibles para mostrar el resultado:
    
        - Si no se encuentran jugadores que cumplan con la posición y el salario máximo, se muestra el siguiente mensaje:
            - "No se encontraron jugadores que jueguen de [X] y tengan un salario máximo de $[Y]."

        - Si se encuentran jugadores, se imprime el mensaje:
            - "Los jugadores que juegan de [X] y tienen un salario máximo de $[Y] son:" 
            Luego, se usa la función auxiliar mostrar_jugadores() para mostrar los jugadores encontrados.

       Nota: Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación.
            
            Donde:
                - [X] es la posición ingresada por el usuario.
                - [Y] es el salario máximo ingresado por el usuario.
                
    """
    # TODO 10: Implemente la función tal y como se destcribe en la documentación.
    posicion = str(input("ingrese la posicion del jugador")).strip().lower()
    salario_maximo = int(input("ingrese el salario maximo del jugador"))
    llamado = c.buscar_jugadores_por_posicion_salario(cupimundial, posicion, salario_maximo)
    if llamado == []:
        print("No se encontraron jugadores que jueguen de {} y tengan un salario máximo de {}.".format(posicion,salario_maximo))
    else:
        print("Los jugadores que juegan de {} y tienen un salario máximo de ${} son:".format(posicion,salario_maximo))
        mostrar_jugadores(llamado)
    
    
    
# Ejecución de Función 3:    
def ejecutar_buscar_jugador_con_contrato_mas_antiguo(cupimundial: dict) -> None:
    """
    Ejecuta la búsqueda del jugador con el contrato más antiguo.
    
    No se debe pedir ningún dato al usuario.

    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.
    
    Existen 2 casos posibles para mostrar el resultado:
    
        - Si no se encuentran ningún jugador, se muestra el siguiente mensaje:
            - "No se encontraron jugadores en Cupimundial."
            
        - Si se encuentra un jugador, se imprime el encabezado:
            - "El jugador con el contrato más antiguo es:"
            Luego, se usa la función auxiliar: mostrar_jugador() para mostrar al jugador con el contrato más antiguo.

    """
    # TODO 11: Implemente la función tal y como se describe en la documentación.
    antiguo = c.buscar_jugador_con_contrato_mas_antiguo(cupimundial)
    if antiguo == {}:
        print("No se encontraron jugadores en Cupimundial.")
    else:
        print("El jugador con el contrato más antiguo es:")
        mostrar_jugador(antiguo)


# Ejecución de Función 4:
def ejecutar_obtener_salario_total_jugadores_posicion(cupimundial: dict) -> None:
    """
    Ejecuta la función para obtener el salario total de los jugadores de Cupimundial que juegan en una posición específica.
    
    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.
        
    Se debe pedir al usuario la posición del jugador en el campo.
    
    Existen 2 casos posibles para mostrar el resultado:
        
        - Si no se encuentran jugadores con la posición solicitada, se muestra el siguiente mensaje:
            - "No se encontraron jugadores con esa posición."

        - Si se encuentran jugadores, se imprime el encabezado
            - "El salario total de los jugadores que juegan de [X] es: $[Y] USD."
            
        Nota: Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación:
            
            Donde:
                - [X] es la posición ingresada por el usuario.
                - [Y] es el salario total de los jugadores que juegan en esa posición.
    
    """
    # TODO 12: Implemente la función tal y como se describe en la documentación.
    posicion = str(input("ingrese la posicion de la cual se va a extraer su salario")).strip().lower()
    funcion = c.obtener_salario_total_jugadores_posicion(cupimundial, posicion)
    if funcion == 0:
        print("No se encontraron jugadores con esa posición.")
    else:
        print("El salario total de los jugadores que juegan de {} es: ${} USD.".format(posicion,funcion))
              
        
# Ejecución de Función 5:   
def ejecutar_obtener_posicion_mas_costosa(cupimundial: dict) -> None:
    """
    Ejecuta la búsqueda de la posición más costosa de los jugadores.
    
    No se debe pedir ningún dato al usuario.

    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.
        
    Existen 2 casos posibles para mostrar el resultado:
        
        - Si no se encuentra ninguna posicion, se muestra el siguiente mensaje:   
            - "No se encontraron posiciones en Cupimundial."
            
        - Si se encuentra una posición, se imprime el mensaje:
            - "La posición más costosa es [X] con un salario total de $[Y] USD."
        
        Nota: Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación:
        
        Donde:
            - [X] es la posición más costosa.
            - [Y] es el salario total de los jugadores que juegan en esa posición.
            
    """
    # TODO 13: Implemente la función tal y como se describe en la documentación.
    busqueda = c.obtener_posicion_mas_costosa(cupimundial)
    if busqueda == {"posicion": "", "salario_total": 0}:
        print("No se encontraron posiciones en Cupimundial.")
    else:
        print("La posición más costosa es {} con un salario total de ${} USD.".format(busqueda["posicion"],busqueda["salario_total"]))
        
        
    
        

# Ejecución de Función 6:      
def ejecutar_crear_hashtags_para_jugadores(cupimundial: dict) -> None:
    """
    Ejecuta la función para crear hashtags para los jugadores.
    
    No se debe pedir ningún dato al usuario.
    
    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.

    El mensaje tiene el siguiente formato:
        - "El hashtag creado para el jugador [X] es: [Y]"
        
        Nota: Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación:
        
        Donde:
            - [X] es el nombre del jugador.
            - [Y] es el hashtag creado para el jugador.

    A modo de ejemplo, en la implementación aquí dada, se muestra el hashtag creado para el primer jugador de Colombia.
    
    No debe modificar esta función.
    """
    if 'Colombia' in cupimundial and cupimundial['Colombia'] != []:
        c.crear_hashtag_para_jugadores(cupimundial)
        jugador = cupimundial['Colombia'][0]
        print("El hashtag creado para el jugador " + jugador['name'] + " es: " + jugador['hashtag'])
        
        
# Ejecución de Función 7:
def ejecutar_buscar_primer_jugador_reputacion_5(cupimundial: dict) -> None:
    """
    Ejecuta la función para buscar el primer jugador de una selección que tenga una reputación de 5.
    
    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.
        
    Se debe pedir al usuario el nombre de la selección en la cual se realizará la búsqueda.
    
    Existen 2 casos posibles para mostrar el resultado:
        
        - Si no se encuentra ningún jugador con reputación 5 o la selección no existe, se muestra:
            - "No se encontró ningún jugador con reputación 5 en la selección [X]."

        - Si se encuentra un jugador, se imprime el encabezado:
            - "El primer jugador con reputación 5 en la selección [X] es: "
            Luego, se usa la función auxiliar: mostrar_jugador() para mostrar al jugador encontrado.
            
        Nota: Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación:
            
            Donde:
                - [X] es el nombre de la selección ingresada por el usuario.
    
    """
    # TODO 14: Implemente la función tal y como se describe en la documentación.
    seleccion = str(input("ingrese la seleccion"))
    funcion = c.buscar_primer_jugador_reputacion_5(cupimundial, seleccion)
    if funcion == {}:
        print("No se encontró ningún jugador con reputación 5 en la selección {}.".format(seleccion))
    else:
        print("El primer jugador con reputación 5 en la selección {} es: ".format(seleccion))
        mostrar_jugador(funcion)
    
        
        
# Ejecución de Función 8: 
def ejecutar_recomendar_jugador_destacado(cupimundial: dict) -> None:
    """
    Ejecuta la búsqueda del primer jugador destacado que cumple con los criterios definidos.

    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.
        
    Se debe pedir al usuario los siguientes datos:
        - La selección del jugador.
        - La edad mínima del jugador.
        - La edad máxima del jugador.
        - La reputación internacional mínima del jugador.
        - El pie preferido del jugador ("Left" o "Right").
    
    Existen 2 casos posibles para mostrar el resultado:
        
        - Si no se encuentra un jugador que cumpla con los criterios, se muestra el siguiente mensaje:
            - "No se encontró un jugador destacado que cumpla con los criterios."

        - Si se encuentra un jugador, se imprime el encabezado:
            - "El jugador destacado recomendado es:"
            Luego, se usa la función auxiliar: mostrar_jugador() para mostrar al jugador recomendado.
            
    """
    # TODO 15: Implemente la función tal y como se describe en la documentación.
    seleccion = str(input("ingrese seleccion")).lower().strip()
    edad_minima = int(input("ingrese la edad minima"))
    edad_maxima = int(input("ingrese la edad maxima"))
    reputacion_minima = int(input("ingrese la reputacion minima"))
    pie_preferido = str(input("ingrese su pie preferido")).lower().strip()
    funcion = c.recomendar_jugador_destacado(cupimundial, seleccion, edad_minima, edad_maxima, reputacion_minima, pie_preferido)
    if funcion == {}:
        print("No se encontró un jugador destacado que cumpla con los criterios.")
    else:
        print("El jugador destacado recomendado es:")
        mostrar_jugador(funcion)
        
            
        


# Ejecución de Función 9:    
def ejecutar_buscar_jugadores_juegan_en_posiciones(cupimundial: dict) -> None:
    """
    Ejecuta la función para buscar a los jugadores que juegan en una posición específica.
    
    Parámetros:
        cupimundial (dict): Diccionario con la información de las selecciones y sus jugadores.

    Se debe pedir al usuario la posición del jugador en el campo.
    
    Existen 2 casos posibles para mostrar el resultado:
        
        - Si no se encuentran jugadores con la posición solicitada, se muestra el siguiente mensaje:
            - "No se encontraron jugadores con esa posición."

        - Si se encuentran jugadores, se imprime el encabezado:
            - "Los jugadores que juegan de [X] son:"
            
        Nota: Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación:
            
            Donde:
                - [X] es la posición ingresada por el usuario.
                
        Luego, se usa la función auxiliar: mostrar_nombres_jugadores() para mostrar a todos los jugadores
        que cumplen con la posición solicitada.

    A modo de ejemplo, en la implementación aquí dada, se obtiene el diccionario de posiciones y jugadores, 
    se verifica si la posición ingresada existe como llave en dicho diccionario y, en caso afirmativo, 
    se imprime el encabezado junto con la lista de jugadores.
    Caso contrario, se muestra un mensaje indicando que la posición no fue encontrada.
    
    No debe modificar esta función.
    """
    posicion = input("Ingrese la posición del jugador (string no vacío): ").strip().lower() 
    
    jugadores_encontrados = c.buscar_jugadores_juegan_en_posiciones(cupimundial)
    
    if posicion in jugadores_encontrados:
        print("Los jugadores que juegan de " + posicion + " son:")
        mostrar_nombres_jugadores(jugadores_encontrados[posicion])
    else:
        print("No se encontraron jugadores con esa posición.")
        



###### Funciones del menú (NO MODIFICAR):
def iniciar_aplicacion() -> None:
    """
    Función principal de la aplicación.
    """
    ejecutando = False
    archivo = input("Ingrese el nombre del archivo de datos o presione Enter si su archivo se llama cupimundial.csv: ")
    if archivo == "":
        archivo = "cupimundial.csv"
        
    cupimundial = c.cargar_cupimundial(archivo)
    if cupimundial != {} and cupimundial is not None:
        ejecutando = True
        print("#" * 50)
        print("¡Bienvenido a la aplicación de Cupimundial!")
        print("#" * 50)
        
        while ejecutando:
            ejecutando = mostrar_menu_principal(cupimundial)
            if ejecutando:
                input("Presione Enter para continuar...")
    else:
        print("\nError: No se ha podido cargar el archivo. \nRevise su implementación de la función: cargar_cupimundial() en cupimundial.py")


def mostrar_menu_principal(cupimundial: dict) -> bool:
    """
    Muestra el menú principal de la aplicación y ejecuta la opción seleccionada por el usuario.

    Parámetros:
        cupimundial (dict): Diccionario con las selecciones y sus jugadores.
    
    Retorno:
        bool: True si se desea continuar, False si se desea salir.
    """
    print("\nMenú de opciones:")
    print("1. Buscar jugadores por posición y salario.")
    print("2. Buscar jugador con contrato más antiguo.")
    print("3. Obtener salario total de jugadores en una posición.")
    print("4. Obtener posición más costosa.")
    print("5. Crear hashtags para jugadores.")
    print("6. Buscar primer jugador con reputación 5")
    print("7. Recomendar jugador destacado")
    print("8. Buscar jugadores que juegan en una posición específica.")
    print("9. Salir.")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_buscar_jugadores_por_posicion_salario(cupimundial)
    elif opcion_elegida == "2":
        ejecutar_buscar_jugador_con_contrato_mas_antiguo(cupimundial)
    elif opcion_elegida == "3":
        ejecutar_obtener_salario_total_jugadores_posicion(cupimundial)
    elif opcion_elegida == "4":
        ejecutar_obtener_posicion_mas_costosa(cupimundial)
    elif opcion_elegida == "5":
        ejecutar_crear_hashtags_para_jugadores(cupimundial)
    elif opcion_elegida == "6":
        ejecutar_buscar_primer_jugador_reputacion_5(cupimundial)
    elif opcion_elegida == "7":
        ejecutar_recomendar_jugador_destacado(cupimundial)
    elif opcion_elegida == "8":
        ejecutar_buscar_jugadores_juegan_en_posiciones(cupimundial)
    elif opcion_elegida == "9":
        print("\n¡Gracias por usar la aplicación de CupiMundial!")
        continuar_ejecutando = False
    else:
        print("Opción inválida. Por favor inténtelo de nuevo.")
    
    return continuar_ejecutando
###### Fin de las funciones del menú            
            
            
if __name__ == "__main__":
    iniciar_aplicacion()