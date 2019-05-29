#!/bin/env python3
# coding: utf-8

# Marco André <marco.mendes@ifc.edu.br>
# Avaliação de strings e listas


def extrai_pontuacao(texto):
    """
    Faça uma função que receba um texto e retorne apenas os sinais
    de pontuação que esse texto contém.
    Por exemplo: Se o texto for “BSI 1 - Programação 1:” o retorno será
    a string “-:”. Observe que o espaço em branco não é contado como pontuação.

    :param texto: um texto contendo letras, números, sinais de pontuação e espaços em branco.
    :return: uma string contendo os sinais de pontuação.
    """

    pontuacao = ''
    for caractere in texto:
        if caractere in '-()/:':
            pontuacao += caractere
    return pontuacao



def soma_numeros(texto):
    """
    Faça uma função que receba um texto e retorne a soma dos números
    que esse texto contém.
    Por exemplo: Se o texto for “BSI 1 - Programação 1”
    o retorno será o valor inteiro 2 (1 + 1).

    :param texto: um texto contendo letras, números, sinais de pontuação e espaços em branco.
    :return: um valor inteiro, resultado da soma dos números contidos na string de entrada.
    """
    # novotexto = texto.lower().replace(" ", "").replace("!", "").replace("(","").replace(")","").replace("-","").replace("/","").replace(":","")
    numeros=[]
    soma=0

    for x in texto:
        if x in '123456789':
            numeros.append(int(x))
    for n in numeros:
        soma += n
    return soma


def devolve_lista_posicao_de_notas_acima_da_media_da_turma(notas):
    """Faça uma função que receba uma lista com um número indeterminado
    de notas, e retorne uma lista com a posição na lista de notas das notas
    acima da média da turma.
    Dica: você precisará calcular primeiro a média das notas da turma
    (sem utilizar funções prontas da linguagem), para então descobrir as
    notas acima da média da turma. Além disso você precisará ter acesso
    a posição na lista, para poder armazenar essa posição. Por fim, você
    precisará armazenar essas posições em uma nova lista para poder
    retorná-la ao final da função.

    :param notas: uma lista de elementos do tipo float, correspondente a notas.
    :return: uma lista de valores inteiros, correspondente as posições da lista de entrada
                cuja nota é acima da média da lista.
    """
    soma=0
    notas_acima = []

    for nota in notas:
        soma += nota
    media = soma / len(notas)

    for i,x in enumerate(notas):
        if x > media:
            notas_acima.append(i)
    return notas_acima



def encontra_mes_com_menos_chuva(chuvas_meses):
    """Faça uma função que receba uma lista contendo a quantidade de
    chuva (em mm) que caiu em cada mês de um ano.
    Descubra (sem utilizar funções prontas da linguagem) em qual mês caiu
    a menor quantidade de chuvas e devolva o nome desse mês.
    Se houver mais de um mês com o mesmo resultado, considere o primeiro mês.
    Dica: crie uma lista com o nome dos meses e use a posição da lista
    com as chuvas para chegar no nome do mês desejado.

    :param chuvas_meses: uma lista contendo 12 valores float, correspondendo
            a quantidade de chuva (em mm), que caiu em cada mês do ano.
    :return: uma string com três letras, correspondendo ao nome do mês em que
            caiu a menor quantidade de chuva no ano.
    """
    lista = ''

    meses=['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
    anterior = chuvas_meses[0]

    for chuva in chuvas_meses:
        if chuva < anterior:
            anterior = chuva
    menor = anterior

    for i,x in enumerate(chuvas_meses):
        if x == menor:
            lista += meses[i]
            return lista



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
    print('{} Esperado: {} \tObtido: {}\033[1;m'.format(prefixo, esperado, obtido))


def main():
    print('Extrai pontuação:')
    test(extrai_pontuacao('BSI1Programação1'), '')
    test(extrai_pontuacao('BSI1-Programação1'), '-')
    test(extrai_pontuacao('BSI 1 - Programação 1'), '-')
    test(extrai_pontuacao('BSI 1 - Programação 1:'), '-:')
    test(extrai_pontuacao('(47) 9177-5523'), '()-')
    test(extrai_pontuacao('29/10/1973'), '//')

    print('Soma números:')
    test(soma_numeros(''), 0)
    test(soma_numeros('12345'), 15)
    test(soma_numeros('BSI Programação'), 0)
    test(soma_numeros('(47) 9177-5523'), 50)
    test(soma_numeros('29/10/1973'), 32)


    print('Quantidade de notas acima da média da turma:')
    test(devolve_lista_posicao_de_notas_acima_da_media_da_turma([9, 9, 9, 9, 9, 9]), [])
    test(devolve_lista_posicao_de_notas_acima_da_media_da_turma([8, 10, 8, 8, 8, 8]), [1])
    test(devolve_lista_posicao_de_notas_acima_da_media_da_turma([10, 10, 9, 9, 9, 8]), [0, 1])
    test(devolve_lista_posicao_de_notas_acima_da_media_da_turma([9, 10, 9, 9, 9, 10]), [1, 5])
    test(devolve_lista_posicao_de_notas_acima_da_media_da_turma([10, 10, 9, 9, 9, 10]), [0, 1, 5])

    print('Encontra mês com menos chuva:')
    test(encontra_mes_com_menos_chuva([10, 20, 15, 9, 12, 25, 23, 14, 21, 20, 16, 17]), 'abr')
    test(encontra_mes_com_menos_chuva([10, 20, 9, 9, 12, 25, 23, 14, 21, 20, 16, 17]), 'mar')
    test(encontra_mes_com_menos_chuva([10, 20, 20, 20, 12, 25, 23, 14, 21, 20, 16, 17]), 'jan')
    test(encontra_mes_com_menos_chuva([10, 20, 20, 20, 12, 25, 23, 14, 21, 20, 16, 9]), 'dez')
    test(encontra_mes_com_menos_chuva([9, 20, 20, 20, 12, 25, 23, 14, 21, 20, 16, 9]), 'jan')


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")