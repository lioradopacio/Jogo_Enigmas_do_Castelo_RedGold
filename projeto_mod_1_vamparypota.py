import projeto_mod_1_escolhapersonagem

import time
from termcolor import cprint
import pyfiglet

nome_personagem = 'Vamparipota'
lista_resp = ['1', '2']

def jogar1():

    explicacao_missao_vamparipota()


def explicacao_missao_vamparipota():
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
    print('Você está na porta do castelo RedGold, {}, mas parece que a porta tem um enigme para abri-la.\n'.format(nome_personagem))
    time.sleep(1)
    print('Digite o número correspondente a ação que deseja:')
    time.sleep(1)
    cprint('-'* 80, 'red')
    print('1. Desistir e ir embora (nem combina com você)')
    time.sleep(1)
    print('2. Ver enigma!')
    cprint('-'* 80, 'red')
    resposta_abrir_porta_nao_entrou()

def resp_desistiu_entrar():
    condicao = True
    while condicao:
        resp_desistiu = input('Digite sua escolha [1 ou 2]:')
        if (resp_desistiu == '1') or (resp_desistiu == '2'):
            print('\nAo desistiu de entrar, você não se deu conta de que o sol já estava nascendo...')
            time.sleep(2)
            print('Um dos espelhos de dentro da casa, acabou refletindo um raio de sol em você.\n')
            cprint('GAME OVER! MORREU TORRADO.', 'yellow', 'on_red', attrs=['bold'])
            time.sleep(1)
            jogar_novamente()
            condicao = False
        else:
            print('Resposta inválida!')

def explicacao_resp_enigma_porta():
    cprint('\n----------------*ENIGMA DA PORTA*----------------\n', 'red', attrs=['bold'])
    time.sleep(1)
    print('\nQUANDO O SOL SUBIR, PESSOAS COMO VOCÊ SE ESCONDEM, PARA NO CAIR DA NOITE ALÇAREM VOO COMO MORCEGOS LIVRES.\n')
    time.sleep(1)
    print('Qual a sequência de comandos?\n')
    cprint('-'* 80, 'red')
    time.sleep(1)
    print('1. ↑ ↓ ↑ ↑')
    print('2. ↑ ↓ ↓ ↑')
    cprint('-'* 80, 'red')    
    time.sleep(1)
    resp_enigma_porta()

def resp_enigma_porta():
    resp_enigma = input('Digite sua resposta [1 ou 2]:')

    if (resp_enigma in lista_resp) and (resp_enigma == '1'):
        print('\nA porta é amaldiçoada e quem erra o enigma paga com a vida.')
        cprint('-'* 80, 'red')
        time.sleep(1)
        cprint('GAME OVER!!!', 'yellow', 'on_red', attrs=['bold'])
        time.sleep(1)
        jogar_novamente()
    else:
        if (resp_enigma in lista_resp) and (resp_enigma == '2'):
            print('\nSe safou, hein {}? Sabia que quem errou o enigma morreu? Parabéns, sua coragem e perspicacia te mantiveram vive no jogo.'.format(nome_personagem))
            time.sleep(1)
            explicacao_encontro_menininho()
        else:
            print('Resposta inválida!')
            print(resp_enigma_porta())


def resposta_abrir_porta_nao_entrou ():
    resposta_pergunta_abrir_porta = input('Digite sua escolha [1 ou 2]:')
    
    if (resposta_pergunta_abrir_porta in lista_resp) and (resposta_pergunta_abrir_porta == '1'):
        print('\nQuem te viu, quem te vê viu, {}. Mundialmente conhecido por sua coragem, aí dando meia volta logo de cara.\n'.format(nome_personagem))
        time.sleep(1)
        print('Porque você desistiu de entrar?\n')
        time.sleep(1)
        cprint('-'* 80, 'red')
        print('1.Fica para próxima!')
        time.sleep(1)
        print('2.Sinto uma estranha ligação com o castelo, mas não estou pronto para descobrir verdades hoje...')
        cprint('-'* 80, 'red')
        resp_desistiu_entrar()
    elif (resposta_pergunta_abrir_porta in lista_resp) and (resposta_pergunta_abrir_porta == '2'):
        explicacao_resp_enigma_porta()
    else:
        print('Resposta inválida')
        resposta_abrir_porta_nao_entrou ()


