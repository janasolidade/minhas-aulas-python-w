def multiplicacao():
    mult = 10*2
    file = 'arquivo.txt'

    # Abertura de arquivo

    # abertura para escrita
    arquivo_escrita = open(file, "w")
    arquivo_escrita.write(f'O resultado da multiplicação é: {mult}')
    arquivo_escrita.close() # deve ser fechado antes de abrir novamente

    #leitura somente para leitura
    arquivo_leitura = open(file, "r")
    leitura = arquivo_leitura.read()
    print(leitura)
    arquivo_leitura.close()
    
    # abertura de arquivos binários
    #arquivo_binario = open(file, "wb")
    
    

multiplicacao() #chamada da função