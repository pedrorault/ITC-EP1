import sys

class Node:
    def __init__(self, state=None):
        self.state = state
        self.filhos = []

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
    if stNode and len(entradaTeste) > 0:
        transicoesPossiveis = transicoesDoStateX(stNode.state, transicaoList) #dado um estado X
        for t in transicoesPossiveis:
            if existeTransicao(stNode.state,entradaTeste[0],t):
                filho = Node(t[2])
                stNode.filhos.append(filho)
            if existeTransicaoVazia(t):
                filho = Node(t[2])
                compararTree(filho,entradaTeste,transicaoList)
        for f in stNode.filhos:
            compararTree(f,entradaTeste[1:],transicaoList)

def folhasTree(stNode, lista=None):
    if stNode:
        if lista is None:
            lista = []            
        if len(stNode.filhos) == 0:
            lista.append(stNode.state)
        else:
            for f in stNode.filhos:
                folhasTree(f,lista)
    return lista

def checkFinalizadoAceito(finalizadoEm,aceitacaoList):
    for stFinalizado in finalizadoEm:
        if stFinalizado in aceitacaoList:
            return 1
    return 0

def main():
    nomeEntrada = sys.argv[2]
    nomeSaida = sys.argv[4]

    with open(nomeEntrada) as f:
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

            for teste in testeList:
                root = Node(stInicial)
                compararTree(root,teste,transicaoList)
                total.append(checkFinalizadoAceito(folhasTree(root),aceitacaoList))

            w = " ".join(map(lambda x: str(x), total)) 
            with open(nomeSaida,"a") as s:
                s.write(f'{w}\n')

if __name__ == "__main__":
    main()