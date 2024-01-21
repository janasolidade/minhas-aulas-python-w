# FUNÇÕES

# def nomedafunçao ():
 #   instruções ficam dentro da função
# mostrar_mensagem() ----> chamada de função

def soma(): # definição da função soma
    calculo = 10+2
    print(f'O resultado da soma é: {calculo}')
# soma() # chamando a função


def subtracao():
    sub = 10-2
    print(f'O resultado da subtracao é: {sub}')
    multiplicacao() # chamando função dentro de uma função


def multiplicacao():
    mult = 10*2
    print(f'O resultado da multiplicação é: {mult}')

soma() # chamando a função
subtracao()
