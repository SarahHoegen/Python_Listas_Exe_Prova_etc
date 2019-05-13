# !/bin/env python3
# coding: utf-8
# Marco André <marcoandre@ifc-araquari.edu.br>
# Lista de exercícios 2.2

import math


def duzias(ovos):
    ''' Receba o número de ovos e devolva a quantidade de dúzias
    correspondente. Considere sempre dúzias cheias, arredondando pra
    cima se necessário.
    '''
    if(ovos<12):
        duzias=1
        return duzias
    else:
        duzias=ovos/12
        if(round(duzias)<duzias):
            duzias += 1
            return round(duzias)
        else:
            return round(duzias)
    #
    # if ovos <= 0:
    #     pass
    # else:
    #     return ovos // 12


def baskara(a, b, c):
    '''Calcule as raízes de uma equação do segundo grau, na forma
    ax2 + bx + c. A função recebe a, b e c e faz as consistências,
    informando ao usuário nas seguintes situações:
    - Se o usuário informar o valor de A igual a zero é uma equaçao do
    2o grau.
    - Se o delta calculado for negativo, a equação não possui raizes reais.
    Devolva uma tupla vazia.
    - Se o delta calculado for igual a zero a equação possui apenas uma
    raiz real. Devolva uma tupla com um único valor.
    - Se o delta for positivo, a equação possui duas raiz reais.
    Devolva uma tupla com dois elementos.
    '''
    delta=(b**2)-(4*a*c)
    if(a==0):
        x=(-c)/b
        return (x,)
    elif(delta<0):
        return ()
    elif(delta==0):
        x=-b/(2*a)
        return (x,)
    elif(delta>0):
        x = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        return (x,x2)


def decompor_numero(numero):
    '''
    Leia um número inteiro menor que 1000 e devolva a quantidade de
    centenas, dezenas e unidades do mesmo.
    Obs.: não utilize operações com strings
    '''
    if(numero<1000):
        centena= (numero//100)
        dezena= (numero%100)//10
        unidade=((numero%100)%10)
        return (centena, dezena, unidade)
    else:
        return ()

    # import math
    #
    # if(numero<1000):
    #     centena= round(numero/100)
    #     dezena=math.floor((round(numero/10)-(centena*10)))
    #     unidade= (numero)-((centena*100)+(dezena*10))
    #     return (centena,dezena,unidade)
    # else:
    #     return ()


def caixa_eletronico(valor):
    '''Receba a valor do saque e retorne uma lista de pares de valores,
    correspondentes ao valor das notas e quantidades de notas.
    As notas disponíveis serão as de 1, 5, 10, 25, 50 e 100 reais.
    O valor é máximo de 600 reais, sem valor minimo.
    Não se preocupe com a quantidade de notas existentes na máquina.
    Procure dar sempre o número mínimo de notas, partindo das maiores
    para as menores.
    '''
    notas=[1,5,10,25,50,100]
    i=0

    if(valor==0):
        resultado=[]
        print(resultado)


    if(valor>=100):
        qtd_notas=valor//100
        valor= valor-(qtd_notas*100)

        resultado=[notas[5],qtd_notas]

        print(resultado)

    if(valor>=50):
        qtd_notas=1
        valor-=50
        resultado = [notas[4], qtd_notas]
        print(resultado)

    if(valor>=25):
        qtd_notas=1
        valor-=25
        resultado=[notas[3], qtd_notas]
        print(resultado)

    if(valor>=10):
        while(valor>=10):
            i+=1
            valor-=10
            qtd_notas=i
        resultado=[notas[2],qtd_notas]
        print(resultado)

    if(valor>=5):
        qtd_notas=1
        valor-=5
        resultado=[notas[1],qtd_notas]
        print(resultado)

    if(valor<5 and valor>0):
        resultado=[notas[0],valor]
        print(resultado)






    #calculando segundo numero






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
    print('Dúzias:')
    test(duzias(12), 1)
    test(duzias(24), 2)
    test(duzias(11), 1)
    test(duzias(23), 2)
    test(duzias(25), 3)

    print('Báskara:')
    test(baskara(1, 4, 4), (-2.0,))
    test(baskara(1, 5, 4), (-1.0, -4.0))
    test(baskara(0, 4, 2), (-0.5,))
    test(baskara(4, 4, 4), ())

    print('Decompor número:')
    test(decompor_numero(2016), ())
    test(decompor_numero(326), (3, 2, 6))
    test(decompor_numero(320), (3, 2, 0))
    test(decompor_numero(310), (3, 1, 0))
    test(decompor_numero(305), (3, 0, 5))
    test(decompor_numero(300), (3, 0, 0))
    test(decompor_numero(100), (1, 0, 0))
    test(decompor_numero(101), (1, 0, 1))
    test(decompor_numero(311), (3, 1, 1))
    test(decompor_numero(111), (1, 1, 1))
    test(decompor_numero(12), (0, 1, 2))
    test(decompor_numero(25), (0, 2, 5))
    test(decompor_numero(20), (0, 2, 0))
    test(decompor_numero(10), (0, 1, 0))
    test(decompor_numero(21), (0, 2, 1))
    test(decompor_numero(11), (0, 1, 1))
    test(decompor_numero(16), (0, 1, 6))
    test(decompor_numero(1), (0, 0, 1))
    test(decompor_numero(7), (0, 0, 7))

    print('Caixa eletrônico:')
    test(caixa_eletronico(100), [(100, 1)])
    test(caixa_eletronico(200), [(100, 2)])
    test(caixa_eletronico(150), [(100, 1), (50, 1)])
    test(caixa_eletronico(50), [(50, 1)])
    test(caixa_eletronico(175), [(100, 1), (50, 1), (25, 1)])
    test(caixa_eletronico(75), [(50, 1), (25, 1)])
    test(caixa_eletronico(125), [(100, 1), (25, 1)])
    test(caixa_eletronico(25), [(25, 1)])
    test(caixa_eletronico(250), [(100, 2), (50, 1)])
    test(caixa_eletronico(10), [(10, 1)])
    test(caixa_eletronico(20), [(10, 2)])
    test(caixa_eletronico(110), [(100, 1), (10, 1)])
    test(caixa_eletronico(120), [(100, 1), (10, 2)])
    test(caixa_eletronico(60), [(50, 1), (10, 1)])
    test(caixa_eletronico(70), [(50, 1), (10, 2)])
    test(caixa_eletronico(35), [(25, 1), (10, 1)])
    test(caixa_eletronico(135), [(100, 1), (25, 1), (10, 1)])
    test(caixa_eletronico(160), [(100, 1), (50, 1), (10, 1)])
    test(caixa_eletronico(165), [(100, 1), (50, 1), (10, 1), (5, 1)])
    test(caixa_eletronico(65), [(50, 1), (10, 1), (5, 1)])
    test(caixa_eletronico(115), [(100, 1), (10, 1), (5, 1)])
    test(caixa_eletronico(5), [(5, 1)])
    test(caixa_eletronico(6), [(5, 1), (1, 1)])
    test(caixa_eletronico(191), [(100, 1), (50, 1), (25, 1), (10, 1), (5, 1), (1, 1)])
    test(caixa_eletronico(0), [])
    test(caixa_eletronico(600), [(100, 6)])
    test(caixa_eletronico(601), [])
    test(caixa_eletronico(599), [(100, 5), (50, 1), (25, 1), (10, 2), (1, 4)])


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
