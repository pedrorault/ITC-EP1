import sys

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

            #do tests and write to file
            stAtual = stInicial
            resultado =  []
            # 121
            for digito in testeList[0]:
                substr = f'{stAtual} {digito}'
                for transi in transiList:
                    if transi.startswith(substr):
                        stAtual = transi[-1]
                        break
         

                        
            #if stAtual in aceitacaoList:   return 1 else 0

if __name__ == "__main__":
    # main()
    x = "0 1"
    y = ["1 1 3", "0 0 2", "0 1 3"]
    if y[2].startswith(x):
        print("yes")