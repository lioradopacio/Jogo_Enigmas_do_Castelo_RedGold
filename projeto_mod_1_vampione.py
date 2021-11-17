import projeto_mod_1_escolhapersonagem

import time
from termcolor import cprint
import pyfiglet


def jogar1():
    explicacao_missao_vampione()

def explicacao_sala_jantar():
    print('\nNa sala de jantar do castelo, você encontra um prato com um papel dobrado embaixo...')
    time.sleep(1)
    print('quando ergue o prato, lê os seguintes dizeres:\n')
    cprint('-'* 80, 'red')
    time.sleep(1)
    print('TODO MUNDO LEVA, TODO MUNDO TEM, PORQUE A TODOS LHES DÃO UM QUANDO AO MUNDO VEM.')
    time.sleep(1)
    cprint('-'* 80, 'red')
    print('\n***Dica*** _ _ _ _\n')
    time.sleep(1)
    enimga_sala_jantar()


def explicacao_biblioteca_escrito_sangue():
    print('\nAo entrar no biblioteca, viu uma parede escrita com sangue, os seguintes dizeres:\n')
    cprint('-'* 80, 'red')
    time.sleep(1)
    print('ESSA COISA TE DEVORAPÁSSAROS, MONSTROS, ARVORES E FLORES')
    print('MASTIGA O FERRO E MORDE O AÇO, REDUZ EM PÓ AS ROCHAS MAIS RESISTENTES')
    print('MATA O REI E DESTRÓI AS CIDADESE DESTRÓI AS MONTANHAS MAIS ALTAS.\n')
    time.sleep(1)
    cprint('-'* 80, 'red')
    print('Quem sou eu?')
    time.sleep(1)
    print('\n***Dica*** _ _ _ _ _ ')
    enimga_palavra_biblioteca()


def explicacao_encontro_gemeas():
    print('\nAndando pelo castelo, você encontra duas menininhas gemeas pálidas, de vestido branco. ')
    time.sleep(1)
    print('Boatos que elas sabem as passagens secretas do castelo onde estão as recompensas...\n')
    cprint('-'* 80, 'red')
    time.sleep(1)
    print('1. perguntar se há algum outro enigma para decifrar.')
    time.sleep(1)
    print('2. puxar conversa com elas')
    cprint('-'* 80, 'red')
    interacao_menininha()


def explicacao_missao_vampione():
    print('\nPoucos são os que notariam o estranho movimento em um castelo abandonado, porém de requinte, em uma área reservada da cidade.')
    time.sleep(1)
    print('Para olhos destreinados, passam despercebidas as figuras pálidas que nele entram movidas a curiosidade...')
    time.sleep(1)
    print('Sedentas por um desaviado e às vezes, até para explorar o local.\n')
    time.sleep(1)

    print('SUA MISSÃO É:')
    time.sleep(1)
    print('decifrar incógnitas e responder o enigma final para receber: sangue e ouro.\n')
    time.sleep(1)
    print('Você está na porta do castelo RedGold, {}, mas parece que a porta tem um enigme para abri-la.'.format(nome_personagem))
    time.sleep(1)
    print('Digite o número correspondente a ação que deseja:\n')
    cprint('-'* 80, 'red')
    time.sleep(1)
    print('1. ir atrás do barulho que ouviu')
    time.sleep(1)
    print('2. decifrar enigma!')
    cprint('-'* 80, 'red')
    resposta_abrir_porta_nao_entrou()

nome_personagem = 'Vampione'


def jogar_novamente():
    jogar_novamente = input('\nDeseja jogar novamente? [S/N]:')
    if (jogar_novamente.upper().strip() == 'S'):
        projeto_mod_1_escolhapersonagem.escolha_personagem()
    elif(jogar_novamente.upper().strip() == 'N'):
        print('Até a próxima!')



def resp_desistiu_entrar():
    condicao = True
    while condicao:
        resp_desistiu = int(input('Digite sua escolha [1 ou 2]:'))
        if (resp_desistiu == 1) or (resp_desistiu == 2):
                print('\nAo se aproximar, ele oferece um copo de água, pois fazia um calor danado...')
                time.sleep(2)
                print('Porém a água tinha extrato de alho, ao tomar um gole da água, imediatamente, você começou a passar mal e morreu.\n')
                time.sleep(1)
                print('Ele nunca se conformou de ter um amor não correspondido. Não satisfeito, ele tomou o restante da água e morreu ao lado de sua amada.\n')
                time.sleep(1)
                cprint('GAME OVER! MORREU TORRADO.', 'yellow', 'on_red', attrs=['bold'])
                time.sleep(1)
                jogar_novamente()
                condicao = False
        else:
            print('Resposta inválida')

