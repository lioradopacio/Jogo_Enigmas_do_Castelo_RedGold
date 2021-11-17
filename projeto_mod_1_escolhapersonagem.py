import projeto_mod_1_vamparypota
import projeto_mod_1_vampesley
import projeto_mod_1_vampione

import time
from termcolor import cprint

def escolha_personagem():
    abertura()

def abertura():

    cprint('███████╗███╗   ██╗██╗ ██████╗ ███╗   ███╗ █████╗ ███████╗    ██████╗  ██████╗', 'red')
    cprint('██╔════╝████╗  ██║██║██╔════╝ ████╗ ████║██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗', 'red')
    cprint('█████╗  ██╔██╗ ██║██║██║  ███╗██╔████╔██║███████║███████╗    ██║  ██║██║   ██║ ', 'red')
    cprint('██╔══╝  ██║╚██╗██║██║██║   ██║██║╚██╔╝██║██╔══██║╚════██║    ██║  ██║██║   ██║ ', 'red')
    cprint('███████╗██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║██║  ██║███████║    ██████╔╝╚██████╔╝  ', 'red')
    cprint('╚══════╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝  ', 'red')
    time.sleep(1)
    cprint(' ██████╗ █████╗ ███████╗████████╗███████╗██╗      ██████╗     ██████╗ ███████╗██████╗  ██████╗  ██████╗ ██╗     ██████╗ ', 'red')
    cprint(' ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██║     ██╔═══██╗    ██╔══██╗██╔════╝██╔══██╗██╔════╝ ██╔═══██╗██║     ██╔══██╗', 'red')
    cprint(' ██║     ███████║███████╗   ██║   █████╗  ██║     ██║   ██║    ██████╔╝█████╗  ██║  ██║██║  ███╗██║   ██║██║     ██║  ██║', 'red')
    cprint(' ██║     ██╔══██║╚════██║   ██║   ██╔══╝  ██║     ██║   ██║    ██╔══██╗██╔══╝  ██║  ██║██║   ██║██║   ██║██║     ██║  ██║', 'red')
    cprint(' ╚██████╗██║  ██║███████║   ██║   ███████╗███████╗╚██████╔╝    ██║  ██║███████╗██████╔╝╚██████╔╝╚██████╔╝███████╗██████╔╝', 'red')
    cprint('  ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚══════╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═════╝ ', 'red')
    time.sleep(1)
    print_boas_vindas()


def print_boas_vindas ():
    print('\nSeja muito bem-vindo(a).\n')
    time.sleep(1)
    print('Você recebeu o abraço da morte, tornando-se um vampiro.')
    time.sleep(1)
    print('Sua vida agora trafega entre a linha dos vivos e dos mortos, porém imortal.')
    time.sleep(1)
    print('Hoje você deixa de ser presa e se torna um predador.')
    time.sleep(1)
    print('\nAntes de descobrir como essa nova vida será, escolha quem melhor te representa:\n')
    time.sleep(1)
    cprint('-'* 80, 'red')
    print('\n\t1.VAMPARYPOTA: caolho, caótico, ex-bruxo, reclamão. ESPECIALIDADE: coragem')
    time.sleep(1)
    print('\n\t2.VAMPESLEY: comilão, olheiras profundas, trouxa (não bruxo) sempre entediado. ESPECIALIDADE: sagacidade')
    time.sleep(1)
    print('\n\t3.VAMPIONE: exótica, ex-bruxa, curiosa, pálida e apática. ESPECIALIDADE: conhecimento\n')
    cprint('-'* 80, 'red')
    personagens ()


def personagens ():
    personagem = int(input('\nDigite o número corresponder ao personagem que deseja:'))

    if (personagem == 1):
        print('\nHum...')
        time.sleep(0.5)
        print('Você é dos times dos corajosos, então? Vamos lá!')
        projeto_mod_1_vamparypota.jogar1()

    elif (personagem == 2):
        print('\nBom saber...')
        time.sleep(0.5)
        print('Já diziam por aí, malandro é malandro e mané é mané! Vamos nessa!')
        projeto_mod_1_vampesley.jogar1()
    elif (personagem == 3):
        print('\nDas profundezas bibliotecas então...')
        time.sleep(0.5)
        print('Uma mente limitada é aquela que acredita que o conhecimento não é necessário. Nerd assumido(a), vamos ganhar esse jogo, logo!')
        projeto_mod_1_vampione.jogar1()
    else:
        print('Opção não disponível!\n')
        lista_personagem = [1, 2, 3]
        while personagem != lista_personagem:
            print(personagem)


if(__name__ == '__main__'):
    escolha_personagem()
    