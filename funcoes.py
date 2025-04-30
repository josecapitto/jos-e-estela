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

# Questão 2 - Função para verificar se o dado é válido
def guardar_dado(rolados, estoque, guardar): 
    guarda = rolados[guardar]
    estoque.append(guarda)
    del rolados[guardar]
    return [rolados, estoque]

# Questão 3 - Função para verificar se o dado é válido
def remover_dado(rodados_, guardados_, dado_sai):
    sai = guardados_[dado_sai]
    rodados_.append(sai)
    del guardados_[dado_sai]
    return [rodados_, guardados_]

# Questão 4 - Função para verificar se o dado é válido
def calcula_pontos_regra_simples (faces):
    qtd = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for face in faces:
        if face in qtd:
            qtd[face] += 1
    pontos = {}
    for i in qtd.keys():
        pontos[i] = qtd[i] * i
    return pontos

# Questão 5 - Função para calcular pontos
def calcula_pontos_soma(sequencia):
    soma = 0 
    for i in sequencia:
        soma += i
        valor = soma
    return valor

# Questão 6 - Função para calcular a pontuação de sequencia baixa
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

#Questão 7 - Função para calcular a pontuação de sequencia alta
def calcula_pontos_sequencia_alta (faces):
    qtd = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for face in faces:
        if face in qtd:
            qtd[face] += 1
    
    if qtd[1] >= 1 and qtd[2] >= 1 and qtd[3] >= 1 and qtd[4] >= 1 and qtd[5] >= 1:
        return 30
    elif qtd[2] >= 1 and qtd[3] >= 1 and qtd[4] >= 1 and qtd[5] >= 1 and qtd[6] >= 1:
        return 30
    else:
        return 0

# Questão 8 - Calcula pontuação do full-house
def calcula_pontos_full_house(sequencia):
    soma = 0 
    dic = {}
    for numero in sequencia:
        if numero in dic:
            dic[numero] += 1 
        else:
            dic[numero] = 1
    if 2 in dic.values() and 3 in dic.values():
        for num in sequencia:
            soma += num
            valor = soma
    else:
        valor = 0 
    return valor  

# Questão 9 - Faz pontos da quadra 
def calcula_pontos_quadra(sequencia):
    soma = 0 
    dic = {}
    for numero in sequencia:
        if numero in dic:
            dic[numero] += 1 
        else:
            dic[numero] = 1
    
    for valores in dic.values():
        if valores >= 4:
            for num in sequencia:
                soma += num
                valor = soma
            break       
    else:
        valor = 0 
    return valor