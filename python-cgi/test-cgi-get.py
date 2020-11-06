#!/usr/bin/python3

## Nesse caso do cgi para o metodo GET, o servidor web
## no caso o apache, executa o script antes de responder
## a requisicao e envia o seu resultado como response para
## o cliente

import cgi, cgitb

form = cgi.FieldStorage() 

#Obtendo Variaveis da URL - Metodo GET
nome = form.getvalue('nome')
idade  = form.getvalue('idade')


print("Content-type: text/html")
print("")
print("<html>")
print("<head>")
print("<title>Teste CGI - GET</title>")
print("</head>")
print("<body>")
print(f"<h2>Ola {nome}, Bem vindo</h2>")

# Metodo para exemplo de um codigo cgi post

print("<h3>Cadastrar Nova Cidade</h3>")
print("<form action=\"/cgi/test-cgi-post.py\" method=\"POST\">")
print("Nome da Cidade: <input type=\"text\" name=\"nome_cidade\"/>")
print(f"<input type=\"hidden\" name=\"nome_usuario\" value=\"{nome}\"/>")
print("<input type=\"submit\" value=\"OK\"/>")
print("</form>")
print("<h3>Lista de Cidades</h3>")
print("<ol>")

# Lendo arquivo lista_cidades.txt e devolvendo cada linha como
# uma lista

with open("./lista_cidades.txt") as arq:
    for line in arq:
        print(f"<li>{line}</li>")
print("</ol>")

print("</body>")
print("</html>")