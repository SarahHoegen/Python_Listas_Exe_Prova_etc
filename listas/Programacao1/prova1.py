#!/bin/env python3
# Marco André Mendes <marco.mendes@ifc.edu.br>

def converte_hora(horario):
    """
    :param horario: horario em string, no formato "hh:mm"
    :return: horario no formato am/pm

    Recebe um horário no formato 24 horas e retorna no formato am/pm
    am: antes do meio-dia
    pm: depois do meio-dia
    """
    h, m = horario.split(':')
    h=int(h)


    if h <= 12:

        return "%d:%s %s" %(h,m,'am')
    else:
        hora=h-12
        return "%d:%s %s" %(hora,m,'pm')




def nota_para_conceito(nota):
    """
    :param nota: uma nota de uma disciplina, em float
    :return: o conceito no formato string, de A até E, conforme a tabela abaixo:
    Nota                     Conceito
    Entre 10.0 e 9.0            A
    Entre 8.9 e 8.0             B
    Entre 7.9 e 7.0             C
    Entre 6.9 e 6.0             D
    Entre 5.9 e zero            E
    """

    if(nota>=9 and nota<=10):
        return "A"
    elif(nota>=8 and nota<=8.9):
        return "B"
    elif(nota>=7 and nota<=7.9):
        return "C"
    elif(nota>=6 and nota<=6.9):
        return "D"
    else:
        return "E"



def situacao_aluno(nota1, nota2, nota3, faltas, aulas_ministradas):
    """
    :param nota1: 1a nota em float
    :param nota2: 2a nota em float
    :param nota3: 3a nota em float
    :param faltas: número de faltas do aluno na disciplina
    :param aulas_ministradas: Total de aulas ministradas
    :return: retorna situação do aluno como valor booleano

    A média do aluno é dada pela média aritmética simples entre as 3 notas.
    Se o aluno tiver mais de 25% de faltas, está automaticamente reprovado por faltas (RF).
    Se ele tiver média abaixo de 7.0, está em Exame Final (EF)
    Se tiver média acima de 7.0 e frequencia igual ou superior a 75% está aprovado (AP).
    """

    # aulas_idas= aulas_ministradas-faltas
    #
    # porcentagem= (aulas_idas*100)/aulas_ministradas

    frequencia_falta =(faltas*100/aulas_ministradas)
    media= (nota1+nota2+nota3)/3

    if(frequencia_falta)> (25):
        return "RF"

    elif(media<7):
        return "EF"

    else:
        return "AP"


def conta_combustivel(qtde_litros, tipo_combustivel, tipo_pagamento):
    """
    :param qtde_litros: em float
    :param tipo_combustivel: uma string de uma letra, a inicial do combustível
    :param tipo_pagamento: uam string, identificando o tipo de pagamento
    :return: o valor a ser pago, com 2 casas decimais

    O posto Tabajara está vendendo combustíveis com a seguinte tabela de preços:
        a. Tabela de preços
            Álcool: R$ 3,159
            Gasolina: R$ 3,739
            Diesel: 3,090
        b. Se o pagamento for feito à vista ou débito, o cliente recebe um desconto de 10% sobre o valor total
        c. Escreva um função que leia o número de litros vendidos, o tipo de combustível (gasolina, álcool, diesel),
            e o tipo de pagamento (à vista, débito, crédito), calcule e devolva o valor total da compra.
    """
    if(tipo_combustivel =='a'):
        tipo_combustivel= 3.159

    elif(tipo_combustivel =='g'):
        tipo_combustivel=3.739

    else:
        tipo_combustivel=3.090

    valor=qtde_litros*tipo_combustivel

    if(tipo_pagamento=='v') or (tipo_pagamento=='d'):
        desconto= (valor*0.10)
        valor_total=valor-desconto

        return round(valor_total,2)
    else:
        valor_total=valor
        return round(valor_total,2)




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
    print('\033[1;m')

    print('Conversão de horário:')
    test(converte_hora("1:1"), '1:1 am')
    test(converte_hora("10:10"), '10:10 am')
    test(converte_hora("12:00"), '12:00 am')
    test(converte_hora("12:01"), '12:01 am')
    test(converte_hora("12:59"), '12:59 am')

    test(converte_hora("13:00"), '1:00 pm')
    test(converte_hora("23:59"), '11:59 pm')

    test(converte_hora("0:0"), '0:0 am')
    test(converte_hora("0:1"), '0:1 am')

    print('Nota para conceito:')
    test(nota_para_conceito(10.0), 'A')
    test(nota_para_conceito(9.1), 'A')
    test(nota_para_conceito(9.0), 'A')
    test(nota_para_conceito(8.9), 'B')
    test(nota_para_conceito(8.1), 'B')
    test(nota_para_conceito(8.0), 'B')
    test(nota_para_conceito(7.9), 'C')
    test(nota_para_conceito(7.1), 'C')
    test(nota_para_conceito(7.0), 'C')
    test(nota_para_conceito(6.9), 'D')
    test(nota_para_conceito(6.1), 'D')
    test(nota_para_conceito(6.0), 'D')
    test(nota_para_conceito(5.9), 'E')
    test(nota_para_conceito(5.1), 'E')
    test(nota_para_conceito(5.0), 'E')
    test(nota_para_conceito(4.9), 'E')
    test(nota_para_conceito(4.0), 'E')

    print('Situacao aluno:')
    test(situacao_aluno(10, 10, 10, 18, 72), 'AP')
    test(situacao_aluno(7, 7, 7, 18, 72), 'AP')
    test(situacao_aluno(6, 7, 8, 18, 72), 'AP')
    test(situacao_aluno(7, 7, 6, 18, 72), 'EF')
    test(situacao_aluno(7, 7, 6.9, 18, 72), 'EF')
    test(situacao_aluno(5, 7, 7, 18, 72), 'EF')
    test(situacao_aluno(10, 10, 10, 19, 72), 'RF')
    test(situacao_aluno(10, 10, 10, 20, 72), 'RF')
    test(situacao_aluno(0, 0, 0, 30, 72), 'RF')

    print('Conta combustível:')
    test(conta_combustivel(1, 'a', 'c'), 3.16)
    test(conta_combustivel(10, 'a', 'c'), 31.59)
    test(conta_combustivel(1, 'g', 'c'), 3.74)
    test(conta_combustivel(10, 'g', 'c'), 37.39)
    test(conta_combustivel(1, 'd', 'c'), 3.09)
    test(conta_combustivel(10, 'd', 'c'), 30.90)

    test(conta_combustivel(1, 'a', 'd'), 2.84)
    test(conta_combustivel(10, 'a', 'd'), 28.43)
    test(conta_combustivel(1, 'g', 'd'), 3.37)
    test(conta_combustivel(10, 'g', 'd'), 33.65)
    test(conta_combustivel(1, 'd', 'd'), 2.78)
    test(conta_combustivel(10, 'd', 'd'), 27.81)
    test(conta_combustivel(10, 'a', 'v'), 28.43)
    test(conta_combustivel(10, 'g', 'v'), 33.65)
    test(conta_combustivel(10, 'd', 'v'), 27.81)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")