'''
Arquivo de funções utilizadas
2025.08.09
Luiz Otávio de Souza Freo
'''

# OBJETIVO: Criar um arquivo de funções que serão utilizadas em meus Projetos

# CONSTANTES
TAM = int(70)   # Tamnho da Tela
MAR = int(2)    # Margem da mensagem na tela
CAR = '-'       # Caractere utilizado para desenhar a linha

# FUNÇÕES
# Função para limpar a tela 
def limpaTela():
    print('\n'*TAM)     # Mostra na tela TAM(50) linhas em branco (\n)

# Função para desenhar uma linha
def mostraLine():
    print(f'{CAR}'*TAM)      # Mostra na tela TAM(50) caracteres '#'

# Função para mostrar uma Msg Centralizada
def msgCenter(msg):
    print(f'{CAR} {msg:^{TAM-MAR-MAR}} {CAR}') # Mostra na tela o valor do parametro msg Centralizado entre TAM(50)-MAR(2)-MAR(2)

# Função para mostrar uma Msg a Esquerda
def msgLeft(msg):
    print(f'{CAR} {msg:<{TAM-MAR-MAR}} {CAR}') # Mostra na tela o valor do parametro msg a esquerda entre TAM(50)-MAR(2)-MAR(2)

# Função para mostrar Msgs Centralizadas
def mostraMsgs(MSGS):
    mostraLine()            # Chama a função que mostra a linha
    for msg in MSGS:        # Itera sobre a lista MSGS
        msgCenter(msg)      # Chama a função que mostra a mensagem centralizada 
    mostraLine()            # Chama a função que mostra a linha

# Função para mostrar Msgs a Esquerda
def leftMsgs(MSGS):
    for msg in MSGS:
        msgLeft(msg)