def interacao_menininho ():
    resp_pergunta_menininho = input('Digite o número correspondente a ação que deseja [1 ou 2]:')

    if (resp_pergunta_menininho in lista_resp) and (resp_pergunta_menininho == '1'):
        print('\nEle aponta para uma porta aberta, que lembrava um quarto, mas não diz uma palavra.')
        explicacao_quarto_escrito_sangue()
    
    else:
        if (resp_pergunta_menininho in lista_resp) and (resp_pergunta_menininho == '2'):
            print('\n...')
            time.sleep(2)
            print('após um longo período de silêncio,')
            time.sleep(2)
            print('você se lembra que parte dos boatos também diziam que ele não responde perguntas diretas sobre o castelo...\n')
            interacao_menininho ()
            
        else:
            print('Resposta inválida!')
            interacao_menininho()


def enimga_palavra_quarto():
    resp_enigma_palavra = input('\nDigite sua resposta:')

    if (resp_enigma_palavra.lower().strip() == 'amanhã') or (resp_enigma_palavra.lower().strip() == 'amanha') or (resp_enigma_palavra.lower().strip() == 'futuro'):
        print('\nGenial! A resposta está correta!')
        time.sleep(1)
        print('Impressionate sua perspicácia. Com tamanha inteligência está ficando fácil ganhar o que veio buscar.')
        time.sleep(1)
        explicacao_biblioteca()
    else:
        print('Cué, cué, cué, cuééééé...')
        time.sleep(1)
        cprint('GAME OVER!!!', 'yellow', 'on_red', attrs=['bold'])
        jogar_novamente()


def explicacao_encontro_menininho():
    print('\nAndando pelo castelo, você encontra um menininho pálido e solitário.')
    time.sleep(1)
    print('Boatos que ele sabe as passagens secretas do castelo onde estão as recompensas...\n')
    time.sleep(1)
    cprint('-'* 80, 'red')
    print('1. perguntar se há algum outro enigma para solucionar')
    time.sleep(1)
    print('2. tentar conversar com ele')
    cprint('-'* 80, 'red')
    interacao_menininho()


def explicacao_quarto_escrito_sangue():
    print('\nAo entrar no quarto se deparou com uma parede clara escrita com sangue, os seguintes dizeres:\n')
    time.sleep(1)
    print('EU NUNCA FUI, MAS SEMPRE SEREI. NINGUÉM NUNCA ME VIU, E NUNCA VERÃO. AINDA ASSIM, SOU A ESPERANÇA DE TODOS.\n')
    cprint('-'* 80, 'red')
    time.sleep(1)
    print('Quem sou eu?')
    time.sleep(1)
    print('\n***Dica*** _ _ _ _ _ _ ')
    enimga_palavra_quarto() 


def explicacao_biblioteca():
    print('\nNa biblioteca do castelo, você encontra um livro com uma página marcada...')
    time.sleep(1)
    print('quando abre na página encontra um pergaminho dobrado. Abre o pergaminho e lê:\n')
    time.sleep(1)
    print('SE UM MORCEGO VIVE CINCO DIAS E A CADA DIA ELE VOA QUATRO METROS, QUANTOS METROS ELE TERÁ PERCORRIDO EM UMA SEMANA?\n')
    cprint('-'* 80, 'red')
    enimga_biblioteca_morcego()


def enimga_biblioteca_morcego ():
    resp_enigma_morcego = int(input('Digite o número de metros:'))

    if (resp_enigma_morcego == 20):
        print('\nIHULLLLLLLLL!')
        time.sleep(1)
        print('ACERTOOOOOU, você é mais novo imortal cheio dos recursos do pedaço! Sangue à vontade e ainda barras de ouro?')
        time.sleep(1)
        print('Tá afim de uma amizade sincera? :}')
        time.sleep(1)
        cprint('***** FIM DE JOGO *****', 'green', attrs=['bold'])
        jogar_novamente()
    else:
        print('\nPerder no chefão é triste, né? Mas vida que segue.')
        cprint('-'* 80, 'red')
        time.sleep(1)
        cprint('GAME OVERRRRRRR!!!', 'yellow', 'on_red', attrs=['bold'])
        cprint('***** FIM DE JOGO *****', 'red', attrs=['bold'])
        jogar_novamente()


def jogar_novamente():
    resp_jogar_novamente = input('\nDeseja jogar novamente? [S/N]:')
    if (resp_jogar_novamente.upper().strip() == 'S'):
        projeto_mod_1_escolhapersonagem.escolha_personagem()
    elif (resp_jogar_novamente.upper().strip() == 'N'):
        print('Até a próxima!')
    else:
        print('Digite uma resposta válida!')
        jogar_novamente()


if __name__ == '__main__':
    jogar1()