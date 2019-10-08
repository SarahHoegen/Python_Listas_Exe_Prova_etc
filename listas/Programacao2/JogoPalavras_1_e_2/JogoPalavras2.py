import random

dificuldade = int(input('Você deseja qual dificuldade? Fácil(1), Médio(2), ou Difícil(3)? Selecione o numero correspondente:'))

def palavraembaralha(linhaEscolhida):
    palavra = linhaEscolhida
    embaralhada = "".join(random.sample(palavra, len(palavra)))
    print(str(embaralhada))
    print('\n')

while dificuldade < 1 or dificuldade>3:
    print('Valor inválido. Digite, 1, 2 ou 3.')
    dificuldade = int(input('Você deseja qual dificuldade? Fácil(1), Médio(2), ou Difícil(3)? Selecione o numero correspondente:' ))

if dificuldade == 1:
    linhas = open('palavras.txt').read().splitlines()
    linhaEscolhida = random.choice(linhas)
    palavraembaralha(linhaEscolhida)

elif dificuldade == 2:
    linhas = open('palavras2.txt').read().splitlines()
    linhaEscolhida = random.choice(linhas)
    palavraembaralha(linhaEscolhida)

else:
    linhas = open('palavras3.txt').read().splitlines()
    linhaEscolhida = random.choice(linhas)
    palavraembaralha(linhaEscolhida)

linhas2 = open('respostas.txt').read().splitlines()
tentativa = input('Você consegue acertar qual palavra esta escrita: ')


def tentativaAcerto(tentativa):
    tentativaRestante = 5
    while tentativa != linhaEscolhida:
        mensagemErrado = random.choice(linhas2)
        print(str(mensagemErrado))
        tentativaRestante -= 1
        print('Você tem mais {} tentativas!'.format(tentativaRestante))
        tentativa = input('Consegue advinhar? ')
        if tentativaRestante == 0:
            print('Que pena, você não conseguiu acertar :c')
            break
    else:
        return print('Parabéns! Você acertou.')


tentativaAcerto(tentativa)