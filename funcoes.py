import random

# Questão 1 - Funções para o jogo de dados
def rolar_dados(n):
    lista = []
    i = 0 
    while i < n:
        num = random.randint(1, 6)
        lista.append(num)
        i += 1 
    return lista 

# Questão 2 - Guardar o dado escolhido
def guardar_dado(rolados, estoque, guardar): 
    guarda = rolados[guardar]
    estoque.append(guarda)
    del rolados[guardar]
    return [rolados, estoque]


# Questão 5 - Função para calcular pontos
def calcula_pontos_soma(sequência):

    if sequência == [1, 2, 3, 4] or sequência == [2, 3, 4, 5] or sequência == [3, 4, 5, 6]:
        valor = 15
    if sequência == [1, 2, 3, 4, 5] or sequência == [2, 3, 4, 5, 6]:
        valor = 30
    else:
        valor = sum(sequência)
    if len(sequência) == 5:
        num = sequência[0]
        for i in sequência:
            if num != i:
                valor = sum(sequência)
                break
            else:
                valor = 50
    return valor 







    

