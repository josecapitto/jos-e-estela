from funcoes import rolar_dados, guardar_dado, remover_dado, calcula_pontos_regra_simples, calcula_pontos_soma, calcula_pontos_sequencia_baixa, calcula_pontos_sequencia_alta, calcula_pontos_full_house, calcula_pontos_quadra, calcula_pontos_quina, calcula_pontos_regra_avancada, faz_jogada, imprime_cartela
# Variaveis para guardar os pontos de cada ponto da regra avancada 
cinco_iguais = 0
full_house = 0 
quadra = 0
sem_combinacao = 0 
sequencia_baixa = 0
sequencia_alta = 0

# Cartela do jogo (vazia por enquanto) e o print dela 
cartela= {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
print(imprime_cartela(cartela))

# Primeira rolada de dados 
qntd = 5
dados_rolados = rolar_dados(qntd)
print(dados_rolados)

# Dados guardados (vazio por enquanto)
dados_guardados = []
print(f"Dados guardados {dados_guardados}")

# Variavel para que o while de verificar combinacoes funcione (linha 69)
combinacao = " "

# Varivaeis para que o whiles a seguir funcionem
comando = 1
i = 0 

# While para que o jogo dure 12 rodadas (linha 117 está a soma de seu i, contando cada rodada)
while i < 12:
    # rerro = rerrolagem (tem que reinicar a cada rodada)
    rerro = 0 
    # while que depende do comando para parar (ele parar apenas quando for contabilizar as combinacoes)
    while comando != 0:
        comando = int(input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:"))
        # OS IFS que funcionam dependendo do comando 
        # if (1) adiciona nos dados_guardados
        if comando == 1:
            indice_g = int(input("Digite o índice do dado a ser guardado (0 a 4):"))
            num = dados_rolados[indice_g]
            dados_guardados.append(num)
            del dados_rolados[indice_g]
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
        # if (2) retira dos dados_guardados
        elif comando == 2:
            indice_r = int(input("Digite o índice do dado a ser removido (0 a 4):"))
            num2 = dados_guardados[indice_r]
            dados_rolados.append(num2)
            del dados_guardados[indice_r]
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
        # if (3) faz a rerrolagem
        elif comando == 3:
            if rerro < 2:
                qntd = len(dados_rolados)
                dados_rolados = rolar_dados(qntd)
                rerro += 1
                print(f"Dados rolados: {dados_rolados}")
                print(f"Dados guardados: {dados_guardados}")
            else:
                print("Você já usou todas as rerrolagens.")
                print(f"Dados rolados: {dados_rolados}")
                print(f"Dados guardados: {dados_guardados}")
        # if (4) imprime a cartela
        elif comando == 4:
            print(imprime_cartela(cartela))
    # while para verificar qual combinacao colocar na cartela 
    while combinacao != " ":          
        combinacao = input("Digite combinação desejada:")
        # QUINA
        if combinacao == "cinco_iguais":
            if cinco_iguais > 0:
                print("Essa combinação já foi utilizada.")
                combinacao = " "
            else:
                cinco_iguais = calcula_pontos_quina(dados_guardados)
                cartela['regra_avancada']['cinco_iguais'] = cinco_iguais
        # QUADRA
        elif combinacao == "quadra":
            if quadra > 0:
                print("Essa combinação já foi utilizada.")
                combinacao = " "
            else:
                quadra = calcula_pontos_quadra(dados_guardados)
                cartela['regra_avancada'['quadra']] = quadra
        # Full_HOUSE
        elif combinacao == "full_house":
            if full_house > 0:
                print("Essa combinação já foi utilizada.")
                combinacao = " "
            else:
                full_house = calcula_pontos_full_house(dados_guardados)
                cartela['regra_avancada']['full_house'] = full_house
        # SEQUENCIA_BAIXA
        elif combinacao == "sequencia_baixa":
            if sequencia_baixa > 0:
                print("Essa combinação já foi utilizada.")
                combinacao = " "
            else:
                sequencia_baixa = calcula_pontos_sequencia_baixa(dados_guardados)
                cartela['regra_avancada']['sequencia_baixa'] = sequencia_baixa
        # SEQUENCIA_ALTA
        elif combinacao == "sequencia_alta":
            if sequencia_alta > 0:
                print("Essa combinação já foi utilizada.")
                combinacao = " "
            else:
                sequencia_alta = calcula_pontos_sequencia_alta(dados_guardados)
                cartela['regra_avancada']['sequencia_alta'] = sequencia_alta
        # SEM_COMBINACAO
        elif combinacao == "sem_combinacao":
            if sem_combinacao > 0:
                print("Essa combinação já foi utilizada.")
                combinacao = " "
            else:
                sem_combinacao = calcula_pontos_sequencia_baixa(dados_guardados)
                cartela['regra_avancada']['sem_combinacao'] = sem_combinacao

    i += 1 

