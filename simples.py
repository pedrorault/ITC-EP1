import sys


class Node:
    def __init__(self, state=None):
        self.state = state
        self.filhos = []
        self.transicoesVazias = []


def transicoesDoStateX(state, transicaoList):
    lista = []
    for transicao in transicaoList:
        if state == transicao[0]:
            lista.append(transicao)
    return lista


def temTransicao(stAtual, digito, transicao):
    if stAtual == transicao[0] and digito == transicao[1]:
        return True
    return False


def existeTransicaoVazia(transicao):
    if transicao[1] == 0:
        return True
    return False


def compararTesteTransicao(stNode, entradaTeste, transicaoList):
    houveTransicao = False
    if stNode:
        transicoesPossiveis = transicoesDoStateX(
            stNode.state, transicaoList)  # dado um estado X
        for t in transicoesPossiveis:
            if existeTransicaoVazia(t):
                teste = entradaTeste
                if len(teste) and temTransicao(stNode.state, teste[0], t):
                    if t[2] not in stNode.transicoesVazias: 
                        filho = Node(t[2])
                        stNode.filhos.append(filho)
                        filho.transicoesVazias = stNode.transicoesVazias
                        filho.transicoesVazias.append(t[2])
                        compararTesteTransicao(
                            filho, entradaTeste[1:], transicaoList)
                        # faz consumindo
                    else: 
                        filho = Node(None)
                        stNode.transicoesVazias = []
                        stNode.filhos.append(filho)
                        compararTesteTransicao(
                            filho, entradaTeste[1:], transicaoList)

                if t[2] not in stNode.transicoesVazias: 
                    filho = Node(t[2])
                    stNode.filhos.append(filho)   
                    filho.transicoesVazias = stNode.transicoesVazias                                     
                    filho.transicoesVazias.append(t[2])
                    # faz não consumindo
                    compararTesteTransicao(filho, entradaTeste[0:], transicaoList)
                else: 
                    filho = Node(None)
                    stNode.filhos.append(filho)
                    stNode.transicoesVazias = []
                    compararTesteTransicao(
                        filho, entradaTeste[1:], transicaoList)
            else:
                if len(entradaTeste) > 0:
                    if temTransicao(stNode.state, entradaTeste[0], t):
                        stNode.transicoesVazias = []
                        filho = Node(t[2])
                        stNode.filhos.append(filho)

                        houveTransicao = True
                        compararTesteTransicao(
                            filho, entradaTeste[1:], transicaoList)
                    elif not houveTransicao and stNode.state is not None:
                        # elif nao houve transicao
                        filho = Node(None)
                        stNode.transicoesVazias = []
                        stNode.filhos.append(filho)
                        compararTesteTransicao(
                            filho, entradaTeste[1:], transicaoList)
                else:
                    break


def folhasTree(stNode, lista=None):
    # Ignorar as folhas com state/name = None (eq. a resposta de {})
    if stNode:
        if lista is None:
            lista = []
        if len(stNode.filhos) == 0:
            if(stNode.state is not None):
                lista.append(stNode.state)
        else:
            for f in stNode.filhos:
                folhasTree(f, lista)
    return lista


def checkFinalizadoAceito(finalizadoEm, aceitacaoList):
    for stFinalizado in finalizadoEm:
        if stFinalizado in aceitacaoList:
            return 1
    return 0


def main():
    nomeEntrada = sys.argv[2]
    nomeSaida = sys.argv[4]

    saida = ""
    with open(nomeEntrada) as f:
        numAutomatos = int(f.readline())
        for i in range(0, numAutomatos):
            definicao = map(lambda x: int(
                x), f.readline().replace("\t", " ").split(" "))
            aceitacaoList = list(
                map(lambda x: int(x), f.readline().split(" ")))

            numSt, numSymb, numTransi, stInicial, numAceitacao = definicao

            transicaoList = [f.readline().strip().split(" ")
                             for i in range(0, numTransi)]
            transicaoList = [list(map(lambda x: int(x), c))
                             for c in transicaoList]

            numTestes = int(f.readline())
            testeList = []
            for i in range(0, numTestes):
                line = f.readline()
                if(line):
                    testeStr = line.replace("\t", " ").split(" ")
                    teste = list(map(lambda x: int(x), testeStr))
                testeList.append(teste)

            stAtual = stInicial
            total = []

            for teste in testeList:
                root = Node(stAtual)
                compararTesteTransicao(root, teste, transicaoList)
                total.append(checkFinalizadoAceito(
                    folhasTree(root), aceitacaoList))

            w = " ".join(map(lambda x: str(x), total))
            saida += f'{w}\n'
        with open(nomeSaida, "w") as s:
            s.write(saida)


if __name__ == "__main__":
    main()
