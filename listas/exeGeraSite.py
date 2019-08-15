titulo= input("Inserir titutlo")

cabecalho=input("Inserir cabecalho")

titulopost=input("Insira o titulo da psotagem")

link = input("Insira o link")

descricao = input("insira a descrição")



arquivo = open('site.html','w')
arquivo.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>'''+titulo+'''</title></head><body><h1>'''+cabecalho+'''</h1><br><h2>'''+titulopost+'''</h2><a href=" '''+link+''' ">'''+descricao+'''</a></body></html> ''' )

arquivo.close()