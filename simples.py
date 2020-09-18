import sys
from anytree import Node, RenderTree

def transicoesDoStateX(state,transicaoList):
    lista = []
    for transicao in transicaoList:
        if state == transicao[0]:
            lista.append(transicao)
    return lista

def existeTransicao(stAtual,digito,transicao):
    if stAtual == transicao[0] and digito == transicao[1]:
        return True
    return False

def existeTransicaoVazia(transicao):
    if transicao[1] == 0:
        return True
    return False
    
def compararTree(stNode,entradaTeste,transicaoList):
    #TODO: transicao no vazio quando nao tem mais elementos pra ler
    #TODO: Estando em um estado e com coisa pra ler ainda, caso não haja transição,
    # criar um filho com o state/name = None
    if stNode and len(entradaTeste) > 0:
        transicoesPossiveis = transicoesDoStateX(stNode.name, transicaoList) #dado um estado X
        for t in transicoesPossiveis:
            if existeTransicao(stNode.name,entradaTeste[0],t):
                filho = Node(t[2],parent=stNode)
                print(RenderTree(stNode))
            if existeTransicaoVazia(t):
                filho = Node(t[2], parent=stNode)
                print(RenderTree(stNode))
                compararTree(filho,entradaTeste,transicaoList)
        for f in stNode.children:
            compararTree(f,entradaTeste[1:],transicaoList)

def folhasTree(stNode, lista=None):
    #Ignorar as folhas com state/name = None (eq. a resposta de {})
    #Referente ao TODO acima 
    if stNode:
        if lista is None:
            lista = []            
        if len(stNode.children) == 0:
            if(stNode.name is not None):
                lista.append(stNode.name)
        else:
            for f in stNode.children:
                folhasTree(f,lista)
    return lista

def checkFinalizadoAceito(finalizadoEm,aceitacaoList):
    for stFinalizado in finalizadoEm:
        if stFinalizado in aceitacaoList:
            return 1
    return 0

def main():
    # nomeEntrada = sys.argv[2]
    # nomeSaida = sys.argv[4]

    with open("./input3.txt") as f:
        numAutomatos = int(f.readline())
        for i in range(0,numAutomatos):      
            definicao = map(lambda x : int(x), f.readline().replace("\t"," ").split(" "))
            aceitacaoList = list(map(lambda x : int(x), f.readline().split(" ")))

            numEstados, numSimbolos, numTransi, stInicial, numAceitacao = definicao

            transicaoList = [f.readline().strip().split(" ") for i in range(0,numTransi)]
            transicaoList = [list(map(lambda x: int(x), c)) for c in transicaoList]

            numTestes = int(f.readline())
            testeList = []
            for i in range(0,numTestes):
                line = f.readline()
                if(line):
                    teste = list(map(lambda x : int(x), line.replace("\t"," ").split(" ")))
                testeList.append(teste)

            stAtual = stInicial
            total = []

            root = Node(stInicial)
            compararTree(root,testeList[6],transicaoList)
            print(RenderTree(root))
            total.append(checkFinalizadoAceito(folhasTree(root),aceitacaoList))

            # for teste in testeList:
            #     root = Node(stInicial)
            #     compararTree(root,teste,transicaoList)
            #     print(RenderTree(root))
            #     total.append(checkFinalizadoAceito(folhasTree(root),aceitacaoList))

            w = " ".join(map(lambda x: str(x), total)) 
            with open("tt","a") as s:
                s.write(f'{w}\n')

if __name__ == "__main__":
    main()