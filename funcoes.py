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

# Questão 3 - Remover o dado escolhido
def remover_dado(rodados_, guardados_, dado_sai):
    sai = guardados_[dado_sai]
    rodados_.append(sai)
    del guardados_[dado_sai]
    return [rodados_, guardados_]

# Questão 4 - Função paracalcular a pontuação com a regra simples
def calcula_pontos_regra_simples (faces):
    qtd = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for face in faces:
        if face in qtd:
            qtd[face] += 1
    pontos = {}
    for i in qtd.keys():
        pontos[i] = qtd[i] * i
    return pontos

# Questão 5 - Função para calcular a pontuação de sequencia baixa
def calcula_pontos_sequencia_baixa(faces):
    qtd = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for face in faces:
        if face in qtd:
            qtd[face] += 1
    
    if qtd[1] >= 1 and qtd[2] >= 1 and qtd[3] >= 1 and qtd[4] >= 1:
        return 15
    elif qtd[2] >= 1 and qtd[3] >= 1 and qtd[4] >= 1 and qtd[5] >= 1:
        return 15
    elif qtd[3] >= 1 and qtd[4] >= 1 and qtd[5] >= 1 and qtd[6] >= 1:
        return 15
    else:
        return 0