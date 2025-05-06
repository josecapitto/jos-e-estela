from funcoes import rolar_dados, guardar_dado, remover_dado, calcula_pontos_regra_simples, calcula_pontos_soma, calcula_pontos_sequencia_baixa, calcula_pontos_sequencia_alta, calcula_pontos_full_house, calcula_pontos_quadra, calcula_pontos_quina, calcula_pontos_regra_avancada, faz_jogada, imprime_cartela
# Variaveis para guardar os pontos de cada ponto da regra avancada 
# cinco_iguais = 0
# full_house = 0 
# quadra = 0
# sem_combinacao = 0 
# sequencia_baixa = 0
# sequencia_alta = 0

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


imprime_cartela(cartela)

# Primeira rolada de dados 
qntd = 5
dados_rolados = rolar_dados(qntd)
print(f"Dados rolados: {dados_rolados}")

# Dados guardados (vazio por enquanto)
dados_guardados = []
print(f"Dados guardados: {dados_guardados}")

# Variavel para que o while de verificar combinacoes funcione (linha 69)
combinacao = " "

# Varivaeis para que o whiles a seguir funcionem
comando = 1
i = 0 

# While para que o jogo dure 12 rodadas (linha 117 está a soma de seu i, contando cada rodada)
while i < 12:    
    
    dados_guardados = []        
    qntd = 5                  
    dados_rolados = rolar_dados(qntd)


    # rerro = rerrolagem (tem que reinicar a cada rodada)
    rerro = 0
    comando = 1
    combinacao = " "
    # while que depende do comando para parar (ele parar apenas quando for contabilizar as combinacoes)
    while comando != '0':
        comando = input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        # OS IFS que funcionam dependendo do comando 
        # if (1) adiciona nos dados_guardados
        if comando == '1':
            indice_g = int(input("Digite o índice do dado a ser guardado (0 a 4):"))

            # try:
            #     indice_g = int(input("Digite o índice do dado a ser guardado (0 a 4):"))
            # except ValueError:
            #     print("Índice inválido. Tente novamente.")
            #     continue

            result_g = guardar_dado(dados_rolados, dados_guardados, indice_g)
        
            dados_rolados = result_g[0]
            dados_guardados = result_g[1]

            # print(f"Dados rolados: {dados_rolados}")
            # print(f"Dados guardados: {dados_guardados}")
        # if (2) retira dos dados_guardados
        elif comando == '2':
            indice_r = int(input("Digite o índice do dado a ser guardado (0 a 4):"))
            # try:
            #     indice_r = int(input("Digite o índice do dado a ser guardado (0 a 4):"))
            # except ValueError:
            #     print("Índice inválido. Tente novamente.")
            #     continue
            result_r = remover_dado(dados_rolados, dados_guardados, indice_r)
            dados_rolados = result_r[0]
            dados_guardados = result_r[1]

            # print(f"Dados rolados: {dados_rolados}")
            # print(f"Dados guardados: {dados_guardados}")
        # if (3) faz a rerrolagem
        elif comando == '3':
            if rerro < 2:
                qntd = len(dados_rolados)
                dados_rolados = rolar_dados(qntd)

                rerro += 1
                # print(f"Dados rolados: {dados_rolados}")
                # print(f"Dados guardados: {dados_guardados}")
            else:
                print("Você já usou todas as rerrolagens.")
                # print(f"Dados rolados: {dados_rolados}")
                # print(f"Dados guardados: {dados_guardados}")
        # if (4) imprime a cartela
        elif comando == '4':
            imprime_cartela(cartela)
        elif comando == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

    
    # while para verificar qual combinacao colocar na cartela 

    while combinacao == " ":
        combinacao = input("Digite combinação desejada:")
        if combinacao in ['1', '2', '3', '4', '5', '6']:
            if cartela['regra_simples'][int(combinacao)] != -1:
                print("Essa combinação já foi utilizada.")
            else:
                cartela = faz_jogada(dados_guardados, combinacao, cartela)
        elif combinacao in cartela['regra_avancada']:
            if cartela['regra_avancada'][combinacao] != -1:
                print("Essa combinação já foi utilizada.")
            else:
                cartela = faz_jogada(dados_guardados, combinacao, cartela)
        else:
            print("Combinação inválida. Tente novamente.")
    dados_guardados = []
    qntd = 5
    dados_rolados = rolar_dados(qntd)
    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")

    i+=1 #AAAA 

imprime_cartela(cartela)

pontuacao_final = 0
soma_simples = 0

for valor in cartela['regra_simples'].values():
    if valor > 0:
        soma_simples += valor
        pontuacao_final += valor

if soma_simples >= 63:
    pontuacao_final += 35

for valor in cartela['regra_avancada']:
    if valor != -1:
        pontuacao_final += int(valor)

print(f"Pontuação total: {pontuacao_final}")
