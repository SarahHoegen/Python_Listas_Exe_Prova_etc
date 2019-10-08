#!/bin/env python3
# Marco André <marco.mendes@ifc.edu.br>
# Avaliação - Faça os exercícios utilizando repetição com while
# Renomeie o arquivo, incluindo seu nome.
# Coloque o nome do arquivo como assunto do email e envie para o
# endereço acima.


def quantidade_de_pares(valor_inicial, valor_final):
    ''' Determine a quantidade de números ímpares num intervalo.
    Dica: inclua os extremos, isso é, o valor_inicial e o valor final do
    intervalo.'''

    qtd=0
    numero=valor_inicial

    while numero <= valor_final:
        if numero%2 == 0:
            qtd +=1
        numero+=1
    return qtd


def Fibonacci(n):
    ''' Retorne uma lista com os primeiros "n" elementos da série de Fibonacci
    Fibonacci = 1,1,2,3,5,8,13,...'''

    fibovelho =1
    fiboatual = 1
    fibonacci = 0
    numero = 0
    lista=[]


    while numero < n:

        lista.append(fibovelho)
        fibonacci = fiboatual + fibovelho
        fibovelho = fiboatual
        fiboatual = fibonacci


        numero += 1

    return lista



def serie_pi(vezes):
    ''' Calcule o valor de pi através da série
    4/1 - 4/3 + 4/5 - 4/7 + ... - 4/n, sendo informado o número de
    itens (vezes).'''

    pi=4/1
    numero = 1
    divisor=3
    sinal = -1

    while numero < vezes:
        pi += 4/divisor*sinal
        divisor+=2
        sinal *= -1
        numero += 1

    return round(pi,6)



def intercalamento_contrario(lista1, lista2):
    ''' Usando 'lista1' e 'lista2', ambas do mesmo comprimento,
    crie uma nova lista composta pelo intercalamento entre as duas.
    A primeira lista deve ser usada na ordem normal. Já a segunda, deve
    ser utilizada na ordem inversa.'''


    lista3=[]

    for elemento1,elemento2 in zip(lista1,lista2[::-1]):
        lista3.append(elemento1)
        lista3.append(elemento2)
    return lista3



def maiores_13(idades, alturas):
    '''Esta função recebe as idades e alturas de diversas pessoas, em duas
    listas separadas e de igual comprimento.
    Calcule a media das alturas e retorne as alturas daqueles que possuem
    'idades' maior que 13 e altura inferior a media de altura da turma'''

    soma=0
    saida=[]

    for z in alturas:
        soma += z
    media_altura = soma / len(alturas)
    for x,y in zip(idades,alturas):
        if (x > 13) and (y < media_altura):
            saida.append(y)
    return saida



# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % ('Falhou')
    else:
        prefixo = '\033[32m%s' % ('Passou')
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():
    print('Quantidade de pares:')
    test(quantidade_de_pares(1, 1), 0)
    test(quantidade_de_pares(1, 2), 1)
    test(quantidade_de_pares(2, 3), 1)
    test(quantidade_de_pares(2, 4), 2)
    test(quantidade_de_pares(1, 10), 5)

    print('Fibonnaci:')
    test(Fibonacci(1), [1])
    test(Fibonacci(2), [1, 1])
    test(Fibonacci(3), [1, 1, 2])
    test(Fibonacci(4), [1, 1, 2, 3])
    test(Fibonacci(5), [1, 1, 2, 3, 5])

    print('Série pi:')
    test(serie_pi(1), 4.000000)
    test(serie_pi(2), 2.666667)
    test(serie_pi(3), 3.466667)
    test(serie_pi(4), 2.895238)
    test(serie_pi(5), 3.339683)
    test(serie_pi(6), 2.976046)
    test(serie_pi(7), 3.283738)
    test(serie_pi(8), 3.017072)
    test(serie_pi(1000), 3.140593)
    test(serie_pi(9000), 3.141482)

    print(' Lista intercalada contrária:')
    test(intercalamento_contrario([], []), [])
    test(intercalamento_contrario([1], [2]), [1, 2])
    test(intercalamento_contrario([1, 2], [3, 4]), [1, 4, 2, 3])
    test(intercalamento_contrario([1, 2, 3], [4, 5, 6]), [1, 6, 2, 5, 3, 4])
    test(intercalamento_contrario([1, 2, 3, 4, 5], [
         6, 7, 8, 9, 10]), [1, 10, 2, 9, 3, 8, 4, 7, 5, 6])

    print(' Alturas abaixo da media:')
    test(maiores_13([13, 13, 14], [1.7, 1.7, 1.5]), [1.5])
    test(maiores_13([13, 13, 14, 13], [1.7, 1.7, 1.5, 1.6]), [1.5])
    test(maiores_13([14, 20], [1.6, 2]), [1.6])
    test(maiores_13([10, 7, 13, 15, 20, 21], [
         1.7, 1.21, 1.65, 2, 1.9, 1.5]), [1.5])
    test(maiores_13([14, 15, 16, 17, 18, 30], [
         1.9, 1.89, 1.85, 1.95, 2, 1.99]), [1.9, 1.89, 1.85])
    test(maiores_13([10, 9, 90, 9, 13, 14, 15], [
         1.25, 1.3, 1.7, 1.41, 1.5, 1.55, 1.7]), [])


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")