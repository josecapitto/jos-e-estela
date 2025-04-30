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
def calcula_pontos_soma(sequência):
    soma = 0
    soma1 = 0 
    if sequência == [1, 2, 3, 4] or sequência == [2, 3, 4, 5] or sequência == [3, 4, 5, 6]:
        valor = 15
    if sequência == [1, 2, 3, 4, 5] or sequência == [2, 3, 4, 5, 6]:
        valor = 30
    else:
        for numero in sequência:
            soma += numero
            valor = soma
    if len(sequência) == 5:
        num = sequência[0]
        for i in sequência:
            if num != i:
                for numero in sequência:
                    soma1 += numero
                    valor = soma1
                break
            else:
                valor = 50
    return valor 


# Questão 8 - Calcula pontuação do full-house
def calcula_pontos_full_house(sequencia):
    dic = {}
    for numero in sequencia:
        if numero in dic:
            dic[numero] += 1 
        else:
            dic[numero] = 1
    

    for i in dic:
        if dic[i] == 3 or dic[i] == 2:
            soma = 0 
            for j in sequencia:
                soma += j
                valor = soma
        else:
            valor = 0 
    return valor 
