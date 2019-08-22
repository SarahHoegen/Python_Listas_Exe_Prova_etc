import random

linhas = open('palavras.txt').read().splitlines()
linhaEscolhida = random.choice(linhas)

palavra = linhaEscolhida
embaralhada = "".join(random.sample(palavra, len(palavra)))
separacao = '\n'
plvEmb = print(embaralhada)
print(separacao)

tentativa = input('Você consegue acertar qual palavra esta escrita: ')


def tentativaAcerto(tentativa):
    tentativaRestante = 5
    while tentativa != linhaEscolhida:
        print('Você errou! Tente novamente.')
        tentativaRestante -= 1
        print('Você tem {} tentativas!'.format(tentativaRestante))
        tentativa = input('Consegue advinhar? ')
        if tentativaRestante == 0:
            print('Que pena, você não conseguiu acertar :c')
            break
    else:
            return print('Parabéns! Você acertou.')


tentativaAcerto(tentativa)