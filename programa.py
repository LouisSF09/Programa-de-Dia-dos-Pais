'''
Programa de Dia dos Pais 2025
2025.08.10
Luiz Otávio de Souza Freo
'''

# BIBLIOTECAS --> Declaração das bibliotecas
from time import sleep
from functions import limpaTela, msgCenter, mostraMsgs, leftMsgs

# CONSTANTES --> Declaração de constantes
TEM = int(5)

# VARIÁVEIS --> Declaração das variáveis
msgsCab = ["Sistema de", "Dia dos Pais", "2025"]
tecla = ""

# Função principal do programa
def start_program():
    limpaTela()
    mostraMsgs(msgsCab)
    mostraMsgs(["INTRODUÇÃO"])

    sleep(TEM)
    mostraMsgs(["Este é um sistema simples", "feito para comemorar o", "Dia dos Pais", "(pressione ENTER para avançar)"])
    tecla = input()
    mostraMsgs([" ", "Mas apesar de simples", "fiz com muito carinho", "então espero que goste."])
    tecla = input()

    limpaTela()
    mostraMsgs(msgsCab)
    mostraMsgs(["CARTA"])

    sleep(TEM)
    leftMsgs(["Pai,"])
    tecla = input()
    leftMsgs(["     Você deve saber que este é um dia especial, mas mesmo assim", "eu quero lembrá-lo disso. Hoje não é o Dia dos Pais, mas", "sim o dia dos heróis."])
    tecla = input()
    leftMsgs(["     O dia daqueles que sempre estavam lá para ajudar quando", "precisávamos, daqueles que nos deram amor, carinho e auxílio."])
    tecla = input()
    leftMsgs(["     O dia daqueles que nos ajudaram nas tarefas sa escola,", "nos incentivaram a ler, e que brincaram conosco."])
    tecla = input()
    leftMsgs(["     E você, Pai, pode dizer com toda a certeza que é um herói."])
    tecla = input()
    leftMsgs(["     Por isso, e muito mais, no dia de hoje eu quero te agradecer.", "Que você continue sendo esse herói em nossas vidas, e que Deus", "te abençoe."])
    tecla = input()
    leftMsgs(["Luiz Otávio"])
    tecla = input()

    limpaTela()
    mostraMsgs(msgsCab)
    mostraMsgs(["P.S."])
    sleep(TEM)

    mostraMsgs(["Você deve ter sentido falta", "de algo muito importante não é?"])
    tecla = input()

    mostraMsgs(["Sim, faltou o 'Feliz Dia dos Pais'", "Mas não se preocupe,", "eu não esqueci, aqui estão eles:"])
    tecla = input()

    for i in range(1, 1001):
        print(f'{i}. Feliz Dia dos Pais!!!')

    mostraMsgs(["", "", ""])
    msgCenter("-- FIM --")


# Inicia o programa
start_program()
