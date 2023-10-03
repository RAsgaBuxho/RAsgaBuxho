while True:
    print('Use ponto ao invés de vírgula')  # Imprime uma mensagem para o usuário
    concentracao = float(input('Qual a concentração da amostra? '))  # Obtém a concentração como um número decimal
    forca = float(input('Qual a força da amostra? (sem o %) '))  # Obtém a força como um número decimal (assumindo que é uma porcentagem)
    
    # Calcula o resultado com base na concentração e força (percentagem)
    resultado = concentracao / (forca / 100)
    
    if forca != 100:
        tecido = float(input('Qual a massa do seu tecido? '))  # Obtém a massa do tecido como um número decimal
        if tecido != 0:
            total = tecido * resultado  # Calcula a quantidade total
            print(f'q quantitade para pipetar  é: {total}')
    
    # Pergunta ao usuário se eles querem fazer outro cálculo
    continuar = input('Deseja continuar? (Digite "s" para sim, ou qualquer outra tecla para sair) ')
    if continuar.lower() != 's':
        break  # Sai do loop se o usuário não quiser continuar
