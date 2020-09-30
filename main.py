import sys


class Node():
    def __init__(self, estadoObj):
        self.estadoObj = estadoObj
        self.filhos = []


class EstadoQ():
    def __init__(self, state):
        self.state = state  # numero do estado
        self.transicoes = []  # tuplas (char,estado)


class Automato():
    def __init__(self, numSt, numSymb, numTransicao, stInicial, aceitacaoList):
        self.numEstados = numSt
        self.numSimbolos = numSymb
        self.numTransicao = numTransicao
        self.numAceitacao = len(aceitacaoList)

        self.stInicial = stInicial
        self.aceitacaoList = aceitacaoList


def folhasTree(stNode, lista=None):
    if stNode:
        if lista is None:
            lista = []
        if len(stNode.filhos) == 0:
            if(stNode.estadoObj is not None):
                lista.append(stNode.estadoObj)
        else:
            for f in stNode.filhos:
                folhasTree(f, lista)
    return lista


def checkFinalizadoAceito(finalizadoEm, aceitacaoList):
    for stFinalizado in finalizadoEm:
        if stFinalizado.state in aceitacaoList:
            return 1
    return 0


def compararTesteTransicao(stNode, entradaTeste):
    houveTransicao = False
    if stNode and stNode.estadoObj is not None:
        transicoes = stNode.estadoObj.transicoes

        for valor, estado in transicoes:
            if valor == 0:
                digito = entradaTeste[0] if type(entradaTeste) is list and len(entradaTeste) else entradaTeste
                if len(entradaTeste) and digito == stNode.estadoObj.state:
                    filho = Node(estado)
                    stNode.filhos.append(filho)
                    compararTesteTransicao(filho, entradaTeste[1:])
                filho = Node(estado)
                stNode.filhos.append(filho)
                compararTesteTransicao(filho, entradaTeste[0:])
            else:
                if len(entradaTeste):
                    if entradaTeste[0] == valor:
                        filho = Node(estado)
                        stNode.filhos.append(filho)
                        houveTransicao = True
                        compararTesteTransicao(filho, entradaTeste[1:])
                    elif not houveTransicao and estado.state is not None:
                        filho = Node(None)
                        stNode.filhos.append(filho)
                        compararTesteTransicao(filho, entradaTeste[1:])
                else:
                    break


def lerArquivo(nomeEntrada):
    linhasArquivo = None
    with open(nomeEntrada) as f:
        linhasArquivo = map(lambda x: x.strip().split(" "), f.readlines())
        linhasArquivo = [list(map(lambda x: int(x), item))
                         for item in linhasArquivo]
    return linhasArquivo


def lerAutomatos(linhasArquivo):
    # Transformei tudo em uma lista pra facilitar na conversao
    numAutomatos = linhasArquivo.pop(0)[0]
    automatos = {}
    for auto in range(0, numAutomatos):
        tempDefinicao = linhasArquivo.pop(0)
        numSt = tempDefinicao[0]
        numSymb = tempDefinicao[1]
        numTrans = tempDefinicao[2]
        stInicial = tempDefinicao[3]
        # numAceitacao = tempDefinicao[4] #Nunca utilizado

        acptList = linhasArquivo.pop(0)

        transicoes = [linhasArquivo.pop(0) for t in range(0, numTrans)]
        testes = [linhasArquivo.pop(0)
                  for t in range(0, linhasArquivo.pop(0)[0])]

        stList = [EstadoQ(n) for n in range(0, numSt+1)]
        for estado in stList:
            for t in transicoes:
                if t[0] == estado.state:
                    estado.transicoes.append((t[1], stList[t[2]]))

        automatoTmp = \
            Automato(numSt, numSymb, numTrans, stList[stInicial], acptList)
        automatos[automatoTmp] = testes
    return automatos


def escreverArquivo(nomeSaida, saida):
    with open(nomeSaida, "w") as f:
        f.write(saida)


def testarAutomatos(automatosDict):
    resultadoTestes = []
    saida = ""
    for aut in automatosDict.keys():
        for teste in automatosDict[aut]:
            root = Node(aut.stInicial)
            compararTesteTransicao(root, teste)
            resultadoTestes.append(checkFinalizadoAceito(
                folhasTree(root), aut.aceitacaoList))
        w = " ".join(map(lambda x: str(x), resultadoTestes))
        saida += w+"\n"
        resultadoTestes = []
    return saida


def main():
    nomeEntrada = sys.argv[2]
    nomeSaida = sys.argv[4]

    linhasArquivo = lerArquivo(nomeEntrada)
    automatos = lerAutomatos(linhasArquivo)
    saida = testarAutomatos(automatos)
    escreverArquivo(nomeSaida, saida)


if __name__ == "__main__":
    main()
