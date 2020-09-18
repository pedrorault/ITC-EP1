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

def compararTesteTransicao(stNode,entradaTeste,transicaoList):
    houveTransicao = False
    if stNode:
        transicoesPossiveis = transicoesDoStateX(stNode.state, transicaoList) #dado um estado X
        for t in transicoesPossiveis: #possivel juntar esse for com if, em um filter, pras transicoes vazias
            if existeTransicaoVazia(t):                               
                if len(entradaTeste) and existeTransicao(stNode.state,entradaTeste[0],t): 
                    filho = Node(t[2])
                    stNode.filhos.append(filho)
                    compararTesteTransicao(filho,entradaTeste[1:],transicaoList) # faz consumindo

                filho = Node(t[2])
                stNode.filhos.append(filho)

                compararTesteTransicao(filho,entradaTeste[0:],transicaoList) # faz não consumindo
            else:
                if len(entradaTeste) > 0:
                    if existeTransicao(stNode.state,entradaTeste[0],t):
                        filho = Node(t[2])
                        stNode.filhos.append(filho)

                        houveTransicao = True
                        compararTesteTransicao(filho,entradaTeste[1:],transicaoList)
                    elif not houveTransicao and stNode.state is not None: #elif nao houve transicao
                        filho = Node(None)
                        stNode.filhos.append(filho)
                        compararTesteTransicao(filho,entradaTeste[1:],transicaoList) 
                else:
                    break

def folhasTree(stNode, lista=None):
    #Ignorar as folhas com state/name = None (eq. a resposta de {})
    if stNode:
        if lista is None:
            lista = []            
        if len(stNode.filhos) == 0:
            if(stNode.state is not None):
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
                root = Node(stAtual)
                compararTesteTransicao(root,teste,transicaoList)
                total.append(checkFinalizadoAceito(folhasTree(root),aceitacaoList))

            w = " ".join(map(lambda x: str(x), total)) 
            with open(nomeSaida,"a") as s:
                s.write(f'{w}\n')
                print(f'{w}\n')

if __name__ == "__main__":
    main()