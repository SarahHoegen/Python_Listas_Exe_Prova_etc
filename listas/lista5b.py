#!/bin/env python3
# Marco André Mendes <marco.mendes@ifc.edu.br>
# Criada por Felipe Tiago Guimarães <felipeguimaraes0025@gmail.com>
# Exercícios retirados do livro de Python de Raul Waslawick
# Lista de exercícios 2 - while


def corrida(vantagem, vlc_tartaruga, vlc_lebre):
    """A tartaruga e a lebre vão apostar uma corrida. A lebre concede à
        tartaruga o direito de sair a uma vantagem em metros a sua frente.
        A tartarua corre a uma velocidade em metros por segundo (vlc_tartaruga)
        e a lebre corre a uma outra velocidade em metros por segundo (vlc_lebre).
        Desenvolva uma função que calcule quantos minutos são necessários para
        a lebre alcançar a tartaruga."""

    minutos = 0
    metros_lebre = 0
    metros_tartaruga = vantagem

    if vlc_tartaruga > vlc_lebre and vantagem > 0:
        return -1
    elif vlc_tartaruga > vlc_lebre:
        return 0
    else:
        while metros_lebre <= metros_tartaruga:
            metros_lebre += vlc_lebre
            metros_tartaruga += vlc_tartaruga
            minutos += 1
    return minutos


def sub_sucessivas(dividendo, divisor):
    """Escreva um programa que calcula a divisão inteira e o resto da divisão inteira
    entre dois números inteiros positivos usando o método das subtrações sucessivas.
    A técnica consiste em subtrair o divisor do dividendo até que o dividendo se torne
    menor que o divisor. Neste instante, o número de subtrações feitas será o valor da
    divisão inteira e o valor atual do dividendo será o resto.
    Não vale roubar usando módulos prontos do Python e obviamente divisão por
    ZERO não é permitida, afinal não conseguimos representar o INFINITO =)"""

    if divisor == 0:
        return "Parabéns, vc alcançou o Infinito!!"
    else:
        # divisao = dividendo//divisor
        contador = 0 #contador é o valor da divisão inteira, por isso não preciso fazer a linha de código acima

        while dividendo >= divisor:
            dividendo -= divisor
            contador +=1
        return (contador,dividendo)



def compra(aplicacao, valor_carro):
    """Você tem uma certa aplicação financeira com um saldo determinado, que
    rende 0.7% ao mês. Você deseja comprar um carro que custa um determinado
    preço. Porém, o preço do carro sobe à uma taxa de 0,3% ao mês.
    Faça um programa que calcule quantos meses serão necessários até que,
    com essa aplicação, você consiga comprar o carro à vista."""

    taxa_car = 0.003 + 1
    taxa_aplica = 0.007+ 1 #coloco +1 para não precisar somar o valor da aplicacao na conta que está no while
    meses=0

    while aplicacao < valor_carro:
        valor_carro *= taxa_car
        aplicacao *= taxa_aplica        #se não tivesse taxa_aplica +1, eu teria que somar a essa conta a aplicacao
        meses += 1                      #aplicacao = (taxa_aplica*aplicacao) + aplicacao

    return meses


def serie_infinita(x, i):
    """Faça um programa que tenha como objetivo se aproximar da série
     infinita e^x.
     A fórmula de aproximação é a seguinte:
        e^x = 1 + x + (x²/2!) + (x³/3!) + (x⁴/4!) + ...
    Sendo i o número de termos somados. Quanto maior o número de termos,
    maior a precisão do valor encontrado.
    Na expressão, cada uma das partes formadas por (x^y/y!) é denominada termo."""

    # serie = 1+x
    # numero=1

    fatorial=1
    numero=3

    for n in range(0, numero):
        fatorial *= numero
        numero -= 1
    

    # while numero <= i:
    #     serie += x**numero/numero
    #     numero+=1




def populacao_dodo(populacao):
    """ O dodô é uma ave não voadora, extinta atualmente, e que era endêmica
    da ilha Mauritius, na costa leste da África. A população inicial de dodôs
    era de 1 milhão de indivíduos no ínicios de 1600. A partir dessa data, durante
    cada ano, 6% dos animais vivos do começo do ano morreram. O número de animais
    nascidos ao longo do ano foi de 1% da população anual.
    Escreva um programa que retorne o ano em que a população de dodôs cai para
    menos de 10% da população inicial.
    """
    return 1645


def matriz(n):
    """Crie uma matriz quadrada nxn utilizado while, cuja função de
    atribuição é A[i][j] = i+j. A partir da matriz criada, retorne a
    soma da diagonal principal."""


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31mFalhou'
    else:
        prefixo = '\033[32mPassou'
        acertos += 1
    print('{} Esperado: {} \tObtido: {}\033[1;m'.format(
        prefixo, esperado, obtido))


def main():
    print('Corrida:')
    test(corrida(100, 2, 5), 34)
    test(corrida(200, 7, 6), -1)
    test(corrida(0, 2, 5), 0)
    test(corrida(0, 7, 6), 0)
    test(corrida(5884, 4, 5), 5885)

    print('Suntrações Sucessivas:')
    test(sub_sucessivas(17, 4), (4, 1))
    test(sub_sucessivas(50, 5), (10, 0))
    test(sub_sucessivas(3, 9), (0, 3))
    test(sub_sucessivas(25, 1), (25, 0))
    test(sub_sucessivas(24, 0), ("Parabéns, vc alcançou o Infinito!!"))

    print('Compra:')
    test(compra(10000.00, 12000.00), (46))
    test(compra(15000.00, 22000.00), (97))
    test(compra(40000.00, 32000.00), (0))
    test(compra(50000.00, 52000.00), (10))

    print('Série Infinita:')
    test(serie_infinita(2, 2), (5.0))
    test(serie_infinita(1, 0), (1.0))
    test(serie_infinita(2, 7), (7.3809523809523805))
    test(serie_infinita(2, 6), (7.355555555555555))
    test(serie_infinita(2, 1), (3.0))
    test(serie_infinita(7, 57), (1096.6331584284578))

    print('População Dodo:')
    test(populacao_dodo(1000000), 1645)

    print('Matriz:')
    test(matriz(4), 20)
    test(matriz(2), 6)
    test(matriz(7), 56)
    test(matriz(5), 30)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")