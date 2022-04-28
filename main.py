# lê o arquivo de definição do automato
f = open("automato.txt","r")

# lê o conteudo do arquivo e salva o alfabeto, estados, estado inicial e estado final
Alfabeto = f.readline()
alfabeto = Alfabeto.rstrip('\n').split(' ')
Estados = f.readline()
estados = Estados.rstrip('\n').split(' ')
estado_inicial = f.readline().rstrip('\n')
Estados_finais = f.readline()
estados_finais = Estados_finais.rstrip('\n').split(' ')

# aqui lê a matriz 
lines = []
for x in f:
    lines.append(x.rstrip('\n'))

f.close()
  
# classe Estado que salva o estado atual e o proximo estado
class Estado:
    def __init__(self,atual):
        self.atual = atual
        self.proximo_estado = {}
        return
    def add_line(self,x,y):
        self.proximo_estado.update({x:y})
      
# aqui cria um objeto pra cada estado e salva
classes_estados = []
for s in estados:
    s = Estado(s)
    classes_estados.append(s)
  
# aqui lê a linha do array e cria os proximos estados pra cada estado e cada alfabeto informado
for i in lines:
    i = i.rstrip('\n')
    x = i.split(' ')
    for s in classes_estados:
        if s.atual == x[0]:
            print(s.atual)
            s.add_line(x[1],x[2])

# aqui muda o estado de acordo com a entrada e retorna o proximo estado
def verifica_estado(estado,input):
    for i in classes_estados:
        if i.atual == estado.atual :
            tmp_state = i.proximo_estado.get(input)
            for s in classes_estados:
                if s.atual == tmp_state:
                    return s
                  
# cria uma variavel para depois verificar se todas as letras da entrada estao no alfabeto
string_in_alfabeto = True

# essa é a função que verifica letra a letra da entrada e retorna o ultimo estado
def Verifica_automato(string,estado):
    for z in string:
        if string in alfabeto:
            estado = verifica_estado(estado,z)
        else: string_in_alfabeto = False
    return estado
  
# aqui encontra o estado inicial entre os estados da classe Estado
def encontra_inicio(state_classes):
    for s in classes_estados:
        if s.atual == estado_inicial:
            return s

# aqui abre o arquivo das entradas e lê linha a linha
# tambem verifica o automato com a linha da entrada
with open("entradas.txt", "r") as e:
  saidas = []
  for string in e:
    estado = Verifica_automato(string, encontra_inicio(classes_estados))

    # aqui salva se ACEITA ou RECUSA a entrada num array
    if estado.atual in estados_finais and string_in_alfabeto is True:
      saidas.append('ACEITA')
    else:
      saidas.append('RECUSA')
e.close()

# aqui escreve o resultado das entradas no arquivo de saida
with open("saida.txt", "w") as p:
  for saida in saidas:
    p.write(saida + '\n')
p.close()

print('Automato executado. Verificar o arquivo saida.txt')
    
        
