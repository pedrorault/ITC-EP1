import sys

class Node:
    def __init__(self, state=None):
        self.state = state
        self.filhos = []

def cadeiaVazia(stAtual,transicao):
    #Pra uma transição só. Retorna os estados em que está
    #Imaginando que tenha um estado com transicao vazia, ele está antes e após da transicao

    #TODO: Remover porque nem ta sendo usado
    estado = stAtual
    l = [estado] 
    while estado == transicao[0] and transicao[1] == 0:
        estado = transicao[2]
        l.append(estado)
    return l

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

def folhasTree(stNode):
    if stNode:
        if len(stNode.filhos) == 0:
            print(stNode, stNode.state)
        else:
            for f in stNode.filhos:
                folhasTree(f)

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

            # TESTE
            # root = Node(stInicial)
            # compararTree(root,testeList[2],transicaoList)
            # folhasTree(root)

            # for teste in testeList:
            #     root = Node(stInicial)
            #     compararTree(root,testeList[2],transicaoList)
            #     folhasTree(root)

            # print("resultado: "," ".join(map(lambda x: str(x), total))) #TODO: pra usar o resultado do checkFinalizado Aceito
            #TODO: resultado das folhas como uma lista, pra jogar no checkFinalizadoAceito
            #TODO: Saida como arquivo           

if __name__ == "__main__":
    main()