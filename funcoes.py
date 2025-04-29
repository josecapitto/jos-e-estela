
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

def remover_dado(rodados_, guardados_, dado_sai):
    sai = guardados_[dado_sai]
    rodados_.append(sai)
    del guardados_[dado_sai]
    return [rodados_, guardados_]