def explicacao_resp_enigma_porta():
    cprint('\n----------------*ENIGMA DA PORTA*----------------\n', 'red', attrs=['bold'])
    time.sleep(1)
    print('\n"ACABO DE DESPERTAR DE UM SONO REVITALIZANTE, A LUA BRILHA NO CÉU')
    time.sleep(1)
    print('OS MORCEGOS VOAM ANIMADOS DANDO RASANTES NA CABEÇA DE QUEM PASSA NA RUA”\n')
    time.sleep(1)
    print('Qual a sequência correta de comandos?\n')
    cprint('-'* 80, 'red')
    time.sleep(1)
    print('1. ↑ ↑ ↑ ↓')
    print('2. ↑ → ↑ ↓')
    cprint('-'* 80, 'red')
    resp_enigma_porta()

    
def resp_enigma_porta():    
    resp_enigma = int(input('Digite sua resposta [1 ou 2]:'))

    if resp_enigma == 1:
        print('\nSua inteligência é o que te destaca, sempre.')
        time.sleep(1)
        print('Parabéns {}, pois quem não dispõe de tal destreza pagou com a vida o erro do enigma.'.format(nome_personagem))
        explicacao_encontro_gemeas()

    else:
        if resp_enigma == 2:
            print('\nA porta é amaldiçoada e quem erra o enigma paga com a vida.')
            cprint('-'* 80, 'red')
            time.sleep(1)
            cprint('GAME OVER!!!', 'yellow', 'on_red', attrs=['bold'])
            time.sleep(1)
            jogar_novamente()
        else:
            print('Resposta inválida!')
            print(resp_enigma_porta())


def resposta_abrir_porta_nao_entrou ():
    resposta_pergunta_abrir_porta = int(input('Digite sua escolha [1 ou 2]:'))
    if (resposta_pergunta_abrir_porta == 1):
        print('\nSempre curiosa, não é mesmo {}?\n'.format(nome_personagem))
        time.sleep(1)
        print('Ao caminhar para longe da porta, você se dá conta que está sendo observada...')
        time.sleep(1)
        print('Ao se dar conta, que o chato do Vamprico (apaixonado por você, desde sempre) está bisbilhotando...\n')
        print('Qual a sua escolha?')
        cprint('-'* 80, 'red')
        time.sleep(1)
        print('1. se aproxima dele...')
        time.sleep(1)
        print('2. vai até ele dar um sermão pela 1458ª vez.\n')
        cprint('-'* 80, 'red')
        resp_desistiu_entrar()
    elif (resposta_pergunta_abrir_porta == 2):
            explicacao_resp_enigma_porta()
    else:
        print('Resposta inválida')
        resposta_abrir_porta_nao_entrou()



def interacao_menininha ():
    resp_pergunta_menininho = int(input('Digite o número correspondente a ação que deseja:'))
    if (resp_pergunta_menininho == 1):
        print('\nElas apontam para uma porta aberta, que lembrava uma biblioteca, mas não disseram uma palavra.')
        explicacao_biblioteca_escrito_sangue()

    elif (resp_pergunta_menininho == 2):
        print('...')
        time.sleep(2)
        print('após um longo período de silêncio')
        time.sleep(1)
        print('você se lembra que parte dos boatos também diziam que elas não responde perguntas diretas sobre o castelo...\n')
        interacao_menininha ()
    
    else:
        print('Resposta inválida!')
        interacao_menininha()



def enimga_palavra_biblioteca():
    resp_enigma_palavra = input('\nDigite sua resposta:')
    if (resp_enigma_palavra.lower().strip() == 'tempo'):
        print('\nFantástico! A resposta está correta!')
        time.sleep(1)
        print('Pela fama de nerd que você tem, faz jus ter chego até aqui ')
        time.sleep(1)
        explicacao_sala_jantar()

    else:
        print('Cué, cué, cué, cuééééé...')
        cprint('GAME OVER!!!', 'yellow', 'on_red', attrs=['bold'])
        time.sleep(1)
        jogar_novamente()


def enimga_sala_jantar():
    resp_enigma_palavra = input('Digite a resposta:')
    if (resp_enigma_palavra.lower().strip() == 'nome'):
        print('\nIHULLLLLLLLL!')
        time.sleep(1)
        print('ACERTOOOOOU, você é mais nova imortal cheia dos recursos do pedaço! Sangue à vontade e ainda barras de ouro?')
        time.sleep(1)
        print('Sua teoria sobre o conhecimento como tesouro te recompensou lindamente.')
        cprint('-'* 80, 'red')
        time.sleep(1)
        cprint('***** FIM DE JOGO *****', 'magenta', attrs=['bold'])
        jogar_novamente()
    else:
        print('\nPerder no chefão é triste, né? Mas você pode tentar de novo...')
        cprint('-'* 80, 'red')
        time.sleep(1)
        cprint('GAME OVERRRRRRR!!!', 'yellow', 'on_red', attrs=['bold'])
        cprint('***** FIM DE JOGO *****', 'red', attrs=['bold'])
        jogar_novamente()
    


if __name__ == '__main__':
    jogar1()