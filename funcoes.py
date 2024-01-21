# FUNÇÕES

# def nomedafunçao ():
 #   instruções ficam dentro da função
# mostrar_mensagem() ----> chamada de função

def soma(num1, num2): # definição da função soma
    
    calculo = num1+num2

    print(f'O resultado da soma é: {calculo}')
# soma() # chamando a função


def subtracao(num1, num2):
    sub = 10-2
    print(f'O resultado da subtracao é: {sub}')
    #multiplicacao() # chamando função dentro de uma função


def multiplicacao(num1, num2):
    mult = 10*2
    print(f'O resultado da multiplicação é: {mult}')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma(num1, num2) # chamando a função
subtracao(num1, num2)
multiplicacao(num1, num2)

#Trabalhando com parâmetros
