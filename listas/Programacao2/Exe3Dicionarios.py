frase = "eu amo meu gato"

letras = {
    "eu" : "i" ,
    "amo" : "love" ,
    "meu" : "my" ,
    "gato" :"cat"
}

def traduz_para_inglês(frase):
    frase = frase.split(" ")
    traduzido = ""
    for palavra in frase:
        if palavra in letras:
            traduzido += letras[palavra]+" "
        else:
            traduzido += " "
    return traduzido


print(traduz_para_inglês(frase))



