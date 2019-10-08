mantimentos = ["banana", "laranja", "melao"]

estoque = {
    "banana": 6,
    "melao": 0,
    "laranja": 32,
    "pera": 15
}

precos = {
    "banana": 4,
    "melao": 2,
    "laranja": 1.5,
    "pera": 3
}
def calcular_conta(lista_de_mantimentos):
    total = 0
    for item in lista_de_mantimentos:
        if estoque[item] > 0:
            total += precos[item]
            estoque[item] -= 1
            print(estoque[item]) #mostra o estoque restante
        else:
            pass
    return total

print(calcular_conta(mantimentos))