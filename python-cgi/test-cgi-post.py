#!/usr/bin/python3


# Esse codigo processa uma requisicao POST
# Cadastrando a variavel 'nome_cidade' no arquivo
# lista_cidades.txt, logo em seguida, temos um 
# Codigo HTTP para redirecionarmos o usuario para a pagina
# test-cgi-get que deve exibir a cidade cadastrada

import cgi, cgitb

form = cgi.FieldStorage() 

nome_usuario = form.getvalue("nome_usuario")
nome_cidade = form.getvalue("nome_cidade")

with open("./lista_cidades.txt","a") as arq:
    arq.write(f"{nome_cidade}\n")

redirectURL = f"/cgi/test-cgi-get.py?nome={nome_usuario}"

print("Content-Type: text/html")
# print(f"Location: {redirectURL}")
print("")#
print("<html>")
print(" <head>")
print(f"    <meta http-equiv=\"refresh\" content=\"2;url={redirectURL}\" />")
print("    <title>Voce sera redirecionado</title>")
print("  </head>" )
print("  <body>")
print(f"    Redirecting... <a href=\"{redirectURL}\">Clique aqui se voce nao for redirecionado</a>")
print("  </body>")
print("</html>")