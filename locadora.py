# LOCADORA DE FILMES

sair = False
listaFilmes = ["O Poderoso Chefão", "Forrest Gump", "A Origem", "O Senhor dos Anéis: A Sociedade do Anel", "O Cavaleiro das Trevas", "Vingadores: Ultimato", "Matrix", "A Vida é Bela", "O Rei Leão", "Pulp Fiction", "Gladiador", "Star Wars: O Império Contra-Ataca", "Clube da Luta", "Cidadão Kane", "O Exorcista", "Os Infiltrados", "A Rede Social", "O Grande Lebowski", "A Lista de Schindler", "O Pianista"]


listaFilmesDiponiveis = ["O Poderoso Chefão", "Forrest Gump", "Vingadores: Ultimato", "O Senhor dos Anéis: A Sociedade do Anel", "Matrix", "A Origem", "O Cavaleiro das Trevas", "A Vida é Bela", "O Rei Leão", "Pulp Fiction"]

while sair != True:
  print("\n(1) Listar os Filmes")
  print("(2) Devolver um Filme")
  print("(3) Alugar um Filme")
  print("(4) Sair")
  opcao = int(input("Escolha uma opção: "))

  while opcao < 1 or opcao > 4:
    opcao = int(input("Digite uma opção válida: "))

  if opcao == 1:
    for i in range(len(listaFilmesDiponiveis)):
      print(f"{listaFilmesDiponiveis[i]}, ", end = "")

      if (i + 1) % 3 == 0:
        print()
    print()
  
  elif opcao == 2:

    nome = input("Digite o nome do filme a ser devolvido: ")

    if nome in listaFilmes and nome not in listaFilmesDiponiveis:
      print("Filme devovido com sucesso!")
      listaFilmesDiponiveis.append(nome)
    elif nome in listaFilmes and nome in listaFilmesDiponiveis:
      print("Já estamos com esse filme na loja, esse filme não é nosso!")
    else:
      print("Esse filme não é nosso!")
    
  elif opcao == 3:
    nome  = input("Digite o nome do filme a ser alugado: ")
    if nome in listaFilmesDiponiveis:
      print("Filme alugado com sucesso!")
      listaFilmesDiponiveis.remove(nome)
    else:
      if nome in listaFilmes:
        print("O filme desejado não está disponível!")
      else:
        print("Não temos esse filme!")
  else:
    sair = True
    print("Saindo...")
