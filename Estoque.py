estoque = []
pesquisa = 0


def travarMenu():
    input("Pressione <ENTER> para continuar...")

def adicao(): 
    global iD
    global estoque

    quantAdicao()

    print("--------------------------- ADICIONAR PRODUTOS ------------------------------")
    novoEstoque = input("Qual produto será adicionado? ") #Adiciona o nome do produto
   

    print("--------------------------- ADICIONAR QUANTIDADE ------------------------------")
    novaquat = int(input("Quantos ítens são desejados?")) #Adiciona a quantidade do produto


    print("--------------------------- ADICIONAR ID ------------------------------")
    novoID = int(input("Adicione seu ID:"))#Adicionar ID

    print("--------------------------- LOCAL ------------------------------")
    novoLoc = input("Qual local o produto estara?") #Adiciona o local que o produto estara

    estoque.append([novoEstoque, novaquat, novoID, novoLoc])

    travarMenu()

def quantAdicao():
    i = 0
    while i < 1:
            i = int(input("Qual a quantidade de produtos seram adicionados? "))
       

while True:
    print("\n--------------------------- ESTOQUE DA LOJA ---------------------------")
    print("\n1- Mostrar status gerais do estoque | 2- Adicionar produto | 3- Mostrar informações isoladas | 4- Procurar produto por ID | 5- Mudar a quantidade dos produtos ou Excluir produto | 6- Sair\n")
    opcao = input("Escolha a opção que dejasa fazer:" )

    if (opcao == "1"):
        if (len(estoque))== 0:
                print("ERRO ⚠️⚠️⚠️")
                print("Não há produtos !!!")
                i = input("Dejesa adicionar um produtos? (s/n)")
                if i == "s":
                    adicao()
        else:
            print(estoque)
            travarMenu()

    elif (opcao == "2"):
        adicao()

    elif(opcao == "3"):
        print(" 1- Nome do produtos | 2- Quantidade dos produtos| 3- ID dos produtos | 4- Local do produto")
        opcaoIso = input("Escolha a opção que dejesa utilizar:")
        if (opcaoIso == "1"):
            if (len(estoque))== 0:
                print("ERRO ⚠️⚠️⚠️")
                print("Não há produtos !!!")
                i = input("Dejesa adicionar um produtos? (s/n)")
                if i == "s":
                    adicao()
            else:
                print(estoque[0])
                travarMenu()

        elif(opcao == "2"):
            if (len(estoque))== 0:
                print("ERRO ⚠️⚠️⚠️")
                print("Não há produtos !!!")
                i = input("Dejesa adicionar um produtos? (s/n)")
                if i == "s":
                    adicao()
            else:
                print(f"{estoque[0]}{estoque[1]}")
                travarMenu()

        elif(opcao == "3"):
            if (len(estoque))== 0:
                print("ERRO ⚠️⚠️⚠️")
                print("Não há produtos !!!")
                i = input("Dejesa adicionar um produtos? (s/n)")
                if i == "s":
                   adicao()
                else:
                    print(f"{estoque[0]}{estoque[2]}")
                    travarMenu()

        elif(opcao == "4"):
            if (len(estoque))== 0:
                print("ERRO ⚠️⚠️⚠️")
                print("Não há produtos !!!")
                i = input("Dejesa adicionar um produtos? (s/n)")
                if i == "s":
                   adicao()
            else:
                print(f"{estoque[0]}{estoque[3]}")
                travarMenu()
    
    elif (opcao == "4"):
        if (estoque)== 0:
                print("ERRO ⚠️⚠️⚠️")
                print("Não há produtos !!!")
                i = input("Dejesa adicionar um produtos? (s/n)")
                if i == "s":
                    adicao()
        else:
            a = int(input("Qual ID deseja saber?"))
            for itens in estoque:
                if itens[0] == a:
                    print(f"Nome: {itens[0]}, Quantidade: {itens[1]}, ID {itens[2]}, Local: {itens[3]}")

                    escolha = input("Deseja mudar a quantidade do item (s/n)?")
                    if escolha == "s":
                        novoValor = int(input("Qual será a nova quantidade? "))
                        itens[1] = novoValor
                    travarMenu()

    elif (opcao == "5"):
        if (len(estoque))== 0:
                print("ERRO ⚠️⚠️⚠️")
                print("Não há produtos !!!")
                i = input("Dejesa adicionar um produtos? (s/n)")
                if i == "s":
                    adicao()
        else:            
            a = int(input("Digite o ID do produto que deseja ser modificado a quantidade ou ser excluido :"))
            for itens in estoque:
                if itens[2] == a:
                    print(f"Nome: {itens[0]}, Quantidade: {itens[1]}, ID {itens[2]}")
                    escolha = input("1-modificar quantidade | 2- Excluir | 3- Sair")
                    if escolha == "1":
                        novoValor = int(input("Qual será a nova quantidade? "))
                        itens[1] = novoValor
                        print("Seu produto foi alterado a quantidade!")
                        travarMenu()
                    elif escolha == "2":
                        estoque.pop(itens)
                        print("Seu produto foi excluido!")
                        travarMenu()
                    elif escolha == "3":
                        break
            
    elif(opcao == "8"):
        print("Obrigado pela preferencia")
        print("Volte sempre !")
        break

    else:
        print("Essa opção não existe !!!")
        print("Digite novamente")
        travarMenu()