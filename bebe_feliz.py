def es_feliz(x:int)->bool:
    hecho = False
    es_feliz = False
    n = x
    existentes = []
    repetidos = {}
    
    if x == 1:
       es_feliz = True
    
    while n != 1 and hecho == False:
        cuadrados = []
        
        contador = 0
        
        while n > 0:
           
          digito = n % 10
          cuadrados.append(digito)
          n = n // 10
        
        for i in cuadrados:
            contador += i ** 2
        
        existentes.append(contador)
        n = contador
        
        
        if n in repetidos:
            repetidos[n] += 1
            
        else:
            repetidos[n] = 1
        
        if repetidos[n] >= 2:
            es_feliz = False
            hecho = True
        
        if n == 1:
            es_feliz = True
            hecho = True
            
    return es_feliz
                
            
            
            
            
        
            
            
            
            