filmes={
    "Drama":["Dois Papas", "O Quarto de Jack", "Sempre a seu lado"],
    "Comédia":["Deadpool", "American Pie", "O Auto da Compadecida"],
    "Policial":["Dia de Treinamento", "Tropa de Elite", "Os Infiltrados"],
    "Guerra":["Até o Último Homem", "1917", "Rambo"]
}
pagina=open("index.html", "w")
pagina.write("""
<html lang="pt-BR">
<head>
    <title>Dicionário de Filmes</title>
</head>
<body>
""")
for i,x in filmes.items():
    pagina.write("<h2>%s</h2>" % i)
    for y in x:
        pagina.write("<p>%s</p>" % y)
pagina.write
pagina.close()