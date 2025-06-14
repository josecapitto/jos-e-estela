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
    dic = {}
    for numero in sequencia:
        if numero in dic:
            dic[numero] += 1
        else:
            dic[numero] = 1

    tem_quadra = False
    for valor in dic.values():
        if valor >= 4:
            tem_quadra = True
            break

    if tem_quadra:
        soma = 0
        for num in sequencia:
            soma = soma + num  # soma manual, sem sum()
        return soma
    else:
        return 0


# Questão 10 - Faz pontos de quina
def calcula_pontos_quina (sequencia):
    dic = {}
    for numero in sequencia:
        if numero in dic:
            dic[numero] += 1 
        else:
            dic[numero] = 1
    
    for valores in dic.values():
        if valores >= 5:
            return 50      
    return 0

# Questão 11 - Cartela com os pontos 
def calcula_pontos_regra_avancada(sequencia):
    val_cinco = calcula_pontos_quina(sequencia)
    val_full = calcula_pontos_full_house(sequencia)
    val_quadra = calcula_pontos_quadra(sequencia)
    val_baixo = calcula_pontos_sequencia_baixa(sequencia)
    val_alto = calcula_pontos_sequencia_alta(sequencia)
    val_qlqr = calcula_pontos_soma(sequencia)

    dic = {}
    dic['cinco_iguais'] = val_cinco
    dic['full_house'] = val_full
    dic['quadra'] = val_quadra
    dic['sem_combinacao'] = val_qlqr
    dic['sequencia_alta'] = val_alto
    dic['sequencia_baixa'] = val_baixo
    return dic

# Questão 12 - Faz jogada
def faz_jogada(dados, categoria, aonde_joga):
    if categoria in ['1', '2', '3', '4', '5', '6']:
        pontos = calcula_pontos_regra_simples(dados)
        num_categoria = int(categoria)
        pontuacao = pontos[num_categoria]
        aonde_joga['regra_simples'][num_categoria] = pontuacao
    else:
        pontos = calcula_pontos_regra_avancada(dados)
        aonde_joga['regra_avancada'][categoria] = pontos[categoria]
    return aonde_joga

# Cartela do Jogo
def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)