
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
    guarda = rolados[guardar]
    estoque.append(guarda)
    del rolados[guardar]
    return [rolados, estoque]

def remover_dado(rodados, guardados, dado_sai):
    sai = guardados[dado_sai]
    rodados.append(sai)
    del guardados[dado_sai]
    return [rodados, guardados]







    

>>>>>>> 1117bf1fbcaad69c8cbd78e7dd7b35637894918a
