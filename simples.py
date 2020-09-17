import sys

def existeTransicao(stAtual,digito,stDestino):
    if stDestino:
        if int(stDestino[2]) == 0 or stDestino.startswith(f'{stAtual} {digito}'):
            return True
    return False

def compararVTesteEstado(stAtual,teste,listaTransicao):
    finaliza = [stAtual]
    #FIXME: Nao consumir digito quando a cadeia lida eh vazia

    for digito in teste:
        stTempList = finaliza[:]
        finaliza = []
        stDestinoList = []
        for stTemp in stTempList: 
            for transicao in listaTransicao:
                if int(transicao[0]) == stTemp and existeTransicao(stTemp,digito,transicao):
                    stDestino = transicao[4]                    
                    stDestinoList.append(stDestino)
        stDestinoList = filter(lambda x: x not in finaliza, stDestinoList)
        finaliza += map(lambda x : int(x), stDestinoList)
    return finaliza

def checkFinalizadoAceito(finalizadoEm,aceitacaoList):
    for stFinalizado in finalizadoEm:
        if int(stFinalizado) in aceitacaoList:
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

            transiList = [f.readline().strip() for i in range(0,numTransi)]

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
                stFinalizados = compararVTesteEstado(stAtual,teste,transiList)
                foiAceito = checkFinalizadoAceito(stFinalizados,aceitacaoList)
                total.append(foiAceito)
            print("resultado: "," ".join(map(lambda x: str(x), total)))
            #TODO: Saida como arquivo           

if __name__ == "__main__":
    main()
