titulo= input("Inserir titutlo")

cabecalho=input("Inserir cabecalho")

titulopost=input("Insira o titulo da psotagem")

link = input("Insira o link")

nomelink = input("Insira o nome do  link")

descricao = input("insira a descrição")



arquivo = open('site.html','w')
arquivo.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>'''+titulo+'''</title></head><body><h1>'''+cabecalho+'''</h1><br><h2>'''+titulopost+'''</h2><a href=" '''+link+''' ">'''+nomelink+'''</a><p>'''+descricao+'''</p><a href=" '''+link2+''' ">'''+nomelink2+'''</a><p>'''+descricao2+'''</p></body></html> ''' )

arquivo.close()
