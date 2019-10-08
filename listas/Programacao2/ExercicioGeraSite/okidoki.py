titulo= input("Inserir titutlo")
cabecalho=input("Inserir cabecalho")
titulopost=input("Insira o titulo da psotagem")
link = input("Insira o link")
link2 = input("Insira outro link")
nomelink = input("Insira o nome do  link")
nomelink2 = input("Insira o nome do  link2")
descricao = input("insira a descrição")
descricao2 = input("insira a descrição2")



arquivo = open('site.html','w')
arquivo.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>'''+titulo+'''</title></head><body><h1>'''+cabecalho+'''</h1><br><h2>'''+titulopost+'''</h2><a href=" '''+link+''' ">'''+nomelink+'''</a><p>'''+descricao+'''</p><a href=" '''+link2+''' ">'''+nomelink2+'''</a><p>'''+descricao2+'''</p></body></html> ''' )

arquivo.close()