def remover_dado(rodados, guardados, dado_sai):
    sai = guardados[dado_sai]
    rodados.append(sai)
    del guardados[dado_sai]
    return [rodados, guardados]
