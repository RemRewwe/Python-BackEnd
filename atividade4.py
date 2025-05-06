with open('dados.txt', 'w') as ovolada:
    ovolada.write("Nome: Ovo\nIdade: 1\nProfissão: componente de omelete\n")
    ovolada.write("Nome: Ovonilson\nIdade: 1.5\nProfissão: componente de pão com ovo\n")
    ovolada.write("Nome: galinha\nIdade: 5\nProfissão: mão de ovo e ovonilson\n")
    ovolada.write("Nome: galão\nIdade: 5\nProfissão: pai de ovo e ovonilson")

with open('dados.txt', 'r') as ovolada:
    conteudo = ovolada.read()
    print(conteudo)

