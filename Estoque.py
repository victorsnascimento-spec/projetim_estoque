nomeProd = []
quantProd = []
idProd = []
locProd = []
estoque = nomeProd, quantProd, idProd, locProd
def adicao(): 
    print("--------------------------- ADICIONAR PRODUTOS------------------------------")
    novoEstoque = input("Qual produto será adicionado? ")
    nomeProd.append(novoEstoque)



i = int(input("Qual a quantidade de produtos seram adicionados? "))
if(i <= 1):
    for k in range(1,i+1):
        adicao()
    
else:
    print("Digite novamente a quantidade de produtos")

print(estoque)

#lista.pop() = remove o ultimo item