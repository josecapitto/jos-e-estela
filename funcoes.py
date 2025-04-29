import random

def rolar_dados(n):
    lista = []
    i = 0 
    while i < n:
        num = random.randint(1, 6)
        lista.append(num)
        i += 1 
    return lista 

def guardar_dado(rolados, estoque, guardar): 
    lista_estoque = []
    lista_estoque.append(estoque)
    estoque_c = estoque.copy()
    guarda = rolados[guardar]
    estoque_c.append(guarda)
    lista_estoque.append(estoque_c)
    return lista_estoque



    

