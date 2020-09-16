import sys

class EstadoQ():
    def __init__(self):
        pass

class Afn():
    def __init__(self, listaDefinicao, stInicial, stAceita):
        self.numEstados = listaDefinicao[0]
        self.numSimbolos = listaDefinicao[1]
        self.numTransi = listaDefinicao[2]

        self.simbolos = listaDefinicao[3:]
        self.stInicial = stInicial
        self.stAceita = stAceita
        self.stAtual = self.stInicial

def convertToInt(text):
    try:
        text = text.replace("\n","").strip() #retirando a quebra de linha e espaço no fim
        return int(text)
    except ValueError as ex:
        print(f'ERRO: {type(ex).__name__}: Não foi possível converter {text} para um número\nExecução terminada')

def lerDefAutomato(line, arq):
    line = line.replace("\t"," ").replace("\n","")
    print(arq.readline())

    #remove elementos vazios da lista
    #caso tivesse mais que um espaço entre os chars que interessamm
    line = filter(None,line.split(" "))
    line = list(map(convertToInt,line))
    numTransi = line[2]

    Afn(listaDefinicao=line,stInicial=None,stAceita=None)
def main():
    nomeEntrada = sys.argv[2]
    nomeSaida = sys.argv[4]

    with open(nomeEntrada) as arqEntrada:
        numAutomatos = convertToInt(arqEntrada.readline())        
        lerDefAutomato(arqEntrada.readline(),arqEntrada)
        print(arqEntrada.readline())
        
if __name__ == "__main__":
    main()