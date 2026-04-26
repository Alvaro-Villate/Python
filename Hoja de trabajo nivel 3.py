def sumatoria_n_pares(n:int)->int:
    sumatoria = 0
    for i in range(2,(n*2)+1,2):
        if i % 2 == 0:
            sumatoria += i
    return sumatoria

def sumatoria_de_pares_hasta_n(n:int)->int:
    suma = 0
    for i in range(2,n+1,2):
        suma += i
    return suma

def es_primo(n:int)->bool:
    es_primo = True
    if n == 2:
        es_primo = True
    elif n == 1 or n == 0:
        es_primo = False
        
    limite = n//2
    indicador = 2
    
    while indicador <= limite and es_primo == True:
        if n % indicador == 0:
           es_primo = False
           
        indicador += 1
   
    return es_primo

def suma_digitos_pares(n:int)->int:
    sumatoria = 0
    while n != 0:
        digito = n % 10
        if digito % 2 == 0:
            sumatoria += digito
        n = n//10
    return sumatoria

def suma_digitos_pares_2(n:int)->int:
    cadena = str(n)
    sumatoria = 0
    for i in cadena:
        if int(i) % 2 == 0:
            sumatoria += int(i)
    return sumatoria

def elminar_no_letras(cadena:str)->str:
    cadenas = ""
    for letra in cadena:
        if letra.isalpha() == True:
            cadenas += letra
    return cadenas

def es_feliz(n:int)->bool:
    es_feliz = False
    hecho = False
    resultados = {}
    while hecho == False:
        digitos = []
        cuadrados = []
        resultado = 0
        while n > 0:
            digito = n % 10
            digitos.append(digito)
            n = n // 10
        for i in digitos:
            cuadrado = i ** 2
            resultado += cuadrado
            cuadrados.append(resultado)
        n = resultado
        
        if n == 1:
            hecho = True
            es_feliz = True
        else:
            if str(n) not in resultados:
                resultados[str(n)] = 0
            else:
                resultados[str(n)] += 1
                
        if resultados[str(n)] > 1:
            es_feliz = False
            hecho = True
 
    return es_feliz

def maximo_minimo(minimo:int,maximo:int,lista:list)->str:
    contador_inferior = 0
    contador_intermedio = 0
    contador_superior = 0
    for numero in lista:
        if numero < minimo:
            contador_inferior += 1
        elif minimo <= numero <= maximo:
            contador_intermedio += 1
        elif numero > maximo:
            contador_superior += 1
    cadena = """El contador cuando el n es inferior que minimo es {},y
    cuando esta entre los dos es {} y cuando es superior es {}
    """.format(contador_inferior,contador_intermedio,contador_superior)
    return cadena

def primera_palabra_con_letra(cadena:str,letra:str)->str:
    nueva = ""
    lista = cadena.split()
    finalizado = False
    i = 0
    while finalizado == False and i < len(lista):
        if lista[i][0] == letra:
            nueva = lista[i]
            finalizado = True
        i += 1
    return nueva

def repita_letras(cad:str,num:int)->str:
    cadena = ""
    pos = 0
    for i in str(num):
        cadena += int(i) * cad[pos]
        pos += 1
    return cadena

def cuente_palabras(cad:str)->int:
    cad = cad.replace("."," ")
    cad = cad.replace(",", " ")
    cad = cad.replace(" ", " ")
    lista = cad.split()
    return len(lista)

def replique_palabras(pal:list,num:list)->str:
    cadena = ""
    i = 0
    for cada_letra in num:
        cadena +=  cada_letra * pal[i] + " "
        i += 1
    cadena = cadena.split()
    cadena = " ".join(cadena)
    return cadena

def v_1(pal:list,num:list)->str:
    
    cadena = ""
    if len(pal) > len(num):
       suma = -(len(pal) - len(num))
       copia = pal[:]
       copia = copia[:suma]
       replicar = replique_palabras(copia, num)
       faltante = pal[suma:] 
       cadena = replicar +"  " +" ".join(faltante)
    
    return cadena

def v_2 
